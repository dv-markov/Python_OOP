# 4.6 Множественное наследование

# Миксины (mixins) - примеси

class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class MixinLog:
    ID = 0

    def __init__(self):
        print("init MixinLog")
        MixinLog.ID += 1
        self.id = MixinLog.ID

    def save_sell_log(self):
        print(f"{self.id}: товар был продан в 00:00 часов")


# При множественном наследовании по-умолчанию вызывается только инициализатор первого класса в списке
# (если он есть)
class NoteBook(Goods, MixinLog):
    pass


n = NoteBook('Acer', 1.8, 30_000)
n.print_info()
n.save_sell_log()

# MRO - Method Resolution Order
print(NoteBook.__mro__)
# Инициализатор первого базового класса сработает в первую очередь
# Следующие за первым родительские классы должны иметь в своем инициализаторе только параметр self.


# Если все-таки требуется наследовать несколько базовых классов с параметрами в инициализаторе,
# конструкция приобретает следующий вид:
class Goods:
    def __init__(self, name, weight, price):
        super().__init__(1)
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class MixinLog:
    ID = 0

    def __init__(self, p1):
        super().__init__(1, 2)
        print("init MixinLog")
        MixinLog.ID += 1
        self.id = MixinLog.ID

    def save_sell_log(self):
        print(f"{self.id}: товар был продан в 00:00 часов")


class MixinLog2:
    ID = 0

    def __init__(self, p1, p2):
        print("init MixinLog2")
        MixinLog.ID += 1
        self.id = MixinLog.ID


class NoteBook(Goods, MixinLog, MixinLog2):
    pass


n = NoteBook('Asus', 1.8, 30_000)
n.print_info()
n.save_sell_log()
# Каждый раз при вызове super() вызывается инициализатор следующего класса по списку


# Для избежания ошибок принято в базовых дополнительных классах использовать только один параметр - self
# Тогда дополнительные классы можно указывать в любом порядке
class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class MixinLog:
    ID = 0

    def __init__(self):
        super().__init__()
        print("init MixinLog")
        MixinLog.ID += 1
        self.id = MixinLog.ID

    def save_sell_log(self):
        print(f"{self.id}: товар был продан в 00:00 часов")


class MixinLog2:
    ID = 0

    def __init__(self):
        print("init MixinLog2")
        MixinLog.ID += 1
        self.id = MixinLog.ID


class NoteBook(Goods, MixinLog2, MixinLog):
    pass


n = NoteBook('Lenovo', 1.8, 30_000)
n.print_info()
n.save_sell_log()


# Использование методов с одинаковыми именами из разных классов
class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class MixinLog:
    ID = 0

    def __init__(self):
        print("init MixinLog")
        MixinLog.ID += 1
        self.id = MixinLog.ID

    def save_sell_log(self):
        print(f"{self.id}: товар был продан в 00:00 часов")

    def print_info(self):
        print(f"print_info из MixinLog")


class NoteBook(Goods, MixinLog2, MixinLog):
    pass


n = NoteBook('HP', 1.8, 30_000)
n.print_info()
n.save_sell_log()

# Вариант 1 - вызывать через метод класса
MixinLog.print_info(n)


# Вариант 2 - переопределить метод в дочернем классе
class NoteBook(Goods, MixinLog2, MixinLog):
    def print_info(self):
        MixinLog.print_info(self)


n = NoteBook('Monster', 1.8, 30_000)
n.print_info()


# Способ сделать так, чтобы родительские классы наследовались вне зависимости от порядка указания
class A:
    def __init__(self, name, old):
        super().__init__()
        self.name = name
        self.old = old


class B:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class C(B, A):
    def __init__(self, name, old, weight, height):
        super().__init__(name, old)
        self.weight = weight
        self.height = height


person = C("Balakirev", 33, 80, 185)
print(person.__dict__)


print("""
Задачи""")


# Task 4
class Digit:
    ALLOWED_TYPES = int, float

    def __init__(self, value):
        self._verify_number(value)
        self.value = value

    def _verify_number(self, value):
        if type(value) not in self.ALLOWED_TYPES:
            self._err()

    def _err(self):
        raise TypeError('значение не соответствует типу объекта')


class Integer(Digit):
    ALLOWED_TYPES = int,


class Float(Digit):
    ALLOWED_TYPES = float,


class Positive(Digit):
    def _verify_number(self, value):
        super()._verify_number(value)
        if value <= 0:
            self._err()


class Negative(Digit):
    def _verify_number(self, value):
        super()._verify_number(value)
        if value >= 0:
            self._err()


class PrimeNumber(Integer, Positive):
    pass


class FloatPositive(Float, Positive):
    pass


# i = Negative(-100)
# print(i.__dict__)

PN = (10, 37, 800)
FP = (21.123, 13.45, 123.247, 4564.234, 0.1)
digits = [PrimeNumber(x) for x in PN] + [FloatPositive(y) for y in FP]
lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))

for v in lst_positive + lst_float:
    print(v.__dict__)


# Variant 2 - Евгений Вохмин
# class Digit:
#     def __init__(self, value):
#         self._value = value
#
#     def __setattr__(self, name, value):
#         if not self._check_value(value):
#             raise TypeError('значение не соответствует типу объекта')
#         super().__setattr__(name, value)
#
#     def _check_value(self, value):
#         return type(value) in (int, float)
#
#
# class Integer(Digit):
#     def _check_value(self, value):
#         return super()._check_value(value) and type(value) is int
#
#
# class Float(Digit):
#     def _check_value(self, value):
#         return super()._check_value(value) and type(value) is float
#
#
# class Positive(Digit):
#     def _check_value(self, value):
#         return super()._check_value(value) and value > 0
#
#
# class Negative(Digit):
#     def _check_value(self, value):
#         return super()._check_value(value) and value < 0


# Task 5
class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


class ShopGenericView:
    def __repr__(self):
        return "\n".join(f"{k}: {v}" for k, v, in self.__dict__.items())


class ShopUserView:
    def __repr__(self):
        return "\n".join(f"{k}: {v}" for k, v, in tuple(self.__dict__.items())[1:])


class Book(ShopItem, ShopUserView):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year


book = Book("Python ООП", "Балакирев", 2022)
print(book)


# Variant 2 -
# class ShopGenericView:
#     def __iter__(self):
#         for i in self.__dict__.items():
#             yield i
#
#     def __str__(self):
#         return '\n'.join(map(lambda x: f'{x[0]}: {x[1]}', self))
#
# class ShopUserView(ShopGenericView):
#     def __iter__(self):
#         for data in list(self.__dict__.items())[1::]:
#             yield data


# Task 8
class RetriveMixin:
    def get(self, request):
        return "GET: " + request.get('url')


class CreateMixin:
    def post(self, request):
        return "POST: " + request.get('url')


class UpdateMixin:
    def put(self, request):
        return "PUT: " + request.get('url')


class GeneralView:
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')

    def render_request(self, request):
        method = request.get('method')
        if method not in self.allowed_methods:
            raise TypeError(f"Метод {method} не разрешен.")
        return getattr(self, method.lower())(request)


class DetailView(RetriveMixin, GeneralView):
    allowed_methods = ('GET', 'PUT', )


view = DetailView()
html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'GET'})
print(html)   # GET: https://stepik.org/course/116336/
# html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'PUT'})
# print(html)   # AttributeError: 'DetailView' object has no attribute 'put'


class DetailView(RetriveMixin, UpdateMixin, GeneralView):
    allowed_methods = ('GET', 'PUT', )


view = DetailView()
html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'PUT'})
print(html)


# Task 9
class MoneyOperators:
    def __add__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money + other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money + other.money)

    def __sub__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money - other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money - other.money)


class Money:
    def __init__(self, value):
        if type(value) not in (int, float):
            raise TypeError('сумма должна быть числом')
        self._money = value

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        self._money = value


class MoneyR(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyR: {self.money}"


class MoneyD(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyD: {self.money}"


m1 = MoneyR(1)
m2 = MoneyD(2)
m = m1 + 10
print(m)  # MoneyR: 11
m = m1 - 5.4
print(m)
# m = m1 + m2  # TypeError