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

