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


