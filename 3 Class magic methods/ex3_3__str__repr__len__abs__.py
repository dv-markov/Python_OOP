# 3.3 Методы __str__, __repr__, __len__, __abs__


# Методы __str__ и __repr__
import math


class Cat:
    def __init__(self, name):
        self.name = name

    # метод __repr__ предназначен для вывода информации в режиме отладки
    def __repr__(self):
        return f"{self.__class__}: {self.name}"

    # метод __str__ предназначен для вывода информации для пользователя
    # если не определен метод __str__, то по умолчанию вызывается метод __repr__
    def __str__(self):
        return f"{self.name}"


cat = Cat("Васька")
print(cat)
print(str(cat))


# Методы __len__ и __abs__
class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return list(map(abs, self.__coords))


p = Point(1, -2, -5)
print(len(p))
print(abs(p))

print("""
Задачи""")


# Task 2
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Книга: {self.title}; {self.author}; {self.pages}"


import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['Python ООП', 'Балакирев С.М.', '1024']
book = Book(*lst_in)
print(book)


# Task 3
class Model:
    def __init__(self):
        self.fields = {}

    def query(self, **kwargs):
        self.fields.update(kwargs)

    def __str__(self):
        lst = [f"{key} = {value}" for key, value in self.fields.items()]
        return "Model: " + ", ".join(lst) if self.fields else "Model"


model = Model()
model.query(id=1, fio='Sergey', old=33)
model.query(id=2)
print(model.__dict__)
print(model)


# Task 4
class WordString:
    def __init__(self, string=None):
        self.string = string

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, s):
        self.__string = s

    def __len__(self):
        return len(self.string.split())

    def __call__(self, indx, *args, **kwargs):
        return self.string.split()[indx]


words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")

words.string = "Курс по Python    ООП от  Сергея Балакирева"
print(words.__dict__)


# Task 5
# class ObjListValue:
#     def __set_name__(self, owner, name):
#         self.name = "__" + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         setattr(instance, self.name, value)
#
#
# class ObjList:
#     prev = ObjListValue()
#     next = ObjListValue()
#     data = ObjListValue()
#
#     pass


class ObjList:
    def __init__(self, data=None):
        self.prev = self.next = None
        self.data = data

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, prv):
        self.__prev = prv if isinstance(prv, self.__class__) else None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, nxt):
        self.__next = nxt if isinstance(nxt, self.__class__) else None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def __walk_list(self, indx=math.inf):
        i = 0
        obj = self.head
        while obj and i < indx:
            obj = obj.next
            i += 1
        return i, obj

    def add_obj(self, obj):
        if not self.head:
            self.head = obj
        if self.tail:
            self.tail.next = obj
            obj.prev = self.tail
        self.tail = obj

    def remove_obj(self, indx):
        obj = self.__walk_list(indx)[1]
        if not obj:
            return
        if obj.prev:
            obj.prev.next = obj.next
        else:
            self.head = obj.next
        if obj.next:
            obj.next.prev = obj.prev
        else:
            self.tail = obj.prev

    def __len__(self):
        return self.__walk_list()[0]

    def __call__(self, indx, *args, **kwargs):
        obj = self.__walk_list(indx)[1]
        return obj.data if obj else None

    def get_data(self):
        obj = self.head
        res_lst = []
        while obj:
            res_lst.append(obj.data)
            obj = obj.next
        return res_lst or None


linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))
print(linked_lst.get_data())

n = len(linked_lst)  # n = 3
s = linked_lst(2) # s = Balakirev
print(n, s)

l1 = LinkedList()
print(len(l1))
l1.remove_obj(0)
print(l1(2))

# Variant 0
# def __walk_list(self, indx=math.inf):
#     i = 0
#     obj = self.head
#     if obj:
#         while i < indx and obj.next:
#             obj = obj.next
#             i += 1
#         if indx != math.inf and i != indx:
#             raise AttributeError('Index out of range')
#     return i, obj


# Task 6
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value):
        self.__real = value

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        self.__img = value

    def __setattr__(self, key, value):
        if type(value) in (int, float):
            super().__setattr__(key, value)
        else:
            raise ValueError("Неверный тип данных.")

    def __abs__(self):
        return (self.real**2 + self.img**2)**0.5


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)

print(c_abs)


# Task 7
class RadiusVector:
    def __init__(self, *args):
        if len(args) == 1 and type(args[0]) == int and args[0] > 1:
            self.coords = [0] * args[0]
        else:
            self.coords = [x for x in args if self.check_coord(x)]

    @staticmethod
    def check_coord(value):
        return type(value) in (int, float)

    def set_coords(self, *args):
        args = list(filter(self.check_coord, args))
        for i in range(min(len(self.coords), len(args))):
            self.coords[i] = args[i]

    def get_coords(self):
        return tuple(self.coords)

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        return sum(x**2 for x in self.coords)**0.5


r = RadiusVector()
print(r.__dict__)
vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
a, b, c = vector3D.get_coords()
print(a, b, c)
vector3D.set_coords(3, -5.6, 8, 10, 11)  # ошибки быть не должно, последние две координаты игнорируются
print(vector3D.__dict__)
vector3D.set_coords(1, 2)  # ошибки быть не должно, меняются только первые две координаты
print(vector3D.__dict__)
res_len = len(vector3D) # res_len = 3
res_abs = abs(vector3D)
print(res_len, res_abs)


# Task 8
class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hr = hours
        self.mn = minutes
        self.sec = seconds

    def get_time(self):
        return self.hr * 3600 + self.mn * 60 + self.sec


class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self):
        time_diff = len(self)
        hr = time_diff // 3600
        mn = time_diff % 3600 // 60
        sec = time_diff % 3600 % 60
        return f'{hr:02}: {mn:02}: {sec:02}'

    def __len__(self):
        res = self.clock1.get_time() - self.clock2.get_time()
        return res if res > 0 else 0


dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt) # 01: 30: 00
len_dt = len(dt) # 5400
print(len_dt)

dt1 = DeltaClock(Clock(0, 45, 0), Clock(1, 15, 0))
print(dt1) # 01: 30: 00
len_dt1 = len(dt1) # 5400
print(len_dt1)

# Variant 0
# class DeltaClock:
#     def __init__(self, clock1, clock2):
#         self.clock1 = clock1
#         self.clock2 = clock2
#
#     def __str__(self):
#         cl1, cl2 = self.clock1, self.clock2
#         return f'{self.subtr(cl1.hr, cl2.hr):02}: {self.subtr(cl1.mn, cl2.mn):02}: {self.subtr(cl1.sec, cl2.sec):02}'
#
#     def __len__(self):
#         return self.subtr(self.clock1.get_time(), self.clock2.get_time())
#
#     @staticmethod
#     def subtr(value1, value2):
#         res = value1 - value2
#         return res if res > 0 else 0


# Task 9
class Ingredient:
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f'{self.name}: {self.volume}, {self.measure}'


class Recipe:
    def __init__(self, *args):
        self._ing_list = list(args)

    def add_ingredient(self, ing):
        self._ing_list.append(ing)

    def remove_ingredient(self, ing):
        self._ing_list.remove(ing)

    def get_ingredients(self):
        return tuple(self._ing_list)

    def __len__(self):
        return len(self._ing_list)


recipe = Recipe()
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
ings = recipe.get_ingredients()
n = len(recipe) # n = 3
print(ings)
print(n)


# Task 10
class PolyLine:
    def __init__(self, *args):
        self.__coords = list(args)

    def add_coord(self, x, y):
        self.__coords.append((x, y),)

    def remove_coord(self, indx):
        self.__coords.pop(indx)

    def get_coords(self):
        return self.__coords


poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
print(poly.__dict__)
poly.add_coord(10, 20)
poly.remove_coord(0)
print(poly.get_coords())

