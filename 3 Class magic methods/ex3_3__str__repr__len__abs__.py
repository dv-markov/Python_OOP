# 3.3 Методы __str__, __repr__, __len__, __abs__


# Методы __str__ и __repr__
class Cat:
    def __init__(self, name):
        self.name = name

    # метод __repr__ предназначен для вывода информации в режиме отладки
    def __repr__(self):
        return f"{self.__class__}: {self.name}"

    # метод __str__ предназначен для вывода информации для пользователя
    # если не определен метод __str__, то по умолчанию вызывается метод __repr__
    def __str__(self):
        return f"{self.name}"


cat = Cat("Васька")
print(cat)
print(str(cat))


# Методы __len__ и __abs__
class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return list(map(abs, self.__coords))


p = Point(1, -2, -5)
print(len(p))
print(abs(p))

print("""
Задачи""")


# Task 1
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Книга: {self.title}; {self.author}; {self.pages}"


import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
book = Book(*lst_in)
print(book)




