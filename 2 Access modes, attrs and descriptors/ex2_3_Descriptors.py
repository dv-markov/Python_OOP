# 2.3 Дескрипторы (data descriptor и non-data descriptor)


# запись координат напрямую в защищенные атрибуты
class Point3D:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z


p0 = Point3D(1, 2, 3)


# использование объектов-свойств (декораторов property) для проверки входных данных
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом")

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, coord):
        self.verify_coord(coord)
        self._x = coord

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, coord):
        self.verify_coord(coord)
        self._y = coord

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, coord):
        self.verify_coord(coord)
        self._z = coord


# класс работает, но получилось дублирование кода для каждого объекта-свойства
p = Point3D(3, 2, 1)
print(p.__dict__)
# p1 = Point3D(3, 2, '1')
# Оптимизировать эту задачу можно с помощью дескрипторов


# Виды дескрипторов
# 1. non-dta descriptor (дескриптор не данных) - класс содержит магический метод __get__
# 2. data descriptor (дескриптор данных) - класс содержит также методы __set__ и __del__ (или один из них)
# Например, для работы с целыми числами можно создать класс Integer (дескриптор данных)
class Integer:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print(f"__set__: {self.name} = {value}")
        instance.__dict__[self.name] = value


# реализация класса Point3D с дескриптором Integer
class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом")


print('\n', 'Работа класса через дескриптор:', sep='')
p = Point3D(1, 2, 3)
print(p.__dict__)


# Реализация метода проверки входных данных в дескрипторе Integer
class Integer:
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.verify_coord(value)
        instance.__dict__[self.name] = value


class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


print('\n', 'Работа класса через дескриптор с проверкой входных данных:', sep='')
p = Point3D(3, 2, 1)
print(p.__dict__)
# Ошибка ValueError при проверке входных данных
# p = Point3D(3, 2, '1')


# Реализация __get__ и __set__ в дескрипторе Integer через getattr и setattr
# Более правильный подход с точки зрения Python
class Integer:
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coord(value)
        setattr(instance, self.name, value)


class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


print('\n', 'Работа класса через дескриптор с проверкой входных данных и getattr / setattr:', sep='')
p = Point3D(10, 20, 30)
print(p.__dict__)
# дескрипторы данных работают и на запись, и на считывание
p.z = 100
print(p.z)


# Дескриптор не-данных работает только на считывание информации (__get__)
# Имеет тот же приоритет, что и обычные атрибуты класса
# Пример - реализация нового дескриптора не-данных xr
class ReadIntX:
    def __set_name__(self, owner, name):
        self.name = "_x"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()
    xr = ReadIntX()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


print('\n', 'Non-data descriptor', sep='')
p = Point3D(1, 2, 3)
print(p.xr, p.__dict__)
# дескрипторы не-данных работают только на считывание
# при попытке записи создается новый локальный атрибут экземпляра класса
p.xr = 5
print(p.xr, p.__dict__)


# Если превратить ReadIntX в дескриптор данных, приоритет изменится
class ReadIntX:
    def __set_name__(self, owner, name):
        self.name = "_x"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()
    xr = ReadIntX()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


print('\n', 'Non-data descriptor -> Data descriptor', sep='')
p = Point3D(1, 2, 3)
print(p.xr, p.__dict__)
# при попытке записи изменяется существующий локальный атрибут экземпляра класса
p.xr = 5
print(p.xr, p.__dict__)
# приоритет при работе с дескрипторами данных выше, чем для локальных свойств экземпляра
p.__dict__['xr'] = 7
print(p.xr, p.__dict__)

print("""
Задачи""")


# Task 6
class FloatValue:
    @classmethod
    def verify_float(cls, number):
        if type(number) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_float(value)
        setattr(instance, self.name, value)


class Cell:
    value = FloatValue()

    def __init__(self, cell_value=0.0):
        self.value = cell_value


class TableSheet:
    def __init__(self, N, M):
        self.cells = [[Cell() for _ in range(M)] for _ in range(N)]


table = TableSheet(5, 3)
x = 1.0
for row in table.cells:
    for cell in row:
        cell.value = x
        x += 1

print(table.cells)
for row in table.cells:
    for cell in row:
        print(cell.value, end=' ')
    print()


# Task 7
class ValidateString:
    def __init__(self, min_length=3, max_length=100):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):
        return type(string) is str and self.min_length <= len(string) <= self.max_length


class StringValue:
    def __init__(self, validator=ValidateString()):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validator.validate(value):
            setattr(instance, self.name, value)


class RegisterForm:
    login = StringValue()
    password = StringValue()
    email = StringValue()

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        print(f"""<form>
Логин: {self.login}
Пароль: {self.password}
Email: {self.email}
</form>""")


validate1 = ValidateString(min_length=3, max_length=100)
print(validate1.__dict__)
print(validate1.validate('Ва'))

reg = RegisterForm('Вася', '123', 'email')
reg.login = 'Бо'
print(reg.__dict__)
print(reg.get_fields())
reg.show()


# Task 8
class SuperShop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class StringValue:
    def __init__(self, min_length=2, max_length=50):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.name = f'_{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) == str and self.min_length <= len(value) <= self.max_length:
            setattr(instance, self.name, value)


class PriceValue:
    def __init__(self, max_value=10_000):
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = f'_{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) in (int, float) and 0 <= value <= self.max_value:
            setattr(instance, self.name, value)


class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name, price):
        self.name = name
        self.price = price


shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")

new_book = Product("Курс по Python Django", 3000)
shop.add_product(new_book)
shop.remove_product(new_book)
for p in shop.goods:
    print(f"{p.name}: {p.price}")

# Variant 2 - с наследованием и полиморфизмом
# class Descriptor:
#     def __set_name__(self, owner, name):
#         self.name = "__" + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         if self.is_valid(value):
#             setattr(instance, self.name, value)
#
#
# class StringValue(Descriptor):
#     def __init__(self, minl=0, maxl=50):
#         self.minl = minl
#         self.maxl = maxl
#
#     def is_valid(self, value):
#         return isinstance(value, str) and self.minl <= len(value) <= self.maxl
#
#
# class PriceValue(Descriptor):
#     def __init__(self, maxl=10000):
#         self.maxl = maxl
#
#     def is_valid(self, value):
#         return isinstance(value, (int, float)) and value <= self.maxl


# Task 9
class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things = []

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        if self.get_total_weight() + thing.weight <= self.max_weight:
            self.things.append(thing)

    def remove_thing(self, indx):
        self.things.pop(indx)

    def get_total_weight(self):
        return sum(map(lambda x: x.weight, self.things))


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
bag.remove_thing(1)
# присвоить и вернуть значение
print(w := bag.get_total_weight())
for t in bag.things:
    print(f"{t.name}: {t.weight}")
print(bag.__dict__)


# Task 10
class TVProgram:
    def __init__(self, channel_name):
        self.ch_name = channel_name
        self.items = []

    def add_telecast(self, tl):
        self.items.append(tl)

    def remove_telecast(self, indx):
        for i in range(len(self.items)):
            if self.items[i].uid == indx:
                self.items.pop(i)
                break  # можно не писать, если есть несколько передач с одинаковым id


class Telecast:
    def __init__(self, uid, name, duration):
        self.uid = uid
        self.name = name
        self.duration = duration

    @property
    def uid(self):
        return self.__id

    @uid.setter
    def uid(self, uid):
        self.__id = uid

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        self.__duration = duration


pr = TVProgram("Первый канал")
pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(2, "Новости", 2000))
pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
for t in pr.items:
    print(f"{t.name}: {t.duration}")

pr.remove_telecast(2)
for t in pr.items:
    print(f"{t.name}: {t.duration}")
    print(t.__dict__)


# Variant 2 - Решение С. Балакирева
#     def remove_telecast(self, indx):
#         t_lst = tuple(filter(lambda x: x.uid == indx, self.items))
#         for t in t_lst:
#             self.items.remove(t)
