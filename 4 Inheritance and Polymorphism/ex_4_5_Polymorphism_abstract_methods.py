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
