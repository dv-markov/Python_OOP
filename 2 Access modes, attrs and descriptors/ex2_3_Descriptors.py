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
