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
# при создании объекта класса Line, сначала вызывается метод __call__ - из метакласса object
# он содержит вызовы магических методов __new__ и __init__
# если __new__ не определен в Line и Geom, то он вызывается из класса onject
# далее, метод __init__ ищется в классе Line, и если он там не определен, то в классе Geom


# Функция super()
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
        super().__init__(x1, y1, x2, y2)
        print("инициализатор Rect")
        self.fill = fill

    def draw(self):
        print("Рисование прямоугольника")


l = Line(0, 0, 10, 20)
print(l.__dict__)

r = Rect(10, 10, 100, 200)
print(r.__dict__)
