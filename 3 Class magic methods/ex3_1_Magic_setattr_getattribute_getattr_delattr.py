# 3.1 Магические методы __setattr__, __getattribute__, __getattr__ и __delattr__

# свойства и методы - это аттрибуты класса
# данный класс содержит 4 атрибута: 2 свойства и 2 имени метода (__init__ и set_coord, остальные добавлены позже)
class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    # создает новый локальный атрибут внутри экземпляра класса, не меняет сам атрибут класса
    def set_bound(self, left):
        self.MIN_COORD = left

    # меняет атрибут класса
    @classmethod
    def set_bound2(cls, left):
        cls.MIN_COORD = left


pt1 = Point(1, 2)
pt2 = Point(10, 20)

# если какой-то атрибут не существует в экземпляре класса, поиск переходит во внешнее пространство - сам класс
print(pt1.MAX_COORD)

# изменение локального атрибута
pt1.set_bound(-100)
print(pt1.__dict__)
print(Point.__dict__)

# изменение атрибута класса
pt2.set_bound2(-100)
print(pt2.__dict__)
print(Point.__dict__)


# Магические методы для атрибутов
# __setattr__(self, key, value) - автоматически вызывается при изменении свойства key класса
# __getattribute__(self, item) - автоматически вызывается при получении свойства класса с именем item
# __getattr__(self, item) - автоматически вызывается при получении несуществующего свойства item класса
# __delattr__(self, item) - автоматически вызывается при удалении свойства item (не важно, существует оно или нет)


# __getattribute__
class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    @classmethod
    def set_bound2(cls, left):
        cls.MIN_COORD = left

    # вызывается, когда происходит обращение к атрибуту через экземпляр класса, возвращает значение атрибута
    def __getattribute__(self, item):
        print("__getattribute__")
        return object.__getattribute__(self, item)

    # может использоваться для запрещения доступа напрямую к переменным
    # управление обращение к атрибуту
    def __getattribute__(self, item):
        if item == "x":
            raise ValueError("доступ запрещен")
        else:
            return object.__getattribute__(self, item)


pt1 = Point(1, 2)
pt2 = Point(10, 20)
# a = pt1.x
# print(a)
b = pt1.y
print(b)


# __setattr__
class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    # вызывается при создании или изменении локальных свойств
    def __setattr__(self, key, value):
        print("__setattr__")
        object.__setattr__(self, key, value)

    # можно запретить создавать локальный атрибут в экземплярах класса
    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError('недопустимое имя атрибута')
        else:
            object.__setattr__(self, key, value)
            # если на выходе явно присвоить атрибуту значение
            # self.x = value  # будет рекурсия
            # поэтому следует делать это через __dict__
            self.__dict__[key] = value  # но лучше делать это через object


pt1 = Point(1, 2)
pt2 = Point(10, 20)
# выдаст ошибку
# pt2.z = 123
pt2.y = 25


# __getattr__
class Point2:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    # обращение к несуществующему атрибуту класса
    # если прописан, вызывается вместо AttributeError
    def __getattr__(self, item):
        print("__getattr__: " + item)

    # переопределение
    def __getattr__(self, item):
        return False


p1 = Point2(1, 2)
p2 = Point2(10, 20)
print(p1.yy)
print(p2.MAX_COORD)


# __delattr__
class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    # вызывается при удалении атрибута экземпляра класса
    # позволяет контролировать удаление атрибутов класса
    def __delattr__(self, item):
        print("__delattr__: " + item)
        object.__delattr__(self, item)


pt2 = Point(10, 20)
del pt2.x
print(pt2.__dict__)

print("""
Задачи""")


# Task 3
class Book:
    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key in ('title', 'author') and type(value) != str or key in ('pages', 'year') and type(value) != int:
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            object.__setattr__(self, key, value)


book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)
print(book.__dict__)

# Variant 2 - через аннотацию типов
# class Book:
#     title: str
#     author: str
#     pages: int
#     year: int
#
#     def __init__(
#             self,
#             title: str = "",
#             author: str = "",
#             pages: int = 0,
#             year: int = 0,
#     ) -> None:
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.year = year
#
#     def __setattr__(self, key, value) -> None:
#         if not isinstance(value, self.__annotations__.get(key, object)):
#             raise TypeError("Неверный тип присваиваемых данных.")
#         super().__setattr__(key, value)
#
#     def __repr__(self) -> str:
#         return f"{self.title} - {self.author}"
#
# book = Book(title="Python ООП", author="Сергей Балакирев", year=2022, pages=123)


# Task 4
class Shop:
    def __init__(self, shop_name):
        self.shop_name = shop_name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    attrs = {'id': (int, ), 'name': (str, ), 'weight': (int, float), 'price': (int, float)}
    __id = 0

    @classmethod
    def __get_id(cls):
        cls.__id += 1
        return cls.__id

    def __init__(self, name, weight, price):
        self.id = self.__get_id()
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if type(value) not in self.attrs.get(key) or key in ('weight', 'price') and value <= 0:
            # not isinstance(value, self.attrs.get(key))
            raise TypeError("Неверный тип присваиваемых данных.")
        super().__setattr__(key, value)

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        super().__delattr__(item)


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
shop.remove_product(book)
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")


# Task 5
class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, indx):
        self.modules.pop(indx)


class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        self.lessons.pop(indx)


class LessonItem:
    title: str
    practices: int
    duration: int

    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if not isinstance(value, self.__annotations__.get(key)) or type(value) == int and value <= 0:
            raise TypeError("Неверный тип присваиваемых данных.")
        return super().__setattr__(key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item not in self.__annotations__:
            super().__delattr__(item)


course = Course("Python ООП")
module_1 = Module("Часть первая")
module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
module_1.add_lesson(LessonItem("Урок 3", 5, 800))
module_1.remove_lesson(0)
course.add_module(module_1)
module_2 = Module("Часть вторая")
module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
course.add_module(module_2)
delattr(module_2.lessons[0], 'title')

for mod in course.modules:
    print(mod.name)
    for lsn in mod.lessons:
        print(lsn.__dict__)


# Task 6
class Museum:
    def __init__(self, name):
        self.name = name
        self.exhibits = []

    def add_exhibit(self, obj):
        self.exhibits.append(obj)

    def remove_exhibit(self, obj):
        self.exhibits.remove(obj)

    def get_info_exhibit(self, indx):
        return f"Описание экспоната {self.exhibits[indx].name}: {self.exhibits[indx].descr}"


class Picture:
    def __init__(self, name, author, descr):
        self.name = name
        self.author = author
        self.descr = descr


class Mummies:
    def __init__(self, name, location, descr):
        self.name = name
        self.location = location
        self.descr = descr


class Papyri:
    def __init__(self, name, date, descr):
        self.name = name
        self.date = date
        self.descr = descr


mus = Museum("Эрмитаж")
mus.add_exhibit(Picture("Балакирев с подписчиками пишет письмо иноземному султану", "Неизвестный автор",
                        "Вдохновляющая, устрашающая, волнующая картина"))
mus.add_exhibit(Mummies("Балакирев", "Древняя Россия",
                        "Просветитель XXI века, удостоенный мумификации"))
p = Papyri("Ученья для, не злата ради", "Древняя Россия",
           "Самое древнее найденное рукописное свидетельство о языках программирования")
mus.add_exhibit(p)
for x in mus.exhibits:
    print(x.descr)
for i in range(len(mus.exhibits)):
    print(mus.get_info_exhibit(i))


# Variant 2 - с наследованием классов
# class Museum:
#     def __init__(self, name):
#         self.name = name
#         self.exhibits = []
#
#     def add_exhibit(self, obj):
#         self.exhibits.append(obj)
#
#     def remove_exhibit(self, obj):
#         self.exhibits.remove(obj)
#
#     def get_info_exhibit(self, indx):
#         obj = self.exhibits[indx]
#         return f"Описание экспоната {obj.name}: {obj.descr}"
#
#
# class Exhibit:
#     def __init__(self, name, descr):
#         self.name = name
#         self.descr = descr
#
#
# class Picture(Exhibit):
#     def __init__(self, name, author, descr):
#         super().__init__(name, descr)
#         self.author = author
#
#
# class Mummies(Exhibit):
#     def __init__(self, name, location, descr):
#         super().__init__(name, descr)
#         self.location = location
#
#
# class Papyri(Exhibit):
#     def __init__(self, name, date, descr):
#         super().__init__(name, descr)
#         self.date = date


# Task 7
class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []

    def add_app(self, app):
        for a in self.apps:
            if a.__class__ == app.__class__:
                break
        else:
            self.apps.append(app)
        # if not any(filter(lambda x: type(x) == type(app), self.apps)):
        #     self.apps.append(app)

    def remove_app(self, app):
        if app in self.apps:
            self.apps.remove(app)


class AppVK:
    def __init__(self, name="ВКонтакте"):
        self.name = name


class AppYouTube:
    def __init__(self, memory_max, name="YouTube"):
        self.name = name
        self.memory_max = memory_max


class AppPhone:
    def __init__(self, phone_list: dict, name="Phone"):
        self.name = name
        self.phone_list = phone_list


app_1 = AppVK() # name = "ВКонтакте"
app_2 = AppYouTube(1024) # name = "YouTube", memory_max = 1024
app_3 = AppPhone({"Балакирев": 1234567890, "Сергей": 98450647365, "Работа": 112}) # name = "Phone", phone_list = словарь с контактами

print(app_1.__dict__)
print(app_2.__dict__)
print(app_3.__dict__)

sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)


# Variant 2
#     def add_app(self, app):
#         for i in self.apps:
#             if type(app) == type(i):
#                 app = None
#         if app:
#             self.apps.append(app)


# Task 8
class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    def __setattr__(self, key, value):
        if type(value) not in (int, float):
            raise TypeError("Неверный тип присваиваемых данных.")
        if key == 'radius' and value > 0 or key != 'radius':
            super().__setattr__(key, value)

    def __getattr__(self, item):
        return False


c = Circle(2, 5, 10)
print(c.__dict__)

circle = Circle(10.5, 7, -22)
circle.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
x, y = circle.x, circle.y
res = circle.name # False, т.к. атрибут name не существует
print(x, y, circle.radius, res)


# Task 9
class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(self, a, b, c):
        self.__a = self.__b = self.__c = None  # задание пустых свойств на случай ввода неверных данных
        self.a = a
        self.b = b
        self.c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        self.__c = value

    def __setattr__(self, key, value):
        if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        if type(value) in (int, float) and self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            super().__setattr__(key, value)


d = Dimensions(10.5, 20.1, 30)
d.a = 8
d.b = 15
a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
print(a, b, c)
# d.MAX_DIMENSION = 10  # исключение AttributeError


# Task 10
import time


class GeyserClassic:
    MAX_DATE_FILTER = 100
    filt_dict = {1: 'Mechanical', 2: 'Aragon', 3: 'Calcium'}

    def __init__(self):
        self.filters = [None]*3

    def add_filter(self, slot_num, filt):
        if self.filt_dict.get(slot_num) == type(filt).__name__ and self.filters[slot_num-1] is None:
            self.filters[slot_num-1] = filt
            print(f'Filter {filt} of type {type(filt).__name__} was installed to slot {slot_num}')

    def remove_filter(self, slot_num):
        self.filters[slot_num-1] = None

    def get_filters(self):
        return tuple(self.filters)

    def water_on(self):
        return all(self.filters) and all(map(lambda f: 0 <= time.time() - f.date <= self.MAX_DATE_FILTER, self.filters))


class FiltClass:
    f = True

    def __init__(self, date):
        self.date = date
        self.f = False

    def __setattr__(self, key, value):
        if self.f:
            super().__setattr__(key, value)


class Mechanical(FiltClass):
    pass


class Aragon(FiltClass):
    pass


class Calcium(FiltClass):
    pass


my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on()  # False
print(w)
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on()  # True
print(w)
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
print(f1, f2, f3)
my_water.remove_filter(3)
my_water.add_filter(3, Calcium(time.time()))  # повторное добавление в занятый слот невозможно
my_water.add_filter(2, Calcium(time.time()))  # добавление в "чужой" слот также невозможно
