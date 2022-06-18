# 1.5 Инициализатор __init__ и финализатор __del__

#  __init__(self) - инициализатор объекта класса
class Point:
    color = 'red'
    circle = 2

    def __init__(self):
        print("вызов __init__")
        self.x = 0
        self.y = 0

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y


pt = Point()
pt.set_coords(1, 2)
print(pt.__dict__)

# метод __init__ вызывается при создании объекта, сразу после __new__
pt2 = Point()
print(pt2.__dict__)


class Point2:
    color = 'red'
    circle = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y


pt3 = Point2(10, 20)
print(pt3.__dict__)
# имена атрибутов устанавливаются в методе self.x =

# при создании объекта класса без атрибутов произойдет ошибка
# pt = Point2()

# можно указать именованные параметры в качестве формальных
class Point3:
    color = 'red'
    circle = 2

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y


# тогда создать экземпляр можно без аргументов
pt4 = Point3()
print(pt4.__dict__)

pt5 = Point3(5)
print(pt5.__dict__)

pt6 = Point3(6, 7)
print(pt6.__dict__)


#  __del__(self) - финализатор объекта класса
class Point4:
    color = 'red'
    circle = 2

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        # print("Удаление экземпляра: " + str(self))
        pass

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y


pt7 = Point4()
print(pt7.__dict__)

# объект удаляется при исчезновении всех ссылок на него
# после вызова метода __del__ объект прекращает свое существование

print("""
Задачи""")


# Task 2
class Money:

    def __init__(self, money):
        self.money = money


my_money = Money(100)
your_money = Money(1000)
print(my_money.__dict__)
print(your_money.__dict__)


# Task 3
class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


points = [Point(i, i) for i in range(1, 2000, 2)]
points[1].color = 'yellow'
print(points[1].__dict__)


# Task 4
from random import randrange as rand
from random import randrange, choice

class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


# Variant 1
# elements = []
# for i in range(217):
#     k = [rand(1000) for _ in range(4)]
#     elements.append(choice([Line, Rect, Ellipse])(*k))
#
# # print(elements)
# for x in elements:
#     if isinstance(x, Line):
#         x.sp, x.ep = (0, 0), (0, 0)
#     # print(x.__dict__)


# Variant 2
elements = [choice([Line, Rect, Ellipse])(*[randrange(1000) for _ in range(4)]) for i in range(217)]

# print(elements)
for x in elements:
    if isinstance(x, Line):
        x.sp = x.ep = 0, 0
    # print(x.__dict__)


# Variant 3
# cls = (Line, Rect, Ellipse)
#
# elements = [choice(cls)(*sample(range(10), 4)) for _ in range(217)]
#
# for i in elements:
#     if isinstance(i, Line):
#         i.sp = i.ep = 0, 0


# Task 5
class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        triangle_sides = self.__dict__.values()
        if any(type(x) not in (int, float) or x < 1 for x in triangle_sides):
            return 1
        elif sum(triangle_sides) < 2 * max(triangle_sides):
            return 2
        return 3


# a, b, c = map(int, input().split())
a = 3; b = 4; c = 5
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())


# Task 6
class Graph:
    def __init__(self, data, is_show=True):
        self.data = data[:]
        self.is_show = is_show

    def set_data(self, data):
        self.data = data[:]

    def check_show(self):
        if self.is_show:
            return True
        else:
            print("Отображение данных закрыто")

    def show_table(self):
        if self.check_show():
            print(*self.data)

    def show_graph(self):
        if self.check_show():
            print("Графическое отображение данных:", *self.data)

    def show_bar(self):
        if self.check_show():
            print("Столбчатая диаграмма:", *self.data)

    def set_show(self, fl_show):
        self.is_show = fl_show


# data_graph = list(map(int, input().split()))
data_graph = list(map(int, "8 11 10 -32 0 7 18".split()))
# a = str(*data_graph)
gr_1 = Graph(data_graph)
gr_1.show_bar()
gr_1.set_show(False)
gr_1.show_table()

print(gr_1.__dict__)
gr_1.set_show(True)
gr_1.show_table()
gr_1.set_show(False)
gr_1.show_table()

gr_1.set_show(True)
gr_1.show_graph()
gr_1.set_show(False)
gr_1.show_graph()

gr_1.set_show(True)
gr_1.show_bar()
gr_1.set_show(False)
gr_1.show_bar()
