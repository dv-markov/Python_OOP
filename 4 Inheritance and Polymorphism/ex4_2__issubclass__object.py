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
