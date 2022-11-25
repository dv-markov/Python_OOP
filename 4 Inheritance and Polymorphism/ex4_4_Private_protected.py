# 4.4. Наследование. Атрибуты private и protected

# attribute - публичное свойство (public)
# _attribute - защищенное св-во (protected), доступны в текущем и во всех дочерних классах
# __attribute - приватное св-во (private), служит для обращения только внутри класса,
# private атрибуты не доступны в дочерних классах
import inspect


class Geom:
    name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f"Инициализатор Geom для {self.__class__}")
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    # метод сработает в базовом классе
    def get_coords(self):
        return self.__x1, self.__y1


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        self.__fill = fill

    # не сработает в дочернем классе
    # этот метод не найдет приватные атрибуты __x1 и __y1, т.к. они объявлены в базовом классе
    # def get_coords(self):
    #     return self.__x1, self.__y1


# Особенность поведения формирования приватных атрибутов в базовых классах
# Префикс добавляется в приватный атрибут из того класса, где этот атрибут прописан
r = Rect(0, 0, 10, 20)
print(r.__dict__)
print(r.get_coords())


# protected
class Geom:
    name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f"Инициализатор Geom для {self.__class__}")
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        self._fill = fill

    # сработает в дочернем классе
    def get_coords(self):
        return self._x1, self._y1


r = Rect(100, 100, 1010, 2020)
print(r.__dict__)
print(r.get_coords())
# не запрещает обращение извне, но использовать прямое внешнее обращение не рекомендуется
print(r._x1)

# похожим образом ведут себя атрибуты уровня класса
print(r.name)


# в private атрибут класса также нельзя обратиться из объекта дочернего класса
class Geom:
    __name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f"Инициализатор Geom для {self.__class__}")
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        # передача значения private атрибута в protected
        self._name = self.__name


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        self._fill = fill


r = Rect(99, 99, 888, 888)
print(r.__dict__)
# print(r.__name) #  не сработает
print(r._name)  # сработает


# аналогичные ограничения накладываются на работу с методами
class Geom:
    __name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f"Инициализатор Geom для {self.__class__}")
        self.__verify_coords(x1)
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

    # метод доступен только в текущем классе
    def __verify_coords(self, coord):
        return 0 <= coord < 100

    # метод доступен в текущем классе и в дочерних классах
    def _verify_coords(self, coord):
        return 0 <= coord < 100


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        # self.__verify_coords(x1) #  не сработает
        self._verify_coords(x1)  # сработает
        self._fill = fill


r = Rect(10, 10, 20, 20)
print(r.__dict__)

print("""
Задачи""")


# Task 5
class Animal:
    def __init__(self, name: str, kind: str, old: int):
        self.name = name
        self.kind = kind
        self.old = old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, value):
        self.__kind = value

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, value):
        self.__old = value


animals = """Васька; дворовый кот; 5
Рекс; немецкая овчарка; 8
Кеша; попугай; 3"""
animals = [Animal(*x.split("; ")) for x in animals.split("\n")]

for a in animals:
    print(a.name, a.kind, a.old)


# Variant 2 - с дескрипторами; Descriptor, property()
# class Property:
#     def __set_name__(self, owner, name):
#         self.name = f'_{owner.__name__}__{name}'
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return property()
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         setattr(instance, self.name, value)
#
#
# class Animal:
#     name = Property()
#     kind = Property()
#     old = Property()
#
#     def __init__(self, name, kind, old):
#         self.name = name
#         self.kind = kind
#         self.old = old


# Task 6
class Furniture:
    name: str

    def __init__(self, name: str, weight: float):
        self._name = name
        self._weight = weight

    @staticmethod
    def __verify_name(name):
        if not isinstance(name, str):
            raise TypeError('название должно быть строкой')

    @staticmethod
    def __verify_weight(weight):
        if not type(weight) in (int, float) or weight <= 0:
            raise TypeError('вес должен быть положительным числом')

    def __setattr__(self, key, value):
        # вариант с match, не работает на старых версия Python
        # match key:
        #     case '_name':
        #         self.__verify_name(value)
        #     case '_weight':
        #         self.__verify_weight(value)
        # вариант с getattr, работает всегда
        if key in ('_name', '_weight'):
            print(f'_{__class__.__name__}__verify{key}', value)
            # изучить до конца тему с аннотациями типов
            # print(inspect.get_annotations(self.__class__))
            # print(self.__annotations__)
            getattr(self, f'_{__class__.__name__}__verify{key}')(value)
        super().__setattr__(key, value)

    def get_attrs(self):
        return tuple(self.__dict__.values())


class Closet(Furniture):
    tp: bool

    def __init__(self, name, weight, tp: bool, doors: int):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors

        # и здесь про аннотации типов
        # self.__annotations__.update(super().__annotations__)
        print(self.__annotations__)
        print(super().__annotations__)
        self.__annotations__.update(super().__annotations__)
        print(self.__annotations__)


class Chair(Furniture):
    def __init__(self, name, weight, height: float):
        super().__init__(name, weight)
        self._height = height


class Table(Furniture):
    def __init__(self, name, weight, height: float, square: float):
        super().__init__(name, weight)
        self._height = height
        self._square = square


f = Furniture('table', 500)
print(f.__dict__)

cl = Closet('шкаф-купе', 342.56, True, 3)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)
print(tb.get_attrs())
print()

# Special Attributes
print(cl.__annotations__)
print(Closet.__mro__)
print(Closet.__base__)
print(Closet.__bases__)
print(Furniture.__subclasses__())


# Task 6
class Observer:
    def update(self, data):
        pass

    def __hash__(self):
        return hash(id(self))


class Subject:
    def __init__(self):
        self.__observers = {}
        self.__data = None

    def add_observer(self, observer):
        self.__observers[observer] = observer

    def remove_observer(self, observer):
        if observer in self.__observers:
            self.__observers.pop(observer)

    def __notify_observer(self):
        for ob in self.__observers:
            ob.update(self.__data)

    def change_data(self, data):
        self.__data = data
        self.__notify_observer()


class Data:
    def __init__(self, temp, press, wet):
        self.temp = temp  # температура
        self.press = press  # давление
        self.wet = wet  # влажность


class TemperatureView(Observer):
    def update(self, data):
        print(f"Текущая температура {data.temp}")


class PressureView(Observer):
    def update(self, data):
        print(f"Текущее давление {data.press}")


class WetView(Observer):
    def update(self, data):
        print(f"Текущая влажность {data.wet}")


subject = Subject()
tv = TemperatureView()
pr = PressureView()
wet = WetView()

subject.add_observer(tv)
subject.add_observer(pr)
subject.add_observer(wet)

subject.change_data(Data(23, 150, 83))
# выведет строчки:
# Текущая температура 23
# Текущее давление 150
# Текущая влажность 83
subject.remove_observer(wet)
subject.change_data(Data(24, 148, 80))


# выведет строчки:
# Текущая температура 24
# Текущее давление 148


# Variant 2 - через BaseView
# class BaseView(Observer):
#     msg = None
#     attr = None
#
#     def update(self, data):
#         attr = getattr(data, self.attr)
#         print(f'{self.msg} {attr}')
#
#
# class TemperatureView(BaseView):
#     msg = 'Текущая температура'
#     attr = 'temp'
#
#
# class PressureView(BaseView):
#     msg = 'Текущее давление'
#     attr = 'press'
#
#
# class WetView (BaseView):
#     msg = 'Текущая влажность'
#     attr = 'wet'


# Task 7
class Aircraft:
    def __init__(self, model, mass, speed, top):
        self._verify_str(model)
        self._verify_positive_number(mass, speed, top)
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top

    @staticmethod
    def _err():
        raise TypeError('неверный тип аргумента')

    def _verify_str(self, s):
        if not isinstance(s, str):
            self._err()

    def _verify_positive_number(self, *args):
        if not all(type(x) in (int, float) and x > 0 for x in args):
            self._err()

    def _verify_positive_int(self, i):
        if not isinstance(i, int) or i < 0:
            self._err()


class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self._verify_positive_int(chairs)
        self._chairs = chairs


class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self._verify_weapons(weapons)
        self._weapons = weapons

    def _verify_weapons(self, w):
        if not isinstance(w, dict):
            self._err()
        for k, v in w.items():
            self._verify_str(k)
            self._verify_positive_int(v)


planes = [
    PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
    PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
    WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
    WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})
]

for p in planes:
    print(p.__dict__)


# Variant 2 - Константин Мамонов
# class Aircraft:
#     def __init__(self, model, mass, speed, top):
#         self.chek(model, str)
#         self._model = model
#         [self.chek(i, (int, float)) for i in (mass, speed, top)]
#         self._mass = mass
#         self._speed = speed
#         self._top = top
#
#     @staticmethod
#     def chek(value, type_value):
#         if not isinstance(value, type_value):
#             raise TypeError('неверный тип аргумента')
#         if type(value) in (int, float) and value < 0:
#             raise TypeError('неверный тип аргумента')
#
#
# class PassengerAircraft(Aircraft):
#     def __init__(self, model, mass, speed, top, chairs):
#         super().__init__(model, mass, speed, top)
#         self.chek(chairs, int)
#         self._chairs = chairs
#
#
# class WarPlane(Aircraft):
#     def __init__(self, model, mass, speed, top, weapons):
#         super().__init__(model, mass, speed, top)
#         self.chek(weapons, dict)
#         self._weapons = weapons


# Task 9
# def class_log(cls):
#     # methods = {k: v for k, v in cls.__dict__ if callable(v)}
#     # for k in methods
#     #     pass
#     vector_log.append(k for k, v in cls.__dict__ if callable(v))
#     return cls

# def class_log_decorated(func):
#     def wrapper(*args):
#         return func(*args)
#     return wrapper
#
#
# def class_log(cls):
#     methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
#     for k, v in methods.items():
#         print(k)
#         setattr(cls, k, class_log_decorated(v))
#     return cls


def method_decorator(func_name, func, lst):
    def wrapper(*args):
        lst.append(func_name)
        return func(*args)
    return wrapper


def class_log(lst):
    def class_decorator(cls):
        # lst.extend([k for k, v in cls.__dict__.items() if callable(v)])
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, method_decorator(k, v, lst))
        return cls
    return class_decorator


vector_log = []   # наименование (vector_log) в программе не менять!


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value


print(Vector.__dict__)
vec = Vector(1, 2, 3)
vec[0] = 10
print(vector_log)
