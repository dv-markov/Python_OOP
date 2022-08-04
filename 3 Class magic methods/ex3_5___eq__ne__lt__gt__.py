# 3.5 Сравнения __eq__, __ne__, __lt__, __gt__ и другие
import string


class Clock:
    __DAY = 86400  # число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    def __eq__(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Операнд справа должен иметь тип int или Clock")

        sc = other if isinstance(other, int) else other.seconds
        return self.seconds == sc


print("""
Сравнение на равенство/неравенство:""")
c1 = Clock(1000)
c2 = Clock(1000)
# по умолчанию сравниваются id экземпляров класса
# чтобы это изменить, надо описать метод eq
# переопределение при сравнении двух экземпляров класса
print(c1 == c2)

c3 = Clock(2000)
print(c1 == c3)
print(c1 == 1000)

# оператор неравенства !=
# по умолчанию Python определяет с1 != с2, как not(c1 == c2)
# если не определен метод __neq__
print(c1 != c2)
print(c1 != c3)

print("""
Сравнение больше / меньше:""")


# операторы <, <=, >, >= по умолчанию не реализованы
# необходимо их прописать
class Clock:
    __DAY = 86400  # число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Операнд справа должен иметь тип int или Clock")
        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.seconds == sc

    def __lt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds < sc

    def __gt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds > sc


c1 = Clock(1000)
c3 = Clock(2000)
print(c1 < c3)

# оператор с1 > с2 вычисляется по умолчанию как c2 < c1
# если не задан метод __gt__
# и наоборот
print(c1 > c3)

# когда метод __gt__ реализован, он вызывается напрямую, без подмены

print("""
Сравнение <= / >=""")


class Clock:
    __DAY = 86400  # число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Операнд справа должен иметь тип int или Clock")
        return other if isinstance(other, int) else other.seconds

    # def __le__(self, other):
    #     sc = self.__verify_data(other)
    #     return self.seconds <= sc

    def __ge__(self, other):
        sc = self.__verify_data(other)
        return self.seconds >= sc


# аналогично <, >
c1 = Clock(1000)
c3 = Clock(2000)
print(c1 <= c3)
print(c1 >= c3)

# для работы всех методов сравнения достаточно определить основные:
# __eq__
# __lt__
# __le__
# тогда по умолчанию будут вычисляться также
# __ne__
# __gt__
# __ge__

print("""
Задачи""")


# Task 3
class Track:
    def __init__(self, start_x, start_y):
        self.track_lst = [TrackLine(start_x, start_y, 0)]

    def add_track(self, tr):
        self.track_lst.append(tr)

    def get_tracks(self):
        return tuple(self.track_lst[1:])

    def __get_len(self, i):
        x1, y1 = self.track_lst[i - 1].coords
        x2, y2 = self.track_lst[i].coords
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def __len__(self):
        # lst_len = len(self.track_lst)
        # if lst_len < 2:
        #     return 0
        return int(sum(self.__get_len(i) for i in range(1, len(self.track_lst))))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return len(self) == len(other)

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return len(self) > len(other)


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.coords = to_x, to_y
        self.max_speed = max_speed


track1 = Track(0, 0)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2 = Track(0, 1)
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))

res_eq = track1 == track2

print(len(track1))
print(len(track2))

print(track1 == track2)  # маршруты равны, если равны их длины
print(track1 != track2)  # маршруты не равны, если не равны их длины
print(track1 > track2)  # True, если длина пути для track1 больше, чем для track2
print(track1 < track2)  # True, если длина пути для track1 меньше, чем для track2

print(track1.get_tracks())
print(track2.get_tracks())

track3 = Track(5, 5)
print(len(track3))


# Task 4
class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        # self.__a = self.__b = self.__c = 0
        self.a = a
        self.b = b
        self.c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        self.__c = value

    def __setattr__(self, key, value):
        if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            super().__setattr__(key, value)

    def __get_vol(self):
        # print(self.a * self.b * self.c)
        return self.a * self.b * self.c

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.__get_vol() < other.__get_vol()

    def __le__(self, other):
        if isinstance(other, self.__class__):
            return self.__get_vol() <= other.__get_vol()


class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim


print('\n', "Task 4")
lst_shop = [ShopItem('кеды', 1024, Dimensions(40, 30, 120)),
            ShopItem('зонт', 500.24, Dimensions(10, 20, 50)),
            ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)),
            ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))]

lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)

for x in lst_shop:
    print(x.name, x.dim._Dimensions__get_vol())

for x in lst_shop_sorted:
    print(x.name, x.dim._Dimensions__get_vol())

# Variant 2 - c дескриптором
# Data Descriptor with private properties
# class Desc:
#     def __set_name__(self, owner, name):
#         self.name = f'_{owner.__name__}__{name}'
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         if instance.__class__.MIN_DIMENSION <= value <= instance.__class__.MAX_DIMENSION:
#             setattr(instance, self.name, value)
#
#
# class Dimensions:
#     MIN_DIMENSION = 10
#     MAX_DIMENSION = 10000
#
#     a = Desc()
#     b = Desc()
#     c = Desc()
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_volume(self):
#         return self.a * self.b * self.c
#
#     def __lt__(self, other):
#         return self.get_volume() < other.get_volume()
#
#     def __le__(self, other):
#         return self.get_volume() <= other.get_volume()


# Task 5
stich = ["Я к вам пишу – чего же боле?",
         "Что я могу еще сказать?",
         "Теперь, я знаю, в вашей воле",
         "Меня презреньем наказать.",
         "Но вы, к моей несчастной доле",
         "Хоть каплю жалости храня,",
         "Вы не оставите меня."]


class StringText:
    def __init__(self, lst_words):
        self.lst_words = lst_words

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return len(self.lst_words) > len(other.lst_words)

    def __ge__(self, other):
        if isinstance(other, self.__class__):
            return len(self.lst_words) >= len(other.lst_words)


lst = [[y.strip('–?!,.;') for y in x.split() if y not in "–?!,.;"] for x in stich]
# print(lst)
lst_text = map(StringText, lst)

# for item in lst_text:
#     print(item.lst_words)
#
# print(lst_text[0] > lst_text[1])
# print(lst_text[1] <= lst_text[2])

lst_text_sorted = sorted(lst_text, reverse=True)
# for item in lst_text_sorted:
#     print(len(item.lst_words), item.lst_words)

lst_text_sorted = [' '.join(x.lst_words) for x in lst_text_sorted]
# for item in lst_text_sorted:
#     print(len(item), item)


# Task 6
from string import punctuation


class Morph:
    def __init__(self, *words):
        self.lst_words = [word.lower() for word in words]

    def add_word(self, word):
        self.lst_words.append(word.lower())

    def get_words(self):
        return tuple(self.lst_words)

    def __eq__(self, other):
        return other.lower() in self.lst_words


wrds = ('связь, связи, связью, связей, связями, связях',
        'формула, формулы, формуле, формулу, формулой, формул, формулам, формулами, формулах',
        'вектор, вектора, вектору, вектором, векторе, векторы, векторов, векторам, векторами, векторах',
        'эффект, эффекта, эффекту, эффектом, эффекте, эффекты, эффектов, эффектам, эффектами, эффектах',
        'день, дня, дню, днем, дне, дни, дням, днями, днях')

# dict_words = [Morph(*(y.strip(',') for y in x.split())) for x in wrds]
dict_words = [Morph(*x.split(', ')) for x in wrds]
print(dict_words)
for x in dict_words:
    print(x.get_words())

# text = input()
text = 'Мы будем устанавливать связь завтра днем.'

print(punctuation)
print([x.strip(punctuation) in dict_words for x in text.split()])

res = sum(x.strip(punctuation) in dict_words for x in text.split())
print(res)

# Version 2
# s = """- связь, связи, связью, связи, связей, связям, связями, связях
# - формула, формулы, формуле, формулу, формулой, формул, формулам, формулами, формулах
# - вектор, вектора, вектору, вектором, векторе, векторы, векторов, векторам, векторами, векторах
# - эффект, эффекта, эффекту, эффектом, эффекте, эффекты, эффектов, эффектам, эффектами, эффектах
# - день, дня, дню, днем, дне, дни, дням, днями, днях
# """
#
# dict_words = [Morph(*line.lstrip('- ').split(', ')) for line in s.splitlines()]


# Task 7
class FileAcceptor:
    def __init__(self, *extensions):
        self.extension_tpl = extensions

    def __call__(self, filename: str, *args, **kwargs):
        return filename.endswith(self.extension_tpl)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return FileAcceptor(*set(self.extension_tpl + other.extension_tpl))


acceptor1 = FileAcceptor("jpg", "jpeg", "png")
acceptor2 = FileAcceptor("png", "bmp")
filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]

print(acceptor1(filenames[1]))
print(acceptor2(filenames[1]))
acceptor12 = acceptor1 + acceptor2
print(acceptor12.extension_tpl)

acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
filenames2 = list(filter(acceptor_images + acceptor_docs, filenames))
print(filenames2)


# Variant 2
class FileAcceptor:
    def __init__(self, *args):
        self.extensions = set(args)

    def __call__(self, file: str):
        if type(file) is str:
            return file.endswith(tuple('.' + e for e in self.extensions))

    def __add__(self, other):
        if type(other) is FileAcceptor:
            return FileAcceptor(*self.extensions.union(other.extensions))


