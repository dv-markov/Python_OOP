# 4.3 Наследование. Функция super() и делегирование

# Расширение
class Geom:
    name = 'Geom'


class Line1(Geom):
    # расширение базового класса (extension)
    def draw(self):
        print("Рисование линии")


# Переопределение
class Geom:
    name = 'Geom'

    def draw(self):
        print("Рисование линии")


class Line2(Geom):
    # переопределение метода базового класса (overriding)
    def draw(self):
        print("Рисование линии")


# Наследование методов из базовых классов
class Geom:
    name = 'Geom'

    def __init__(self):
        print("Инициализатор Geom")


class Line(Geom):
    def draw(self):
        print("Рисование линии")


l1 = Line()
# при создании объекта класса Line, сначала вызывается метод __call__ - из метакласса type
# он содержит вызовы магических методов __new__ и __init__
# если __new__ не определен в Line и Geom, то он вызывается из класса object
# далее, метод __init__ ищется в классе Line, и если он там не определен, то в классе Geom


# super()
class Geom:
    name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f"Инициализатор Geom для {self.__class__}")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    def draw(self):
        print("Рисование линии")


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        # инициализатор базового класса стоит вызывать в самую первую очередь
        # вызов метода базового класса через метод супер называется делегированием
        super().__init__(x1, y1, x2, y2)
        print("инициализатор Rect")
        self.fill = fill

    def draw(self):
        print("Рисование прямоугольника")


l = Line(0, 0, 10, 20)
print(l.__dict__)

r = Rect(10, 10, 100, 200)
print(r.__dict__)

# super() - по сути это не функция, это класс, который создает объект-посредник,
# и он сам уже подставляет нужный self для родительских классов

# при вызове, super() будет ссылаться на первый базовый класс,
# в соответствии с алгоритмом MRO (см. коллекцию __mro__ у класса)


print("""
Задачи
""")


# Task 3
class Book:
    def __init__(self, title, author, pages, year):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year


class DigitBook(Book):
    def __init__(self, title, author, pages, year, size, frm):
        super().__init__(title, author, pages, year)
        self.size = size
        self.frm = frm


# Task 4
class Thing:
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight


class ArtObject(Thing):
    def __init__(self, name, weight, author, date):
        super().__init__(name, weight)
        self.author = author
        self.date = date


class Computer(Thing):
    def __init__(self, name, weight, memory, cpu):
        super().__init__(name, weight)
        self.memory = memory
        self.cpu = cpu


class Auto(Thing):
    def __init__(self, name, weight, dims):
        super().__init__(name, weight)
        self.dims = dims


class Mercedes(Auto):
    def __init__(self, name, weight, dims, model, old):
        super().__init__(name, weight, dims)
        self.model = model
        self.old = old


class Toyota(Auto):
    def __init__(self, name, weight, dims, model, wheel):
        super().__init__(name, weight, dims)
        self.model = model
        self.wheel = wheel


t = Toyota('Corolla-1', 2500, (100, 200, 100), 'Corolla', True)
print(t.__dict__)

# Variant 2
# class Thing:
#     arg = ['name', 'weight']
#
#     def __init__(self, *args):
#         [setattr(self, *x) for x in zip(self.arg, args)]
#
#
# class ArtObject(Thing):
#     arg = ['name', 'weight', 'author', 'date']
#
#
# class Computer(Thing):
#     arg = ['name', 'weight', 'memory', 'CPU']
#
#
# class Auto(Thing):
#     arg = ['name', 'weight', 'dims']
#
#
# class Mercedes(Auto):
#     arg = ['name', 'weight', 'dims', 'model', 'old']
#
#
# class Toyota(Auto):
#     arg = ['name', 'weight', 'dims', 'model', 'wheel']


# Variant 3
# class Thing:
#     _name_core = ("name", "weight")
#     _name_add = ()
#
#     def __init__(self, *args, **kwargs):
#         if kwargs:
#             self.__dict__.update(kwargs)
#         if args:
#             self.__dict__.update(zip((self._name_core + self._name_add), args))
#
#
# class ArtObject(Thing):
#     _name_add = ('author', 'date')
#
#
# class Computer(Thing):
#     _name_add = ('memory', 'CPU')
#
#
# class Auto(Thing):
#     _name_add = ('dims', )
#
#
# class Mercedes(Auto):
#     _name_add = ('dims', 'model', 'old')
#
#
# class Toyota(Auto):
#     _name_add = ('dims', 'model', 'wheel')


# Task 5
class SellItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class House(SellItem):
    def __init__(self, name, price, material, square):
        super().__init__(name, price)
        self.material = material
        self.square = square


class Flat(SellItem):
    def __init__(self, name, price, size, rooms):
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms


class Land(SellItem):
    def __init__(self, name, price, square):
        super().__init__(name, price)
        self.square = square


class Agency:
    def __init__(self, name):
        self.name = name
        self.obj_list = []

    def add_object(self, obj):
        if isinstance(obj, SellItem):
            self.obj_list.append(obj)

    def remove_object(self, obj):
        if obj in self.obj_list:
            self.obj_list.remove(obj)

    def get_objects(self):
        return self.obj_list


ag = Agency("Рога и копыта")
flat1 = Flat("квартира, 3к", 10000000, 121.5, 3)
ag.add_object(flat1)
ag.add_object(Flat("квартира, 2к", 8000000, 74.5, 2))
ag.add_object(Flat("квартира, 1к", 4000000, 54, 1))
ag.add_object(House("дом, кирпичный", price=35000000, material="кирпич", square=186.5))
ag.add_object(Land("участок под застройку", 3000000, 6.74))
ag.remove_object(flat1)

for obj in ag.get_objects():
    print(obj.name)

lst_houses = [x for x in ag.get_objects() if isinstance(x, House)] # выделение списка домов
print(lst_houses, *(x.name for x in lst_houses))


# Task 6
class Router:
    app = {}

    @classmethod
    def get(cls, path):
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path, func):
        cls.app[path] = func


# Декоратор на уровне класса
class Callback:
    def __init__(self, path, route_cls):
        self.path = path
        self.route_cls = route_cls

    def __call__(self, func):
        self.route_cls.add_callback(self.path, func)


# Здесь передается ссылка на сам класс Router.
# Когда мы вызываем класс, как декоратор, создается экземпляр этого класса, вызывается инициализатор.
# При декорировании функции (применении класса-декоратора к функции),
# после вызова инициализатора, автоматически происходит вызов метода call из класса-декоратора,
# аргумент - декорируемая функция
# Декоратор фактически будет делать то, что прописано в методе call
@Callback('/', Router)
def index():
    return '<h1>Главная</h1>'


route = Router.get('/')
if route:
    ret = route()
    print(ret)


# Task 7
# функция-декоратор для методов класса
# вызывается только для объектов "callable", то есть функций и методов
def integer_params_decorated(v):
    def wrapper(*args):
        if not all(map(lambda x: isinstance(x, int) or isinstance(x, Vector), args)):
            raise TypeError("аргументы должны быть целыми числами")
        return v(*args)

    return wrapper


def integer_params(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))

    return cls


@integer_params
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

    def set_coords(self, *coords, reverse=False):
        c = list(coords)
        self.__coords = c if not reverse else c[::-1]


vector = Vector(1, 2)
vector[0] = 500
print(vector[0], vector[1])
print(vector.__dict__)
print(Vector.__dict__)
# vector[1] = 20.4 # TypeError


# Variant 2 - Balakirev
# def integer_params_decorated(func):
#     def wrapper(self, *args, **kwargs):
#         if not all(type(x) == int for x in args):
#             raise TypeError("аргументы должны быть целыми числами")
#         if not all(type(x) == int for x in kwargs.values()):
#             raise TypeError("аргументы должны быть целыми числами")
#         return func(*args)
#     return wrapper


# Task 8
class SoftList(list):
    def __getitem__(self, item):
        if item > len(self) - 1 or item < -len(self):
            return False
        return super().__getitem__(item)


sl = SoftList("python")
print(sl[0])  # 'p'
print(sl[-1])  # 'n'
print(sl[6])  # False
print(sl[-7])  # False


# Task 9
from string import digits


class StringDigit(str):
    def __init__(self, string):
        self.__check_is_digits(string)

    @staticmethod
    def __check_is_digits(string):
        if not set(string).issubset(digits):
            raise ValueError('В строке должны быть только цифры')

    def __add__(self, other):
        self.__check_is_digits(other)
        return self.__class__(super().__add__(other))

    def __radd__(self, other):
        # self.__check_is_digits(other)
        # return self.__class__(super().__add__(other + self))
        other = self.__class__(other)
        return other + self


class StringDigit(str):
    def __init__(self, string):
        self.__check_is_digits(string)

    @staticmethod
    def __check_is_digits(string):
        if not set(string).issubset(digits):
            raise ValueError('В строке должны быть только цифры')

    def __add__(self, other):
        self.__check_is_digits(other)
        return self.__class__(super().__add__(other))

    def __radd__(self, other):
        return self.__class__(other) + self


sd = StringDigit('123')
print(sd, type(sd))
sd = sd + '456'
print(sd, type(sd))
sd = '789' + sd
print(sd, type(sd))
# sd1 = StringDigit('ads')


# Task 10
class ItemAttrs:
    def __getitem__(self, item):
        attrs_lst = list(self.__dict__)
        return getattr(self, attrs_lst[item])

    def __setitem__(self, key, value):
        attrs_lst = list(self.__dict__)
        setattr(self, attrs_lst[key], value)


class Point(ItemAttrs):
    def __init__(self, x, y):
        self.x = x
        self.y = y


pt = Point(1, 2.5)
x = pt[0]
y = pt[1]
print(x, y)
pt[0] = 10
print(pt.__dict__)

