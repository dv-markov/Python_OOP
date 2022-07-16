# 3.2 Метод __call__. Функторы и классы-декораторы
import math


# Магический метод - dunder метод
class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, *args, **kwargs):
        print("__call__")
        self.__counter += 1
        return self.__counter


# магический метод __call__ запускается при  вызове класса (создании экземпляра класса)
# __call__ содержит инструкции по вызову __new__, __init__ и других встроенных методов
c = Counter()
# экземпляры класса по умолчанию нельзя вызывать подобно функциям и классам
# c()

# если явно прописать метод __call__ в классе, при вызове экземпляра не будет возникать ошибки
c()
print(c())

# классы, экземпляры которых являются вызываемыми, называются функторы
c()
c()
c()
print(c())

# каждый объект класса будет иметь независимые локальные переменные
c2 = Counter()
res = c()
res2 = c2()
print(res, res2)


# при вызове экземпляра можно передавать ему необходимые аргументы
class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, step=1, *args, **kwargs):
        print("__call__")
        self.__counter += step
        return self.__counter


c = Counter()
c2 = Counter()
c()
c(2)
res = c(10)
res2 = c2(-5)
print(res, res2)


# Использование - 1 - замена замыканий функций
class StripChars:
    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError("Аргумент должен быть строкой")

        return args[0].strip(self.__chars)


s1 = StripChars("?:!.; ")
s2 = StripChars(" ")
res = s1(" Hello world! ")
res2 = s2(" Hello world! ")
res3 = s2("  Balakirev!  ")
print(res, res2, res3, sep='\n')
print()


# Второе применение - замена декораторов на основе функций
# Класс-декоратор
class Derivate:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx


def df_sin(x):
    return math.sin(x)


print(df_sin(math.pi/3))

# вызов класса-декоратора осуществляется двумя способами
# Первый - создать экземпляр класса и именем функции и ссылкой на ту же функцию в качестве аргумента
df_sin = Derivate(df_sin)
print(df_sin(math.pi/3))


# Второй - использовать класс как декоратор функции
@Derivate
def df_sin(x):
    return math.sin(x)


print(df_sin(math.pi/3))


print("""
Задачи""")

# Task 1
from random import choices, randint


# через класс-функтор
class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        return ''.join(choices(self.psw_chars, k=randint(self.min_length, self.max_length)))


min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
rnd = RandomPassword(psw_chars, min_length, max_length)
psw = rnd()
print(psw)
lst_pass = [rnd() for _ in range(3)]
print(lst_pass)


# через замыкание функции
def random_password(psw_chars, min_length, max_length):
    def randomizator3000():
        return ''.join(choices(psw_chars, k=randint(min_length, max_length)))
    return randomizator3000


rnd1 = random_password(psw_chars, min_length, max_length)
print(rnd1(), rnd1())
lst_pass_closure = [rnd1() for _ in range(5)]
print(lst_pass_closure)

