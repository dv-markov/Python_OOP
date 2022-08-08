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
print(shop_items)