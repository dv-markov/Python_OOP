# 4.4. Наследование. Атрибуты private и protected

# attribute - публичное свойство (public)
# _attribute - защищенное св-во (protected), доступны в текущем и во всех дочерних классах
# __attribute - приватное св-во (private), служит для обращения только внутри класса,
# private атрибуты не доступны в дочерних классах

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
        self._verify_coords(x1) #  сработает
        self._fill = fill


r = Rect(10, 10, 20, 20)
print(r.__dict__)

print("""
Задачи""")


# Task 5







