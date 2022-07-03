# 2.1 Режимы доступа public, private, protected. Сеттеры и геттеры

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


pt = Point(1, 2)
print(pt.x, pt.y)

pt.x = 200
pt.y = "coord_y"
print(pt.x, pt.y)

# Режимы доступа:
# attribute (без подчеркиваний) - публичное свойство (public)
# _attribute (с одним _) - режим доступа protected (для обращения внутри класса и во всех дочерних классах)
# __attribute (с двумя __) - режим доступа private (обращение только внутри класса)


# _protected
class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y


pt = Point(1, 2)
print(pt._x, pt._y)

pt._x = 200
pt._y = "coord_y"
print(pt._x, pt._y)

# режим protected - _ лишь сигнализирует о том, что данное свойство является защищенным,
# но не запрещает доступ извне
# это внутренние служебные переменные, к ним лучше не обращаться извне


# __private
class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    # setter / сеттер
    def set_coord(self, x, y):
        self.__x = x
        self.__y = y

    # getter / геттер
    def get_coord(self):
        return self.__x, self.__y


pt = Point(1, 2)
# ссылка на защищенные переменные не работает
# print(pt.__x, pt.__y)

# через функцию обращаться можно
pt.set_coord(10, 20)
print(pt.get_coord())

# сеттеры и геттеры - интерфейсные методы, служат для работы с защищенными переменными класса или его экземпляра
# чтобы не нарушить работу класса, следует взаимодействовать с ним только через публичные свойства и методы
print(pt.__dict__)


# сеттеры и геттеры также используют для проверки типа данных
class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def set_coord(self, x, y):
        if type(x) in (int, float) and type(y) in (int, float):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("координаты должны быть числами")

    def get_coord(self):
        return self.__x, self.__y


pt = Point(1, 2)

pt.set_coord(10, 20)
# pt.set_coord(10, "qwerty")  # вызовет ошибку ValueError
print(pt.get_coord())


# добавление приватного метода
class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("координаты должны быть числами")

    def get_coord(self):
        return self.__x, self.__y


pt = Point(1, 2)
pt.set_coord(1000, 2000)
print(pt.get_coord())

print(dir(pt))
print(pt._Point__x)  # так делать крайне не рекомендуется, иначе возможны непредвиденные ошибки
print(pt._Point__check_value(5))  # с защищенным методом аналогично


from accessify import private, protected


# защита методов класса от доступа извне с помощью accessify
class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y

    @private
    @classmethod
    def check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("координаты должны быть числами")

    def get_coord(self):
        return self.__x, self.__y


pt = Point(1, 2)
pt.set_coord(300, 500)
print(pt.get_coord())

# работа accessify
# print(pt.check_value(5))
# выдает ошибку accessify.errors.InaccessibleDueToItsProtectionLevelException:
# Point.check_value() is inaccessible due to its protection level


print("""
ЗАДАЧИ""")


# Task 3
class Clock:
    def __init__(self, tm=0):
        self.__time = 0
        if self.__check_time(tm):
            self.__time = tm

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time

    @staticmethod
    def __check_time(tm):
        return type(tm) == int and 0 <= tm <= 100_000


clock0 = Clock('500')
print(clock0.get_time())
clock0.set_time(100)
print(clock0.get_time())

clock = Clock(4530)
print(clock.get_time())

# Variant 2
# class Clock:
#     MIN_TIME = 0
#     MAX_TIME = 100_000
#
#     def __init__(self, time=0):
#         self.__time = time if self.__check_time(time) else 0
#
#     def set_time(self, tm):
#         if self.__check_time(tm):
#             self.__time = tm
#
#     def get_time(self):
#         return self.__time
#
#     @classmethod
#     def __check_time(cls, tm):
#         return type(tm) is int and cls.MIN_TIME <= tm < cls.MAX_TIME


# Task 4
class Money:
    def __init__(self, money):
        if self.__check_money(money):
            self.__money = money

    def set_money(self, money):
        if self.__check_money(money):
            self.__money = money

    def get_money(self):
        return self.__money

    def add_money(self, mn):
        self.__money += mn.get_money()

    @staticmethod
    def __check_money(mn):
        return type(mn) == int and mn >= 0


mn_1 = Money(10)
mn_2 = Money(20)
mn_1.set_money(100)
mn_2.add_money(mn_1)
m1 = mn_1.get_money()    # 100
m2 = mn_2.get_money()    # 120

print(m1, m2)


# Task 5
class Book:
    def __init__(self, auth, title, price):
        self.__title = title
        self.__author = auth
        self.__price = price

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_price(self, price):
        self.__price = price

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price


book = Book('автор', 'название', 'цена')
print(book.get_title(), book.get_author(), book.get_price())


# Task 7
class Line:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def set_coords(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_coords(self):
        return self.__x1, self.__y1, self.__x2, self.__y2

    def draw(self):
        print(self.__x1, self.__y1, self.__x2, self.__y2)


line = Line(1, 2, 3, 4)
print(line.get_coords())
line.set_coords(5, 6, 7, 8)
line.draw()


# Task 8
class Point:
    def __init__(self, x, y):
        if self.check_coord(x) and self.check_coord(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты точки должны быть числами")

    @staticmethod
    def check_coord(x):
        return type(x) in (int, float)

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, *args):
        if len(args) == 2 and self.check_points(*args):
            self.__sp = args[0]
            self.__ep = args[1]
        elif len(args) == 4:
            self.__sp = Point(*args[:2])
            self.__ep = Point(*args[2:])
        else:
            raise ValueError("Координаты прямоугольника должны быть точками или числами")

    @staticmethod
    def check_points(*args):
        return all(map(lambda x: isinstance(x, Point), args))

    def set_coords(self, sp, ep):
        if self.check_points(sp, ep):
            self.__sp = sp
            self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(f"Прямоугольник с координатами: {self.__sp.get_coords()} {self.__ep.get_coords()}")


pt = Point(100, 200)
print(pt.__dict__)
print(pt.get_coords())

rect = Rectangle(0, 0, 20, 34)
print(rect.get_coords())
rect.draw()

rect2 = Rectangle(Point(100, 100), Point(200, 300))
rect2.set_coords(Point(500, 500), Point(700, 700))
print(rect2.get_coords())
rect2.draw()

