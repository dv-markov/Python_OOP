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

print("""
Задачи""")


# Task 4
# Version 0
# class Player:
#     def __init__(self, name, old, score):
#         self.name = name
#         self.old = old
#         self.score = score
#
#     def __bool__(self):
#         return bool(self.score)
#
#
# # lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in = ['Балакирев; 34; 2048',
#           'Mediel; 27; 0',
#           'Влад; 18; 9012',
#           'Nina P; 33; 0']
#
# # players = [Player(*p.split('; ')) for p in lst_in]
#
# players = []
# for p in lst_in:
#     args = p.split('; ')
#     args[1:] = list(map(int, args[1:]))
#     players.append(Player(*args))
# players_filtered = filter(bool, players)
#
# for p in players_filtered:
#     print(p.__dict__)

# Version 1
class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = int(old)
        self.score = int(score)

    def __bool__(self):
        return bool(self.score)


# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['Балакирев; 34; 2048',
          'Mediel; 27; 0',
          'Влад; 18; 9012',
          'Nina P; 33; 0']

players = [Player(*p.split('; ')) for p in lst_in]
players_filtered = list(filter(bool, players))

for p in players_filtered:
    print(p.__dict__)

# Version 2
# class Player:
#     def __init__(self, name: str, old: int, score: int):
#         self.name = name
#         self.old = old
#         self.score = score
#
#     def __bool__(self):
#         return self.score > 0
#
# players = [Player(*map(lambda x: int(x) if x.isdigit() else x, line.split('; '))) for line in lst_in]
# players_filtered = list(filter(lambda x: bool(x), players))

# Version 3
# None для фильтра работает, как bool
# players_filtered = list(filter(None, players))


# Task 5
import sys


class MailBox:
    def __init__(self):
        self.inbox_list = []

    def receive(self):
        # lst_in = list(map(str.strip, sys.stdin.readlines()))
        lst_in = ['sc_lib@list.ru; От Балакирева; Успехов в IT!',
                  'mail@list.ru; Выгодное предложение; Вам одобрен кредит.',
                  'mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить.']
        self.inbox_list += [MailItem(*msg.split('; ')) for msg in lst_in]

class MailItem:
    def __init__(self, mail_from, title, content):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False

    def set_read(self, fl_read=True):
        self.is_read = fl_read

    def __bool__(self):
        return self.is_read


mail = MailBox()
mail.receive()
mail.inbox_list[0].set_read()
mail.inbox_list[-1].set_read()
inbox_list_filtered = list(filter(bool, mail.inbox_list))

for msg in inbox_list_filtered:
    print(msg.__dict__)


# Task 6 - check
class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __len__(self):
        line_len = ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5
        return int(line_len)


l1 = Line(0, 0, 0, 0.99)
print(len(l1))
print(bool(l1))


# Task 7 - check
class Ellipse:
    def __init__(self, *coords):
        if len(coords) == 4:
            self.x1, self.y1, self.x2, self.y2 = coords

    def __bool__(self):
        return {'x1', 'y1', 'x2', 'y2'} <= self.__dict__.keys()

    def get_coords(self):
        if not self:
            raise AttributeError('нет координат для извлечения')
        return self.x1, self.y1, self.x2, self.y2


lst_geom = [Ellipse(),
            Ellipse(),
            Ellipse(5, 4, 3, 2),
            Ellipse(6, 7, 8, 9)]
for x in lst_geom:
    if x:
        x.get_coords()
        print(x.get_coords())

e1 = Ellipse()
print(e1.__dict__, bool(e1))
e2 = Ellipse(1, 2, 3, 4)
print(e2.__dict__, bool(e2))


# Task 8 - check
from random import randint


class GamePole:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, N, M, total_mines):
        # if type(N) == int and type(M) == int and N > 0 and M > 0:
        self.__pole_cells = tuple(tuple(Cell() for _ in range(M)) for _ in range(N))
        self.__n = N
        self.__m = M
        # if type(total_mines) == int and 0 <= total_mines <= M * N:
        self.total_mines = total_mines

    # def __setattr__(self, key, value):
    #     if key in ('__n')

    @property
    def pole(self):
        return self.__pole_cells

    def __set_mines(self):
        mines = 0
        while mines < self.total_mines:
            i = randint(0, self.__n - 1)
            j = randint(0, self.__m - 1)
            if not self.pole[i][j].is_mine:
                self.pole[i][j].is_mine = True
                mines += 1

    def __count_mines(self):
        for i in range(self.__n):
            for j in range(self.__m):
                self.pole[i][j].number = sum([int(cell.is_mine)
                                              for row in self.pole[max(i-1, 0):min(i+2, self.__n)]
                                              for cell in row[max(j-1, 0):min(j+2, self.__m)]
                                              ]) - (1 if self.pole[i][j].is_mine else 0)

    def init_pole(self):
        for row in self.pole:
            for cell in row:
                cell.is_open = False
                cell.is_mine = False
        self.__set_mines()
        self.__count_mines()

    def open_cell(self, i, j):
        if 0 <= i <= self.__n and 0 <= j <= self.__m:
            self.pole[i][j].is_open = True
        else:
            raise IndexError('некорректные индексы i, j клетки игрового поля')

    def show_pole(self):
        for row in self.pole:
            for cell in row:
                if cell.is_open:
                    print('*' if cell.is_mine else cell.number, end=' ')
                else:
                    print('#', end=' ')
            print()


class Cell:
    def __init__(self):
        self.is_mine = False
        self.number = 0
        self.is_open = False

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, mine):
        if type(mine) != bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_mine = mine

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, num):
        if type(num) != int or not 0 <= num <= 8:
            raise ValueError("недопустимое значение атрибута")
        self.__number = num

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, cell_open):
        if type(cell_open) != bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_open = cell_open

    def __bool__(self):
        return not self.is_open


x = 10
y = 20
mines = 30
print(f"Сапер, поле {x} x {y}, {mines} мин")
pole = GamePole(x, y, mines)
pole.init_pole()
if pole.pole[0][1]:
    pole.open_cell(0, 1)
if pole.pole[3][5]:
    pole.open_cell(3, 5)
# pole.open_cell(30, 100)
pole.show_pole()

print("Поле открыто")
for row in pole.pole:
    for cell in row:
        cell.is_open = True
pole.show_pole()
