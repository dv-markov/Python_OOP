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


# Task 7
class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, mem_slots, total_mem_slots=4):
        self.name = name
        self.cpu = cpu
        # self.total_mem_slots = 4
        self.total_mem_slots = total_mem_slots
        self.mem_slots = mem_slots[:total_mem_slots]

    def get_config(self):
        return [f'Материнская плата: {self.name}',
                f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
                f'Слотов памяти: {self.total_mem_slots}',
                'Память: '+'; '.join([f'{x.name} - {x.volume}' for x in self.mem_slots])]


# при вызове переменных f-строки использовать предпочтительнее, они быстрее и работают с любыми типами данных
mb = MotherBoard('Asus', CPU('Intel', '3 GHz'), [Memory('Kingston', '16 Gb'), Memory('Transcend', '16 Gb')])
print(mb.get_config())

# Variant 2
# class MotherBoard:
#     def __init__(self, name, cpu, *mem_slots):
#         self.name = name
#         self.cpu = cpu
#         self.total_mem_slots = 4
#         self.mem_slots = mem_slots[:self.total_mem_slots]
#
# mb = MotherBoard('Asus', CPU('Intel', 3000), Memory('Kingston', 16000), Memory('Transcend', 16000))


# Task 8
class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        if 0 <= indx < len(self.goods):
            self.goods.pop(indx)

    def get_list(self):
        # обращаться к значениям свойств лучше по имени, а не через словарь
        return [f"{x.name}: {x.price}" for x in self.goods]

        # return [f'{list(x.__dict__.values())[0]}: {list(x.__dict__.values())[1]}' for x in self.goods]

        # return [x.__dict__.values() for x in self.goods]
        # return list(map(lambda k, v: f"{k}: {v}", [x.__dict__.values() for x in self.goods]))

        # res = []
        # for good in self.goods:
        #     k, v = good.__dict__.values()
        #     res.append(f'{k}: {v}')
        # return res


class Goods:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Table(Goods):
    pass


class TV(Goods):
    pass


class Notebook(Goods):
    pass


class Cup(Goods):
    pass


cart = Cart()
cart.add(TV("Samsung", 50000))
cart.add(TV("LG", 40000))
cart.add(Table("Unika Moblar", 70000))
cart.add(Notebook("Apple", 150000))
cart.add(Notebook("Dell", 100000))
cart.add(Cup("Starbucks", 2000))

print(cart.get_list())
