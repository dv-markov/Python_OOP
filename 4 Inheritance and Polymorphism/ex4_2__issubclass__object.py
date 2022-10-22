# 4.2 Функция issubclass(). Наследование от встроенных типов

class Geom:
    # class Geom(object): - аналогичный функционал, все классы по умолчанию наследуются от класса object
    pass


class Line(Geom):
    # дочерний класс наследуется только от класса Geom, но не от класса object напрямую
    pass


print(Geom.__name__)
g = Geom()
print(g)
l = Line()
print(l.__class__)
# при поиске доступных функций и аттрибутов классы проходят по цепочке наследования

# мы можем определять, является ли тот иной класс подклассом другого класса
# функция issubclass
print(issubclass(Line, Geom))
print(issubclass(Geom, Line))
# эта функция работает только с классами, но не с экземплярами

# с экземплярами (объектами) классов работает функция isinstance
# print(issubclass(l, Geom)) - выдаст ошибку
print(isinstance(l, object))

# все стандартные типы данных являются классами
print(issubclass(int, object))
print(issubclass(list, object))


# можно расширить стандартные типы данных
class Vector(list):
    def __str__(self):
        return " ".join(map(str, self))


v = Vector([1, 2, 3])
print(v)
print(type(v))

# стандартные типы данных редко расширяют с помощью пользовательских классов

print("""
Задачи""")


# Task 3
class ListInteger(list):
    @staticmethod
    def __check_int(*args):
        if any(type(x) != int for x in args):
            raise TypeError('можно передавать только целочисленные значения')

    def __init__(self, args):
        self.__check_int(*args)
        super().__init__(args)

    def __setitem__(self, key, value):
        self.__check_int(value)
        super().__setitem__(key, value)

    def append(self, obj) -> None:
        self.__check_int(obj)
        super().append(obj)


s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
# s[0] = 10.5 # TypeError


# Task 4
class Thing:
    def __init__(self, name: str, price: float, weight: float):
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self):
        return hash((self.name, self.price, self.weight))


class DictShop(dict):
    def __init__(self, dictionary=None):
        if not dictionary:
            dictionary = dict()
        if not isinstance(dictionary, dict):
            raise TypeError('аргумент должен быть словарем')
        for key in dictionary:
            self.__check_key(key)
        # super().__init__(**dictionary)
        # super().__init__(((k, v) for k, v in dictionary.items()))
        super().__init__(dictionary)

    def __setitem__(self, key, value):
        self.__check_key(key)
        super().__setitem__(key, value)

    # def __getitem__(self, item):
    #     self.__check_key(item)
    #     super().__getitem__(item)
    #
    # def __delitem__(self, key):
    #     self.__check_key(key)
    #     super().__delitem__(key)

    @staticmethod
    def __check_key(key):
        if not isinstance(key, Thing):
            raise TypeError('ключами могут быть только объекты класса Thing')


thing = Thing('hello', 123, 321)
d = {}
d[thing] = thing
print(thing, thing.__dict__)
print(d)

th_1 = Thing('Лыжи', 11000, 1978.55)
th_2 = Thing('Книга', 1500, 256)
dict_things = DictShop()
dict_things[th_1] = th_1
dict_things[th_2] = th_2

for x in dict_things:
    print(x.name)

dic1 = {th_1: th_1, th_2: th_2}
dic2 = DictShop(dic1)
print(dic2)
for y in dic2:
    print(y.name)

# dict_things[1] = th_1  # исключение TypeError

dic = dict(k=123)
print(dic)


# Task 5
class Protists:
    pass


class Plants(Protists):
    pass


class Animals(Protists):
    pass


class Mosses(Plants):
    pass


class Flowering(Plants):
    pass


class Worms(Animals):
    pass


class Mammals(Animals):
    pass


class Human(Mammals):
    pass


class Monkeys(Mammals):
    pass


class PropertyInterface:
    def __init__(self, name, weight, old):
        self.name = name
        self.weight = weight
        self.old = old


class Monkey(Monkeys, PropertyInterface):
    pass


class Person(Human, PropertyInterface):
    pass


class Flower(Flowering, PropertyInterface):
    pass


class Worm(Worms, PropertyInterface):
    pass


lst_objs = [Monkey("мартышка", 30.4, 7),
            Monkey("шимпанзе", 24.6, 8),
            Person("Балакирев", 88, 34),
            Person("Верховный жрец", 67.5, 45),
            Flower("Тюльпан", 0.2, 1),
            Flower("Роза", 0.1, 2),
            Worm("червь", 0.01, 1),
            Worm("червь 2", 0.02, 1)]

lst_animals = [x for x in lst_objs if isinstance(x, Animals)]
lst_plants = [x for x in lst_objs if isinstance(x, Plants)]
lst_mammals = [x for x in lst_objs if isinstance(x, Mammals)]

for y in lst_animals:
    print(y.name)
print()

for y in lst_plants:
    print(y.name)
print()

for y in lst_mammals:
    print(y.name)
print()


# Task 6
class Tuple(tuple):
    def __add__(self, other):
        return Tuple(super().__add__(tuple(other)))


iter_obj = [1, 2, 3]
t1 = Tuple(iter_obj)
print(t1)
t2 = t1 + iter_obj  # создается новый объект класса Tuple с новым (соединенным) набором данных
print(t2.__class__, t2)
t3 = t2 + {4, 5, 6}
print(t3)
t4 = Tuple({7, 8, 9})
print(t4)

t = Tuple([1, 2, 3])
t = t + "Python"
print(t)   # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
t = (t + "Python") + "ООП"
print(t)


# Task 7
class VideoItem:
    def __init__(self, title: str, descr: str, path: str):
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()


class VideoRating:
    def __init__(self):
        self.rating = 0

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if type(value) != int or not (0 <= value <= 5):
            raise ValueError('неверное присваиваемое значение')
        self.__rating = value


v = VideoItem('Курс по Python ООП', 'Подробный курс по Python ООР', 'D:/videos/python_oop.mp4')
print(v.rating.rating) # 0
v.rating.rating = 5
print(v.rating.rating) # 5
title = v.title
descr = v.descr
# v.rating.rating = 6  # ValueError


# Task 9 - итератор по атрибутам
# Version 1 - my
# class IteratorAttrs:
#     def __init__(self):
#         self.attrs = tuple(self.__dict__)
#         self.ln_attrs = len(self.attrs)
#
#     def __iter__(self):
#         self.indx = -1
#         return self
#
#     def __next__(self):
#         if self.indx < self.ln_attrs - 1:
#             self.indx += 1
#             v = self.attrs[self.indx]
#             return v, getattr(self, v)
#         raise StopIteration


# Version 2 - my
# class IteratorAttrs:
#     def __init__(self):
#         self.attrs = tuple(self.__dict__)
#
#     def __iter__(self):
#         for k in self.attrs:
#             yield k, getattr(self, k)


# Version 3 - my refined
class IteratorAttrs:
    def __iter__(self):
        for attr in self.__dict__.items():
            yield attr


class SmartPhone(IteratorAttrs):
    def __init__(self, model: str, size: tuple, memory: int):
        self.model = model
        self.size = size
        self.memory = memory
        # super().__init__()


phone = SmartPhone('iPhone', (100, 200), 128)
for attr, value in phone:
    print(attr, value)

for attr, value in phone:
    print(attr, value)

for x in phone:
    print(x)


# Version 3 - Vladislav Smolov
# class IteratorAttrs:
#     def __iter__(self):
#         return iter(self.__dict__.items())

# Version 4 - Дмитрий Суднищиков
# class IteratorAttrs:
#     def __iter__(self):
#         yield from self.__dict__.items()

# Version 5 - YouTube - Юрий Качанов
# class IteratorAttrs:
#     def __iter__(self):
#         self.step = -1
#         return self
#
#     def __next__(self):
#         self.step += 1
#         if self.step < len(self.__dict__) - 1:
#             return list(self.__dict__.items())[self.step]
#         raise StopIteration

