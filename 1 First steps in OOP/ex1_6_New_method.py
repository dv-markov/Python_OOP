# 1.6 Магический метод __new__. Пример паттерна Singleton

# Метод __new__ вызывается перед созданием экземпляра класса
# Метод __init__ вызывается сразу после создания объекта

class Point:
    def __new__(cls, *args, **kwargs):
        print("вызов __new__ для " + str(cls))
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print("вызов __init__ для " + str(self))


pt = Point(1, 2)
print(pt)

# Начиная с Python 3, все классы наследуются от базового класса Object


# Паттерн проектирования Singleton
class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"соединение с БД: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("закрытие соединения с БД")

    def read(self):
        return "данные из БД"

    def write(self, data):
        print(f"запись в БД {data}")


db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 40)
print(id(db), id(db2))

db.connect()
db2.connect()


print("""
Задачи""")


# Task 6
class AbstractClass:
    def __new__(cls, *args, **kwargs):
        return "Ошибка: нельзя создавать объекты абстрактного класса"


obj1 = AbstractClass()
print(obj1)


# Task 7
# здесь объявляйте класс SingletonFive
class SingletonFive:
    # двойное подчеркивание - защищенная переменная класса
    __instance = None
    instance_count = 0

    def __new__(cls, *args, **kwargs):
        if cls.instance_count < 5:
            cls.__instance = super().__new__(cls)
        cls.instance_count += 1
        return cls.__instance

    def __init__(self, name):
        if self.instance_count < 6:
            self.name = name


# objs = [SingletonFive(str(n)) for n in range(10)]  # эту строчку не менять
#
# print(*(x.name for x in objs))

objs = []
for i in range(10):
    print(i)
    objs.append(SingletonFive(str(i)))
    print(objs[i].name)

print(*objs, sep='\n')
print(*(x.name for x in objs))

# для управления содержимым создаваемых экземпляров класса, которые ссылаются на предыдущие экземпляры (singleton),
# используется магический метод __call__

# Variant 2 - Sergey Balakirev:
# def __new__(cls, *args, **kwargs):
#     if cls.__count < 5:
#         cls.__instance = super().__new__(cls)
#         cls.__instance.name = args[0]
#         cls.__count += 1
#
#     return cls.__instance


# Task 8
TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    def __new__(cls, *args, **kwargs):
        __instance = DialogWindows() if TYPE_OS == 1 else DialogLinux()
        __instance.name = args[0]
        return __instance


dlg = Dialog('123')
print(dlg.name_class, dlg.name)

# Variant 2
# class Dialog:
#     def __new__(cls, *args, **kwargs):
#         __instance = super().__new__(DialogWindows) if TYPE_OS == 1 else super().__new__(DialogLinux)
#         __instance.name = args[0]
#         return __instance


# Task 9
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        obj = super().__new__(self.__class__)
        for k, v in self.__dict__.items():
            setattr(obj, k, v)
        return obj


pt = Point(1, 2)
pt_clone = pt.clone()

print(pt, pt.x, pt.y)
print(pt_clone, pt_clone.x, pt_clone.y)
print(*pt.__dict__)

# оператор двойной распаковки может использоваться для передачи всех аргументов экземпляра класса
# Variant 2
# def clone(self):
#     return self.__class__(**self.__dict__)


# Task 10
class Factory:
    def build_sequence(self):
        return []

    def build_number(self, string):
        return float(string)


class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


# эти строчки не менять!
ld = Loader()
s = input()
res = ld.parse_format(s, Factory())

print(res)