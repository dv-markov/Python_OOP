# 4.5 Полиморфизм и абстрактные методы

# Полиморфизм - возможность работы с разными объектами единым образом
# Абстрактный метод - метод, заданный на уровне базового класса без определенного функционала,
# требует обязательного переопределения в дочерних классах

# обычный способ вызова однотипных функций из разных классов
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_rect_pr(self):
        return 2 * (self.w + self.h)


class Square:
    def __init__(self, a):
        self.a = a

    def get_sq_pr(self):
        return 4 * self.a


r1 = Rectangle(1, 2)
r2 = Rectangle(3, 4)
s1 = Square(10)
s2 = Square(20)
print(r1.get_rect_pr(), r2.get_rect_pr())
print(s1.get_sq_pr(), s2.get_sq_pr())

geom = [r1, r2, s1, s2]

for g in geom:
    if isinstance(g, Rectangle):
        print(g.get_rect_pr())
    else:
        print(g.get_sq_pr())
print()


# обычный способ сложно реализуем для большого количества классов
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_rect_pr(self):
        return 2 * (self.w + self.h)


class Square:
    def __init__(self, a):
        self.a = a

    def get_sq_pr(self):
        return 4 * self.a


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_tr_pr(self):
        return self.a + self.b + self.c


r1 = Rectangle(1, 2)
r2 = Rectangle(3, 4)
s1 = Square(10)
s2 = Square(20)
t1 = Triangle(1, 2, 3)
t2 = Triangle(4, 5, 6)

geom = [r1, r2, s1, s2, t1, t2]

for g in geom:
    if isinstance(g, Rectangle):
        print(g.get_rect_pr())
    elif isinstance(g, Square):
        print(g.get_sq_pr())
    else:
        print(g.get_tr_pr())
print('\n' + 'Полиморфизм')


# Реализация с использованием полиморфизма
# Обязательно использовать одинаковое наименование метода во всех классах
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        return 2 * (self.w + self.h)


class Square:
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4 * self.a


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_pr(self):
        return self.a + self.b + self.c


geom = [Rectangle(1, 2), Rectangle(3, 4),
        Square(10), Square(20),
        Triangle(1, 2, 3), Triangle(4, 5, 6)
        ]

for g in geom:
    print(g.get_pr())
print('\n' + 'Абстрактный метод')


# Создание абстрактного метода
class Geom:
    def get_pr(self):
        # return -1
        # В питоне нет "настоящих" абстрактных методов, мы выполняем имитацию поведения абстрактного метода
        raise NotImplementedError('В дочернем классе должен быть переопределен метод get_pr()')


class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        return 2 * (self.w + self.h)


class Square(Geom):
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4 * self.a


class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_pr(self):
        return self.a + self.b + self.c


geom = [Rectangle(1, 2), Rectangle(3, 4),
        Square(10), Square(20),
        Triangle(1, 2, 3), Triangle(4, 5, 6)
        ]

for g in geom:
    print(g.get_pr())

# по-настоящему абстрактный класс должен наследовать от класса ABC (Abstract Base Class)
# экземпляр абстрактного класса не может быть создан
from abc import ABC, abstractmethod


# Настоящий абстрактный класс
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass


# a = Animal()
# TypeError: Can't instantiate abstract class Animal with abstract methods move


# Имитация абстрактного класса
class Animal:
    @abstractmethod
    def move(self):
        pass


a = Animal()


# На самом деле абстрактный метод в Python не обязательно должен быть "полностью абстрактным",
# что отличается от некоторых других объектно-ориентированных языков программирования.
# Можно определить некоторые общие вещи в абстрактном методе и использовать функцию super()
# для вызова его в подклассах.
class Animal(ABC):
    @abstractmethod
    def move(self):
        print('Animal moves')


class Cat(Animal):
    def move(self):
        super().move()
        print('Cat moves')


c = Cat()
c.move()
# Animal moves
# Cat moves

# Совместно с декоратором @abstractmethod можно использовать такие декораторы,
# как @property, @classmethod и @staticmethod.
# Когда декоратор @abstractmethod применяется в сочетании с другими дескрипторами методов,
# его следует применять как самый внутренний декоратор.


# Также можно определить абстрактное свойство для чтения и записи,
# соответствующим образом пометив один или несколько базовых методов как абстрактные:
class C(ABC):
    @property
    def x(self):
        ...

    @x.setter
    @abstractmethod
    def x(self, val):
        pass


# Если только некоторые компоненты являются абстрактными,
# только эти компоненты необходимо обновить, чтобы создать конкретное свойство в подклассе:
class D(C):
    @C.x.setter
    def x(self, val):
        pass


# Общий пример концепции определения абстрактных классов.
class C(ABC):
    @abstractmethod
    def my_abstract_method(self):
        pass

    @classmethod
    @abstractmethod
    def my_abstract_classmethod(cls):
        pass

    @staticmethod
    @abstractmethod
    def my_abstract_staticmethod():
        pass

    @property
    @abstractmethod
    def my_abstract_property(self):
        pass

    @my_abstract_property.setter
    @abstractmethod
    def my_abstract_property(self, val):
        pass

    @abstractmethod
    def _get_x(self):
        pass

    @abstractmethod
    def _set_x(self, val):
        pass

    x = property(_get_x, _set_x)


print("""
Задачи""")


# Task 3
class Student:
    def __init__(self, fio, group):
        self._fio = fio  # ФИО студента (строка)
        self._group = group  # группа (строка)
        self._lect_marks = []  # оценки за лекции
        self._house_marks = []  # оценки за домашние задания

    def add_lect_marks(self, mark):
        self._lect_marks.append(mark)

    def add_house_marks(self, mark):
        self._house_marks.append(mark)

    def __str__(self):
        return f"Студент {self._fio}: оценки на лекциях: {str(self._lect_marks)}; " \
               f"оценки за д/з: {str(self._house_marks)}"


class Mentor:
    _name = None

    def __init__(self, fio, subject):
        self._fio = fio
        self._subject = subject

    def set_mark(self, student, mark):
        raise NotImplementedError('В дочерних классах должен быть реализован метод set_mark()')

    def __str__(self):
        return f"{self._name} {self._fio}: предмет {self._subject}"


class Lector(Mentor):
    _name = 'Лектор'

    def set_mark(self, student, mark):
        student.add_lect_marks(mark)


class Reviewer(Mentor):
    _name = 'Эксперт'

    def set_mark(self, student, mark):
        student.add_house_marks(mark)


lector = Lector("Балакирев С.М.", "Информатика")
reviewer = Reviewer("Гейтс Б.", "Информатика")
students = [Student("Иванов А.Б.", "ЭВМд-11"), Student("Гаврилов С.А.", "ЭВМд-11")]
persons = [lector, reviewer]
lector.set_mark(students[0], 4)
lector.set_mark(students[1], 2)
reviewer.set_mark(students[0], 5)
reviewer.set_mark(students[1], 3)

for p in persons + students:
    print(p)


# Task 4
class ShopInterface:
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):
    def __init__(self, name: str, weight: float, price: float):
        self._name = name
        self._weight = weight
        self._price = price
        self.__id = hash((name, weight, price))

    def get_id(self):
        return self.__id


si = ShopItem('phone', 200, 100_000)
print(si.get_id())


# Task 5
class Validator:
    def _is_valid(self, data):
        raise NotImplementedError('в классе не переопределен метод _is_valid')


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        return isinstance(data, float) and self.min_value <= data <= self.max_value

    def __call__(self, value):
        return self._is_valid(value)


float_validator = FloatValidator(0, 10.5)
print(res_1 := float_validator(1))  # False (целое число, а не вещественное)
print(res_2 := float_validator(1.0))  # True
print(res_3 := float_validator(-1.0))  # False (выход за диапазон [0; 10.5])


# Task 6
from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def go(self):
        """Метод для перемещения транспортного средства"""

    @classmethod
    @abstractmethod
    def abstract_class_method(cls):
        """Абстрактный метод класса"""


class Bus(Transport):
    def __init__(self, model, speed):
        self._model = model
        self._speed = speed

    def go(self):
        print("bus go")

    @classmethod
    def abstract_class_method(cls):
        pass

#######################

class Model(ABC):
    @abstractmethod
    def get_pk(self):
        """Абстрактный метод класса Model"""

    def get_info(self):
        return "Базовый класс Model"


class ModelForm(Model):
    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = hash(login)

    def get_pk(self):
        return self._id


form = ModelForm("Логин", "Пароль")
print(form.get_pk())