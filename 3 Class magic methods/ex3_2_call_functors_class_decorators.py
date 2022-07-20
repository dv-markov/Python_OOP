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


# Task 3
class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, file, *args, **kwargs):
        # return file.split(".")[1] in self.extensions  # выдает ошибку, если файл не содержит точку
        return file[file.find(".") + 1:] in self.extensions


filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]

# Variant 2
# метод endswith проверяет наличие заданной подстроки suffix(или кортежа подстрок) в конце передаваемой в него строки
class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, filename):
        return filename.endswith(self.extensions)


acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]


# Task 4
from string import ascii_lowercase, digits


class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""

    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")

    def is_validate(self):
        if not self.validators:
            return True

        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False

        return True


# здесь прописывайте классы валидаторов: LengthValidator и CharsValidator
class LengthValidator:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, input_string, *args, **kwargs):
        return self.min_length <= len(input_string) <= self.max_length


class CharsValidator:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, input_string, *args, **kwargs):
        return set(input_string).issubset(self.chars)


lv = LengthValidator(0, 500)  # min_length - минимально допустимая длина; max_length - максимально допустимая длина
cv = CharsValidator(ascii_lowercase+digits)  # chars - строка из допустимых символов

string = 'Hello123321Python'
res1 = lv(string)
res2 = cv(string)
print(res1, res2)

lg = LoginForm("Вход на сайт", validators=[LengthValidator(3, 50), CharsValidator(ascii_lowercase + digits)])
lg.post({"login": "root", "password": "panda"})
if lg.is_validate():
    print("Дальнейшая обработка данных формы")


# Task 5
class DigitRetrieve:
    def __call__(self, digit, *args, **kwargs):
        try:
            return int(digit)
        except ValueError:
            return


dg = DigitRetrieve()
d1 = dg("123")   # 123 (целое число)
d2 = dg("45.54")   # None (не целое число)
d3 = dg("-56")   # -56 (целое число)
d4 = dg("12fg")  # None (не целое число)
d5 = dg("abc")   # None (не целое число)
print(d1, d2, d3, d4, d5, sep='\n')


# Task 6
class RenderList:
    def __init__(self, type_list='ul'):
        self.tl = type_list if type_list == 'ol' else 'ul'

    def __call__(self, lst, *args, **kwargs):
        return f'<{self.tl}>\n<li>' + '</li>\n<li>'.join(lst) + f'</li>\n</{self.tl}>'


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html)

# Variant 2
# def __call__(self, lst: list):
#     return f'<{self.type_list}>\n' + '\n'.join([f'<li>{i}</li>' for i in lst]) + f'\n</{self.type_list}>'

# Variant 3
# def __call__(self, lst, *args, **kwargs):
#     ml = map(lambda x: f'<li>{x}</li>\n', lst)
#     return f'<{self.type_list}>\n' + ''.join(ml) + f'</{self.type_list}>'


# Task 7
class HandlerGET:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, req, *args, **kwargs):
        return self.get(self.__fn, req)

    def get(self, func, req, *args, **kwargs):
        output = 'GET: ' + func(req)
        return output if req.get('method', 'GET') == 'GET' else None


@HandlerGET
def contact(request):
    return "Сергей Балакирев"


res = contact({"method": "GET", "url": "contact.html"})
print(res)
print()


# Variant 2
# class HandlerGET:
#     def __init__(self, func):
#         self.__fn = func
#
#     def __call__(self, request, *args, **kwargs):
#         m = request.get('method', 'GET')
#         if m == 'GET':
#             return self.get(self.__fn, request)
#         return None
#
#     def get(self, func, request, *args, **kwargs):
#         return f'GET: {func(request)}'


# Task 8
class Handler:
    def __init__(self, methods=('GET',)):
        self.__methods = methods

    def __call__(self, func):
        def wrapper(request, *args, **kwargs):
            m = request.get('method', 'GET')
            if m in self.__methods:
                return self.__getattribute__(m.lower())(func, request)

        return wrapper

    def get(self, func, request, *args, **kwargs):
        return f'GET: {func(request)}'

    def post(self, func, request, *args, **kwargs):
        return f'POST: {func(request)}'


@Handler(methods=('GET', 'POST'))
def contact(request):
    return "Сергей Балакирев"


res = contact({"method": "POST", "url": "contact.html"})
print(res)


# Variant 0
# def __call__(self, func):
#     def wrapper(request, *args, **kwargs):
#         m = request.get('method', 'GET')
#         if m not in self.__methods:
#             return None
#         if m == 'GET':
#             return self.get(func, request)
#         if m == 'POST':
#             return self.post(func, request)
#
#     return wrapper


# Task 9
# class InputDigits:
#     def __init__(self, func):
#         self.__func = func
#
#     def __call__(self, *args, **kwargs):
#         return list(map(int, self.__func().split()))
#
#
# input_dg = InputDigits(input)
# res = input_dg()
# print(res)


# Task 10
# class RenderDigit:
#     def __call__(self, dig, *args, **kwargs):
#         try:
#             return int(dig)
#         except ValueError:
#             return None
#
#
# class InputValues:
#     def __init__(self, render):
#         self.render = render
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             return list(map(self.render, func().split()))
#         return wrapper
#
#
# input_dg = InputValues(RenderDigit())(input)
# res = input_dg()
# print(res)
#
# render = RenderDigit()
# d1 = render("123")   # 123 (целое число)
# d2 = render("45.54")   # None (не целое число)
# d3 = render("-56")   # -56 (целое число)
# d4 = render("12fg")  # None (не целое число)
# d5 = render("abc")   # None (не целое число)
# print(d1, d2, d3, d4, d5)