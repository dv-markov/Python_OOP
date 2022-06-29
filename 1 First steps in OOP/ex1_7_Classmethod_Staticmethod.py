# 1.7 Методы класса (classmethod) и статические методы (staticmethod)

class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        # if Vector.validate(x) and Vector.validate(y):
        #     self.x = x
        #     self.y = y

        # аналогичная запись (более универсальный вариант, устойчивый к изменению имени класса):
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

        print(self.norm2(self.x, self.y))

    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        return x*x + y*y  # квадратичная норма


# объявление и вызов методов
# вариант 1
v = Vector(1, 2)
res = v.get_coord()
print(res)

# вариант 2
v2 = Vector(3, 4)
res = Vector.get_coord(v2)
print(res)

# метод класса можно вызывать через сам класс, не указывая параметр self
# для работы с методами на уровне класса
v3 = Vector(5, 6)
print(Vector.validate(5))
res = Vector.get_coord(v3)
print(res)

# staticmethod - методы, не имеющие доступа ни к атрибутам класса, ни к атрибутам его экземпляров
# независимая, самостоятельная функция, объявленная внутри класса
v4 = Vector(1, 200)
print(Vector.norm2(5, 6))
res = Vector.get_coord(v4)
print(res)

# вызов можно прописывать как через класс, так и через экземпляр класса
v5 = Vector(10, 20)
print(v5.norm2(5, 6))
print(v5.validate(20))

# теоретически, из статического метода можно обращаться к атрибутам класса через имя класса,
# но на практике так не рекомендуется делать

# в статическом методе рекомендуется использовать параметры, только заданные как аргументы метода

