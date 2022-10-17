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


