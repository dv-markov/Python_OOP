# 1.4 Методы классов. Параметр self

# свойства - данные (существительные)
# методы - действия (глаголы)

class Point:
    color = 'red'
    circle = 2

    def set_coords():
        print("вызов метода set_coords")


print(Point.set_coords)
Point.set_coords()

pt = Point()
print(pt.set_coords)
# вызов метода экземпляра класса без аргумента self в описании класса выдает ошибку
# pt.set_coords()


# поэтому при объявлении метода внутри класса нужно всегда указывать параметр self
class Point2:
    color = 'red'
    circle = 2

    def set_coords(self):
        print("вызов метода set_coords" + str(self))


# тогда все будет работать
pt2 = Point2()
print(pt2.set_coords)
# ссылка self ведет на объект pt2, через который был вызван данный метод
pt2.set_coords()

# при вызове метода из класса нужно передавать ссылку на экземпляр класса
# это эквивалент записи pt2.set_coords()
Point2.set_coords(pt2)


# через параметр self можно задавать локальные свойства объекта класса
class Point3:
    color = 'red'
    circle = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)


pt3 = Point3()
pt3.set_coords(1, 2)
print(pt3.__dict__)

pt4 = Point3()
pt4.set_coords(20, 30)
print(pt4.__dict__)

print(pt3.get_coords())

# доступ к методам класса можно получить через функцию getattr
# но обычно используется синтаксис через точку
f = getattr(pt3, "get_coords")
print(f)
print(f())

print("""
Задачи""")


# Task 4
class MediaPlayer:

    def open(self, file):
        self.filename = file

    def play(self):
        print('Воспроизведение', self.filename)


media1 = MediaPlayer()
media2 = MediaPlayer()
media1.open("filemedia1")
media2.open("filemedia2")
media1.play()
media2.play()


# Task 5
class Graph:
    LIMIT_Y = (0, 10)

    def set_data(self, data: list):
        self.data = data

    def draw(self):
        print(*filter(lambda x: self.LIMIT_Y[0] <= x <= self.LIMIT_Y[1], self.data))


lst = [10, -5, 100, 20, 0, 80, 45, 2, 5, 7]
graph_1 = Graph()
graph_1.set_data(lst)
graph_1.draw()


# Task 7
import sys


class StreamData:

    def create(self, fields, lst_values):
        if len(fields) != len(lst_values):
            return False
        try:
            for a, b in zip(fields, lst_values):
                setattr(self, a, b)
            return True
        except Exception:
            return False


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        # lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        # print(lst_in)
        lst_in = ['10', 'Питон - основы мастерства', '512']
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()
print(data.__dict__)
print(result)

# Variant 2
# class StreamData:
#     def create(self, fields, lst_values):
#         self.__dict__ = dict(zip(fields, lst_values))
#         return len(lst_values) == len(fields)


# Task 9
import sys

# программу не менять, только добавить два метода
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы
    def insert(self, data):
        for line in data:
            self.lst_data.append(dict(zip(self.FIELDS, line.split())))

    def select(self, a, b):
        # return self.lst_data[a:(min(b + 1, len(self.lst_data)))]
        # крайняя граница среза может превышать длину списка
        return self.lst_data[a:b + 1]


db = DataBase()
db.insert(lst_in)
print(db.select(0, 100))
print(DataBase.lst_data)


# Task 10
class Translator:
    D = {}

    def add(self, eng, rus):
        self.D.setdefault(eng, []).append(rus)

    def remove(self, eng):
        del self.D[eng]
        # Удалять лучше методом pop
        # self.D.pop(eng, False)

    def translate(self, eng):
        return self.D.get(eng, [None])


tr = Translator()
tr_data_1 = [('tree', 'дерево'),
             ('car', 'машина'),
             ('car', 'автомобиль'),
             ('leaf', 'лист'),
             ('river', 'река'),
             ('go', 'идти'),
             ('go', 'ехать'),
             ('go', 'ходить'),
             ('milk', 'молоко')
             ]
for ru, en in tr_data_1:
    tr.add(ru, en)
print(tr.D)
tr.remove('car')
# print(tr.D)
print(*tr.translate('go'))

# Variant 2
# list_words = """tree - дерево
# car - машина
# car - автомобиль
# leaf - лист
# river - река
# go - идти
# go - ехать
# go - ходить
# milk - молоко"""
# for row in list_words.split('\n'):
#     eng, rus = row.split(' - ')
#     tr.add(eng, rus)
# print(tr.D)
# tr.remove('car')
# # print(tr.D)
# print(*tr.translate('go'))

# Variant 3
# Объявить словарь в экземпляре класса (внутри метода add):
# Тогда для каждого экземпляра класса словарь будут уникален
# def add(self, eng, rus):
#     if 'tr' not in self.__dict__:
#         self.tr = {}
