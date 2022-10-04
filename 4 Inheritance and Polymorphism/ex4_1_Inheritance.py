# 4.1 Наследование в объектно-ориентированном программировании

class Geom:  # базовый (родительский) класс
    name = "Geom"

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @staticmethod  # почему вызов из текста программы не работает без статикметода?
    def draw():
        print("Рисование примитива")


class Line(Geom):  # подкласс (дочерний) класс
    name = "Line"

    def draw(self):
        print("Рисование линии")


class Rectangle(Geom):  # подкласс (дочерний) класс
    def draw(self):
        print("Рисование прямоугольника")


g = Geom
l = Line()
r = Rectangle()
print(g.name, l.name, r.name)
l.set_coords(1, 2, 3, 4)
r.set_coords(5, 6, 7, 8)
print(l.__dict__)
print(r.__dict__)

# в базовых классах стоит вызывать те методы, которые определены в нем, или в его родительских классах, но не в дочерних

g.draw()
l.draw()
r.draw()

print("""
Задачи
""")


# Task 4
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cat(Animal):
    def __init__(self, name, age, color, weight):
        super().__init__(name, age)
        self.color = color
        self.weight = weight

    def get_info(self):
        return f"{self.name}: {self.age}, {self.color}, {self.weight}"


class Dog(Animal):
    def __init__(self, name, age, breed, size):
        super().__init__(name, age)
        self.breed = breed
        self.size = size

    def get_info(self):
        return f"{self.name}: {self.age}, {self.breed}, {self.size}"


cat = Cat('кот', 4, 'black', 2.25)
dog = Dog('Шарик', 7, 'Zwergpinscher', 8)
print(cat.get_info())
print(dog.get_info())


# Task 5
class Thing:
    __id = -1

    def __init__(self, name, price):
        self.id = self.__get_id()
        self.name = name
        self.price = price
        self.weight = None
        self.dims = None
        self.memory = None
        self.frm = None

    @classmethod
    def __get_id(cls):
        Thing.__id += 1
        return cls.__id

    def get_data(self):
        return tuple(self.__dict__.values())


class Table(Thing):
    def __init__(self, name, price, weight, dims):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing):
    def __init__(self, name, price, memory, frm):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm


a = Thing(1, 2000)
b = Thing(2, 3000)
print(a.__dict__)
print(b.__dict__)
print(a.get_data())

table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(*table.get_data())
print(*book.get_data())


# Task 6
class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass

