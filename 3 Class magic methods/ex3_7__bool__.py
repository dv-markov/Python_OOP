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