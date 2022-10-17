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


class DetailView(GenericView):
    def render_request(self, request, method):
        if method not in self.methods:
            raise TypeError('данный запрос не может быть выполнен')
        return getattr(self, method.lower())(request)

        # Balakilrev
        # f = getattr(self, method.lower(), False)
        # if f:
        #     return f(request)

    def get(self, request):
        if type(request) != dict:
            raise TypeError('request не является словарем')
        if 'url' not in request:
            raise TypeError('request не содержит обязательного ключа url')
        return f"url: {request['url']}"


dv = DetailView()
html = dv.render_request({'url': 'https://site.ru/home'}, 'GET')  # url: https://site.ru/home
print(html)


# Task 7
# здесь Singleton работает отдельно для базового класса и отдельно для каждого из дочерних
class Singleton:
    __instance = None
    __instance_base = None

    def __new__(cls, *args, **kwargs):
        if cls == Singleton:
            if cls.__instance_base is None:
                cls.__instance_base = super().__new__(cls)
            return cls.__instance_base

        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


# первый вариант
class Game(Singleton):
    def __init__(self, name):
        if 'name' not in self.__dict__:
            self.name = name


# второй вариант
class Game2(Singleton):
    def __init__(self, name):
        if not hasattr(self, 'name'):
            self.name = name


a0 = Singleton()
a1 = Game(1)
a2 = Game(2)
a3 = Game(3)
print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)

g1 = Game2('one')
g2 = Game2('two')
print(g1.__dict__)
print(g2.__dict__)


# Task 8
class Validator:
    def _is_valid(self, data):
        return True

    def __call__(self, *args, **kwargs):
        if not self._is_valid(args[0]):
            raise ValueError('данные не прошли валидацию')


class IntegerValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        return type(data) == int and self.min_value <= data <= self.max_value


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        return type(data) == float and self.min_value <= data <= self.max_value


v = Validator()
print(v(123))

integer_validator = IntegerValidator(-10, 10)
float_validator = FloatValidator(-1, 1)
res1 = integer_validator(10)  # исключение не генерируется (проверка проходит)
# res2 = float_validator(10)  # исключение ValueError

# Variant 2
# class Validator:
#     def _is_valid(self, data):
#         return True
#
#     def __call__(self, data):
#         if self._is_valid(data):
#             return True
#         else:
#             raise ValueError('данные не прошли валидацию')
#
#
# class ExtValidator(Validator):
#     data_type = None
#
#     def __init__(self, min_value, max_value):
#         self.min_value = min_value
#         self.max_value = max_value
#
#     def _is_valid(self, data):
#         return type(data) == self.data_type \
#                and self.min_value <= data <= self.max_value
#
#
# class IntegerValidator(ExtValidator):
#     data_type = int
#
#
# class FloatValidator(ExtValidator):
#     data_type = float


# Task 9
class Layer:
    def __init__(self):
        self.next_layer = None
        self.name = 'Layer'

    def __call__(self, *args, **kwargs):
        self.next_layer = args[0]
        return args[0]


class Input(Layer):
    def __init__(self, inputs: int):
        super().__init__()
        self.name = 'Input'
        self.inputs = inputs


class Dense(Layer):
    def __init__(self, inputs: int, outputs: int, activation: str):
        super().__init__()
        self.name = 'Dense'
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation


class NetworkIterator:
    def __init__(self, nw):
        self.nw = nw

    def __iter__(self):
        n = self.nw
        while n:
            yield n
            n = n.next_layer

# Variant 2
# Определение имени по имени класса, прописывается в базовом классе
# self.name = self._class__.__name__


print()
first_layer = Layer()
next_layer = first_layer(Layer())
next_layer = next_layer(Layer())
for x in NetworkIterator(first_layer):
    print(x.name)

print()
network = Input(128)
layer = network(Dense(network.inputs, 1024, 'linear'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))
for x in NetworkIterator(network):
    print(x.name)


# Task 10
from operator import add, sub


class Vector:
    def __init__(self, *coords):
        self.coords = coords

    def __eq__(self, other):
        return len(self.coords) == len(other.coords)

    def _check_len(self, other):
        if self != other:
            raise TypeError('размерности векторов не совпадают')

    def _operate(self, other, op):
        self._check_len(other)
        return __class__(*(op(x, y) for x, y in zip(self.coords, other.coords)))

    def __add__(self, other):
        return self._operate(other, add)

    def __sub__(self, other):
        return self._operate(other, sub)

    def get_coords(self):
        return self.coords


class VectorInt(Vector):
    def __init__(self, *coords):
        if not self.__check_int(coords):
            raise ValueError('координаты должны быть целыми числами')
        super().__init__(*coords)

    @staticmethod
    def __check_int(coords):
        return all(type(x) == int for x in coords)

    def _operate(self, other, op):
        self._check_len(other)
        return self.__class__(*(op(x, y) for x, y in zip(self.coords, other.coords)))

    def __add__(self, other):
        if self.__check_int(other.coords):
            return self._operate(other, add)
        return super()._operate(other, add)

    def __sub__(self, other):
        if self.__check_int(other.coords):
            return self._operate(other, sub)
        return super()._operate(other, sub)


v = Vector(1, 2, 3)
print(v.__dict__)

v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
v = v1 + v2  # формируется новый вектор (объект класса Vector) с соответствующими координатами
print(v.coords)
v = v1 - v2  # формируется новый вектор (объект класса Vector) с соответствующими координатами
print(v.coords)

v3 = VectorInt(1, 2, 3, 4)
print(v3.__dict__)
# v = VectorInt(1, 0.2, 3, 4) # ошибка: генерируется исключение
v4 = Vector(8, 7, 6, 5)
print(v4.__dict__)
v = v3 + v4
print(type(v), v.coords)
v = v3 - v4
print(type(v), v.coords)

# Variant 2
# from operator import add, sub
#
# class Vector:
#     type_coords = (int, float)
#     error_message = 'числами'
#
#     def __init__(self, *args):
#         self.__check_data(args)
#         self.coords = [*args]
#
#     def get_coords(self):
#         return tuple(self.coords)
#
#     def __check_data(self, lst):
#         if not all(type(x) in self.type_coords for x in lst):
#             raise ValueError(f'координаты должны быть {self.error_message}')
#
#     def __len__(self):
#         return len(self.coords)
#
#     def __check_vector(self, other):
#         if len(self) != len(other):
#             raise TypeError('размерности векторов не совпадают')
#
#     def __make_calc(self, other, op) -> list:
#         self.__check_vector(other)
#         return [op(*el) for el in zip(self.coords, other.coords)]
#
#     @staticmethod
#     def make_vector(lst):
#         try:
#             return VectorInt(*lst)
#         except ValueError:
#             return Vector(*lst)
#
#     def __add__(self, other):
#         res = self.__make_calc(other, add)
#         return self.make_vector(res)
#
#     def __sub__(self, other):
#         res = self.__make_calc(other, sub)
#         return self.make_vector(res)
#
#
# class VectorInt(Vector):
#     type_coords = (int, )
#     error_message = 'целыми числами'


# Variant 3


class Vector:
    def __init__(self, *coords):
        self.coords = coords

    def __eq__(self, other):
        return len(self.coords) == len(other.coords)

    def _check_len(self, other):
        if self != other:
            raise TypeError('размерности векторов не совпадают')

    def _operate(self, other, op, int_values=False):
        self._check_len(other)
        class_level = self.__class__ if int_values else __class__
        return class_level(*(op(x, y) for x, y in zip(self.coords, other.coords)))

    def __add__(self, other):
        return self._operate(other, add)

    def __sub__(self, other):
        return self._operate(other, sub)

    def get_coords(self):
        return self.coords


class VectorInt(Vector):
    def __init__(self, *coords):
        if not self.__check_int(coords):
            raise ValueError('координаты должны быть целыми числами')
        super().__init__(*coords)

    @staticmethod
    def __check_int(coords):
        return all(type(x) == int for x in coords)

    def __add__(self, other):
        if self.__check_int(other.coords):
            return self._operate(other, add, True)
        return self._operate(other, add)

    def __sub__(self, other):
        if self.__check_int(other.coords):
            return self._operate(other, sub, True)
        return self._operate(other, sub)


v = Vector(1, 2, 3)
print(v.__dict__)

v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
v = v1 + v2  # формируется новый вектор (объект класса Vector) с соответствующими координатами
print(v.coords)
v = v1 - v2  # формируется новый вектор (объект класса Vector) с соответствующими координатами
print(v.coords)

v3 = VectorInt(1, 2, 3, 4)
print(v3.__dict__)
# v = VectorInt(1, 0.2, 3, 4) # ошибка: генерируется исключение
v4 = Vector(8, 7, 6, 5.1)
print(v4.__dict__)
v = v3 + v4
print(type(v), v.coords)
v = v3 - v4
print(type(v), v.coords)