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
