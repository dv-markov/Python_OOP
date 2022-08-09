# 3.6 Методы __eq__ и __hash__

print("""
Задачи""")


#Task 4
class Rect:
    def __init__(self, x, y, width, height):
        self.coords = x, y
        self.width = width
        self.height = height

    def __hash__(self):
        return hash((self.width, self.height))


r1 = Rect(10, 5, 100, 50)
r2 = Rect(-10, 4, 100, 50)

h1, h2 = hash(r1), hash(r2)   # h1 == h2
print(h1, h2, sep="\n")


# Task 6
import sys


# здесь объявляйте классы
class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return hash(self) == hash(other)


i1 = ShopItem("Монитор Samsung", 2000, 34000)
i2 = ShopItem("Клавиатура", 200.44, 545)
i3 = ShopItem("Монитор Samsung", 2000, 34000)
print(i1.__dict__, hash(i1))
print(i2.__dict__, hash(i2))
print(i3.__dict__, hash(i3))
print(i1 == i2, i2 == i3, i1 == i3)

# считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # список lst_in в программе не менять!
# print(lst_in)
lst_in = ["Системный блок: 1500 75890.56",
          "Монитор Samsung: 2000 34000",
          "Клавиатура: 200.44 545",
          "Монитор Samsung: 2000 34000"]
print(lst_in)

shop_items = {}
for x in lst_in:
    name, val = x.split(':')
    weight, price = map(float, val.split())
    print(name, weight, price, sep=" / ")
    item = ShopItem(name, weight, price)
    shop_items.setdefault(item, [item, 0])[1] += 1

print(shop_items)

# Variant 0:
# for x in lst_in:
#     name, val = x.split(':')
#     weight, price = val.split()
#     print(name, weight, price, sep=" / ")
#     item = ShopItem(name, weight, price)
#     qty = shop_items.get(item)
#     print(item, qty)
#     if qty:
#         shop_items[item][1] = qty[1] + 1
#     else:
#         shop_items.setdefault(item, [item, 1])

# Variant 2
shop_items = {}
for item in lst_in:
    name, weight, price = item.rsplit(maxsplit=2)
    obj = ShopItem(name[:-1], weight, price)
    shop_items.setdefault(obj, [obj, 0])[1] += 1
print(shop_items, "\n")


# Task 7
print("Task 7")
import sys


class DataBase:
    def __init__(self, path=None):
        self.path = path
        self.dict_db = {}

    def write(self, record):
        self.dict_db.setdefault(record, []).append(record)

    def read(self, pk):
        res = [x for value in self.dict_db.values() for x in value if x.pk == pk]
        return res[0] if len(res) else None


class Record:
    PK = 1

    def __init__(self, fio: str, descr: str, old: int):
        self.pk = Record.PK
        Record.PK += 1
        self.fio = fio
        self.descr = descr
        self.old = old

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return hash(self) == hash(other)


# считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines())) # список lst_in не менять!

# здесь продолжайте программу (используйте список строк lst_in)
lst_in = ['Балакирев С.М.; программист; 33',
          'Кузнецов Н.И.; разведчик-нелегал; 35',
          'Суворов А.В.; полководец; 42',
          'Иванов И.И.; фигурант всех подобных списков; 26',
          'Балакирев С.М.; преподаватель; 33'
          ]

db = DataBase()
for entry in lst_in:
    *strings, num = entry.split("; ")
    db.write(Record(*strings, int(num)))

print(db.dict_db)
print(db.read(1))

# Объединение вложенных списков
# sum([[1, 2], [3, 4]], []) == [1, 2, 3, 4]

# распаковка итерируемого объекта из одного элемента
# def read(self, pk):
#     return next(obj for lst in self.dict_db.values() for obj in lst if obj.pk == pk)

# манипуляции со значениями, прочитанными их входного потока
# for l in lst_in:
#     args = list(map(str.strip, l.split(';')))
#     args[-1] = int(args[-1])
#     db.write(Record(*args))



