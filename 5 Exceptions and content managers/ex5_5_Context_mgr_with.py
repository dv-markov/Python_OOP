# 5.5 Менеджеры контекстов. Оператор with

# Вариант с классическим try/except
fp = None
try:
    fp = open("myfile.txt")
    for t in fp:
        print(t)
except Exception as e:
    print(e)
finally:
    if fp is not None:
        fp.close()

# Вариант с менеджером контекста with
try:
    with open("myfile.txt") as fp:
        for t in fp:
            print(t)
except Exception as e:
    print(e)

# Менеджер контекста with - это класс
# В при вызове срабатывает два метода:
# __enter__() - в момент создания объекта менеджера контекста
# __exit__() - в момент завершения работы менеджера контекста
# или возникновения исключения (подобно блоку finally)
# as - опциональная часть конструкции


# пример - свой класс
class DefendedVector:
    def __init__(self, v):
        self.__v = v

    def __enter__(self):
        self.__temp = self.__v[:]
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v[:] = self.__temp

        return False


v1 = [1, 2, 3]
v2 = [2, 3]
# v2 = [2, 3, 4]

try:
    with DefendedVector(v1) as dv:
        for i, a in enumerate(dv):
            dv[i] += v2[i]
except:
    print("Ошибка")

print(v1)


print("""
Задачи""")


# Task 3
class PrimaryKey:
    def __enter__(self):
        print("вход")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        return True


with PrimaryKey() as pk:
    raise ValueError


# Task 4
class ConnectionError(Exception):
    def __str__(self):
        return 'Ошибка соединения'


class DatabaseConnection:
    def __init__(self):
        self._fl_connection_open = False

    def __enter__(self):
        return self

    def connect(self, login, password):
        self._fl_connection_open = True
        raise ConnectionError

    def close(self):
        self._fl_connection_open = False

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


try:
    with DatabaseConnection() as conn:
        conn.connect(123, 321)
except Exception as e:
    print(e)


# Task 5
class Box:
    def __init__(self, name, max_weight, things=None):
        self._name = name
        self._max_weight = max_weight
        self._things = things or []

    def add_thing(self, obj):
        *_, w = obj
        if w + self.__get_current_weight() > self._max_weight:
            raise ValueError('превышен суммарный вес вещей')
        self._things.append(obj)

    def __get_current_weight(self):
        return sum(w for *_, w in self._things)

    def get_box_values(self):
        return self._name, self._max_weight, self._things[:]


class BoxDefender:
    def __init__(self, box):
        if not isinstance(box, Box):
            raise TypeError('необходим объект класса box')
        self.box = box

    def __enter__(self):
        self.temp_box = Box(*self.box.get_box_values())
        return self.temp_box

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:  # and not exc_tb:
            self.box._things[:] = self.temp_box._things
        return False


b = Box('ящик', 500)
b.add_thing(('топор', 10))
b.add_thing(('примус', 15))
print(b.__dict__)


box = Box("сундук", 1000)
box.add_thing(("спички", 46.6))
box.add_thing(("рубашка", 134))
print(box, box.__dict__)

try:
    with BoxDefender(box) as b:
        print(b, b.__dict__)
        b.add_thing(("зонт", 346.6))
        b.add_thing(("шина", 500))
except Exception as e:
    print(e)

print(box, box.__dict__)


# Variant 2 - Fedor Kuzmenko
# class BoxDefender:
#     def __init__(self, box):
#         self.box = box
#         self.things = box._things.copy()
#
#     def __enter__(self):
#         return self.box
#
#     def __exit__(self, e_type, e_obj, trace):
#         if e_type:
#             self.box._things[:] = self.things
#         return False


# Variant 3 - Balakirev
class Box:
    def __init__(self, name, max_weight):
        self._name = name
        self._max_weight = max_weight
        self._things = []

    @property
    def things(self):
        return self._things

    @things.setter
    def things(self, lst):
        self._things = lst

    @property
    def total_weight(self):
        return sum(w for _, w in self._things)

    def add_thing(self, obj):
        _, w = obj
        if self.total_weight + w > self._max_weight:
            raise ValueError('превышен суммарный вес вещей')
        self._things.append(obj)


class BoxDefender:
    def __init__(self, box):
        self._box = box
        self._things = box.things[:]

    def __enter__(self):
        return self._box

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self._box.things = self._things
        return False

