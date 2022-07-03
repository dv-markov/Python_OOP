# 2.1 Режимы доступа public, private, protected. Сеттеры и геттеры

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


pt = Point(1, 2)
print(pt.x, pt.y)

pt.x = 200
pt.y = "coord_y"
print(pt.x, pt.y)

# Режимы доступа:
# attribute (без подчеркиваний) - публичное свойство (public)
# _attribute (с одним _) - режим доступа protected (для обращения внутри класса и во всех дочерних классах)
# __attribute (с двумя __) - режим доступа private (обращение только внутри класса)


# _protected
class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y


pt = Point(1, 2)
print(pt._x, pt._y)

pt._x = 200
pt._y = "coord_y"
print(pt._x, pt._y)

# режим protected - _ лишь сигнализирует о том, что данное свойство является защищенным,
# но не запрещает доступ извне
# это внутренние служебные переменные, к ним лучше не обращаться извне


# __private
class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    # setter / сеттер
    def set_coord(self, x, y):
        self.__x = x
        self.__y = y

    # getter / геттер
    def get_coord(self):
        return self.__x, self.__y


pt = Point(1, 2)
# ссылка на защищенные переменные не работает
# print(pt.__x, pt.__y)

# через функцию обращаться можно
pt.set_coord(10, 20)
print(pt.get_coord())

# сеттеры и геттеры - интерфейсные методы, служат для работы с защищенными переменными класса или его экземпляра
# чтобы не нарушить работу класса, следует взаимодействовать с ним только через публичные свойства и методы
print(pt.__dict__)


# сеттеры и геттеры также используют для проверки типа данных
class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def set_coord(self, x, y):
        if type(x) in (int, float) and type(y) in (int, float):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("координаты должны быть числами")

    def get_coord(self):
        return self.__x, self.__y


pt = Point(1, 2)

pt.set_coord(10, 20)
# pt.set_coord(10, "qwerty")  # вызовет ошибку ValueError
print(pt.get_coord())


# добавление приватного метода
class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("координаты должны быть числами")

    def get_coord(self):
        return self.__x, self.__y


pt = Point(1, 2)
pt.set_coord(1000, 2000)
print(pt.get_coord())

print(dir(pt))
print(pt._Point__x)  # так делать крайне не рекомендуется, иначе возможны непредвиденные ошибки
print(pt._Point__check_value(5))  # с защищенным методом аналогично


from accessify import private, protected


# защита методов класса от доступа извне с помощью accessify
class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y

    @private
    @classmethod
    def check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("координаты должны быть числами")

    def get_coord(self):
        return self.__x, self.__y


pt = Point(1, 2)
pt.set_coord(300, 500)
print(pt.get_coord())

# работа accessify
# print(pt.check_value(5))
# выдает ошибку accessify.errors.InaccessibleDueToItsProtectionLevelException:
# Point.check_value() is inaccessible due to its protection level

