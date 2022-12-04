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
