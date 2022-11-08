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


class Callback:
    def __init__(self, path, route_cls):
        self.path = path
        self.route_cls = route_cls

    def __call__(self, func):
        self.route_cls.add_callback(self.path, func)


@Callback('/', Router)
def index():
    return '<h1>Главная</h1>'


route = Router.get('/')
if route:
    ret = route()
    print(ret)
