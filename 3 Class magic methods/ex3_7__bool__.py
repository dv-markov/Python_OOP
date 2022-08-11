# 3.7 Метод __bool__

# __len__ - вызывается функцией bool(), если не определен магический метод __bool__()
# __bool__() - вызывается в приоритетном порчдке функцией bool()

print(bool(123))
print(bool(-1))
print(bool(0))

print(bool("Python"))
print(bool(""))
print(bool([]))
print()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(3, 4)
print(bool(p))  # по умолчанию функция bool() всегда возвращает True для любых объектов пользовательского класса
# переопределить ее поведение можно через методы __len__ и __bool__
print()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print("__len__")
        return self.x * self.x + self.y * self.y


p = Point(3, 4)
print(len(p))
print(bool(p))
p1 = Point(0, 0)
print(len(p1))
print(bool(p1))
print()


# метод __bool__ отрабатывает в приоритете при вызове функции bool()
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print("__len__")
        return self.x * self.x + self.y * self.y

    def __bool__(self):
        print("__bool__")
        return self.x == self.y


p = Point(10, 10)
print(bool(p))
p1 = Point(1, 10)
print(bool(p1))

# на практике чаще всего функция bool вызывается неявно:
if p:
    print("Объект p дает True")
else:
    print("Объект p дает False")

if p1:
    print("Объект p1 дает True")
else:
    print("Объект p1 дает False")

print(p)
print(bool(p1))

