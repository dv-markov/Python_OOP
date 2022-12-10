# 4.7 Коллекция __slots__
# Ограничивает доступные атрибуты для класса
# Наследуется только, если в дочернем классе прописан __slots__

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


pt = Point(1, 2)
print(pt.__dict__)
pt.y = 10
pt.z = 20
print(pt.__dict__)


class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


pt2 = Point2D(10, 20)

# в объекте с коллекцией __slots__ отсутствует коллекция __dict__
# print(pt2.__dict__)

# новые локальные свойства с коллекцией __slots__ создавать нельзя
# pt2.z = 800

print(pt2.__slots__)
print(pt2.__dir__())
del pt2.x
pt2.x = 5
print(pt2.x, pt2.y)

# Коллекция __slots__ накладывает ограничения на создание локальных свойств объекта (экземпляра класса),
# Но не накладывает ограничений на аттрибуты самого класса


class Point2DM:
    __slots__ = ('x', 'y')
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y


print(Point2DM.MAX_COORD)
pt2m = Point2DM(1, 0)
print(pt2m.MAX_COORD)


# Применение __slots__ уменьшает объем потребляемой памяти для экземпляров класса
# и ускоряет работу с их локальными свойствами
print('Сравнение занимаемой памяти:')
print(pt.__sizeof__())
print(pt.__sizeof__() + pt.__dict__.__sizeof__())
print(pt2.__sizeof__())


from timeit import timeit


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


p = Point(1, 2)
p2 = Point2D(1, 2)

t1 = timeit(p.calc)
t2 = timeit(p2.calc)

print(t1, t2)

# Особенности работы с коллекцией __slots__
# - ограничение создаваемых локальных свойств
# - уменьшение занимаемой памяти
# - ускорение работы с локальными свойствами


# ------------ работа __slots__ со свойствами property ------------


class Point2D:
    __slots__ = ('x', 'y', '__length')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__length = (x * x + y * y) * 0.5

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value


pt = Point2D(1, 2)
print(pt.length)
pt.length = 42
print(pt.length)


# ------------ работа __slots__ с наследованием ------------

class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


# Если в дочернем классе коллекция __slots__ не объявлена, она не наследуется от базового класса
class Point3D(Point2D):
    pass


pt = Point3D(1, 2)
pt.z = 3
print(pt.z)


# Если объявлена, даже пустая, тогда наследуется
class Point3D(Point2D):
    __slots__ = ()


# выдаст ошибку
pt = Point3D(1, 2)
# pt.z = 3
# print(pt.z)


# Если в дочернем классе объявить __slots__ с другим аттрибутом, он добавится к уже существующим из базового класса
class Point3D(Point2D):
    __slots__ = 'z',


# не выдаст ошибку
pt = Point3D(1, 2)
pt.z = 3
print(pt.z)


print("""
Задачи""")


# Task 4
class Person:
    __slots__ = ('_fio', '_old', '_job')

    def __init__(self, fio, old, job):
        self._fio = fio
        self._old = old
        self._job = job


txt = """Суворов, 52, полководец
Рахманинов, 50, пианист, композитор
Балакирев, 34, программист и преподаватель
Пушкин, 32, поэт и писатель"""

lst1 = [x.split(', ', maxsplit=2) for x in txt.splitlines()]
print(lst1)
persons = [Person(*x) for x in lst1]

for x in lst1:
    print(x)

for p in persons:
    print(p._fio, p._old, p._job)


# Task 5
class Planet:
    def __init__(self, name, diametr, period_solar, period):
        self._name = name
        self._diametr = diametr
        self._period_solar = period_solar
        self._period = period


class SolarSystem:
    __slots__ = ('_mercury', '_venus', '_earth', '_mars', '_jupiter', '_saturn', '_uranus', '_neptune')
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self._mercury = Planet('Меркурий', 4878, 87.97, 1407.5)
        self._venus = Planet('Венера', 12104, 224.7, 5832.45)
        self._earth = Planet('Земля', 12756, 365.3, 23.93)
        self._mars = Planet('Марс', 6794, 687, 24.62)
        self._jupiter = Planet('Юпитер', 142800, 4330, 9.9)
        self._saturn = Planet('Сатурн', 120660, 10753, 10.63)
        self._uranus = Planet('Уран', 51118, 30665, 17.2)
        self._neptune = Planet('Нептун', 49528, 60150, 16.1)


s_system = SolarSystem()
s_system2 = SolarSystem()
print(id(s_system), id(s_system2))


# Task 6
