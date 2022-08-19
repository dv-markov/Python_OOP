# 3.8 Методы __getitem__, __setitem__ и __delitem__

# __getitem__(self, item) - получение значения по ключу item
# __setitem__(self, key, value) - запись значения value по ключу key
# __delitem__(self, key) - удаление элемента по ключу key

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)


s1 = Student("Сергей", [5, 5, 3, 2, 5])
print(s1.marks[2])


# __getitem__
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item <= len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Неверный индекс")


s1 = Student("Иван", [1, 2, 3, 2, 5])
print(s1[2])
# несуществующий индекс вызовет ошибку
# print(s1[20])


# __setitem__
# __delitem__
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item <= len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Неверный индекс")

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым неотрицательным числом")

        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None]*off)

        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Индекс должен быть целым неотрицательным числом")

        del self.marks[key]


s1 = Student("Петр", [5, 5, 3, 2, 5])
s1[4] = 4
s1[10] = 4
print(s1.marks)
del s1[2]
print(s1.marks)


print("""
Задачи""")


# Task 2
class Record:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def __chk_indx(self, indx):
        if not isinstance(indx, int) or indx < 0 or indx > len(self.__dict__):
            raise IndexError('неверный индекс поля')

    def __getitem__(self, item):
        self.__chk_indx(item)
        return tuple(self.__dict__.values())[item]

    def __setitem__(self, key, value):
        self.__chk_indx(key)
        setattr(self, tuple(self.__dict__.keys())[key], value)


r = Record(pk=1, title='Python ООП', author='Балакирев')
print(r.__dict__)
print(r[0])
r[0] = 2 # доступ к полю pk
r[1] = 'Супер курс по ООП'
print(r[0], r[1])


# Task 3
class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.points = []

    def add_point(self, x, y, speed):
        self.points.append([(x, y), speed])

    def __chk_indx(self, indx):
        if not isinstance(indx, int) or indx < 0 or indx > len(self.points) - 1:
            raise IndexError('некорректный индекс')

    def __getitem__(self, item):
        self.__chk_indx(item)
        return self.points[item]

    def __setitem__(self, key, value):
        self.__chk_indx(key)
        self.points[key][1] = value


tr = Track(10, -5.4)
tr.add_point(20, 0, 100)  # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80)  # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34)  # третий линейный сегмент: indx = 2

print(tr.__dict__)
print(tr[0])

tr[2] = 60
c, s = tr[2]
print(c, s)

# res = tr[3] # IndexError


# Task 4
class Array:
    def __init__(self, max_length, cell):
        self.array = [cell() for _ in range(max_length)]

    def __chk_indx(self, indx):
        if not isinstance(indx, int) or indx < 0 or indx > len(self.array) - 1:
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __getitem__(self, item):
        self.__chk_indx(item)
        return self.array[item].value

    def __setitem__(self, key, value):
        self.__chk_indx(key)
        self.array[key].value = value

    def __repr__(self):
        return " ".join(str(x.value) for x in self.array)


class Integer:
    def __init__(self, start_value=0):
        self.value = start_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        if type(val) != int:
            raise ValueError('должно быть целое число')
        self.__value = val


class Float:
    def __init__(self, start_value=0):
        self.value = start_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        if type(val) not in (int, float):
            raise ValueError('должно быть вещественное число')
        self.__value = val


ar = Array(10, Float)
print(ar[0], ar[1], ar[2])

ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(ar_int) # должны отображаться все значения массива в одну строчку через пробел
ar_int[1] = 10
# ar_int[1] = 10.5 # должно генерироваться исключение ValueError
# ar_int[10] = 1 # должно генерироваться исключение IndexError


# Task 5
class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) != int:
            raise ValueError('возможны только целочисленные значения')
        setattr(instance, self.name, value)


class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value


class TableValues:
    def __init__(self, rows, cols, cell=None):
        if cell is None:
            raise ValueError('параметр cell не указан')
        self.cells = tuple(tuple(cell() for _ in range(cols)) for _ in range(rows))

    def __getitem__(self, item):
        i, j = item
        return self.cells[i][j].value

    def __setitem__(self, key, value):
        i, j = key
        self.cells[i][j].value = value


c1 = CellInteger(999)
print(c1.__dict__)
print(CellInteger.__dict__)
TV = TableValues(2, 3, CellInteger)
print(TV.__dict__)
print(TV[1, 2])

table = TableValues(2, 3, cell=CellInteger)
print(table[0, 1])
table[1, 1] = 10
# table[0, 0] = 1.45 # генерируется исключение ValueError
# вывод таблицы в консоль
for row in table.cells:
    for x in row:
        print(x.value, end=' ')
    print()


# Д/З
class StringValue:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) != str:
            raise ValueError('возможны только целочисленные значения')
        setattr(instance, self.name, value)


class CellString:
    value = StringValue()

    def __init__(self, start_value=''):
        self.value = start_value


# Task 6
# Variant 0
class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.last = None
        self.ln = 0

    def push(self, obj):
        if self.top is None:
            self.top = obj
        if self.last:
            self.last.next = obj
        self.last = obj
        self.ln += 1

    def pop(self):
        res = self.last
        if self.top:
            if self.top.next:
                tmp = self.top
                while tmp.next.next:
                    tmp = tmp.next
                tmp.next = None
                self.last = tmp
                self.ln -= 1
            else:
                self.top = self.last = None
                self.ln = 0
        return res

    def __check(self, indx):
        if type(indx) != int or indx < 0 or indx >= self.ln:
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__check(item)
        if self.top:
            i = 0
            tmp = self.top
            while i < item:
                tmp = tmp.next
                i += 1
            return tmp

    def __setitem__(self, key, value):
        self.__check(key)
        if self.top:
            i = 0
            tmp = self.top
            while i < key - 1:
                tmp = tmp.next
                i += 1
            value.next = tmp.next.next
            tmp.next = value


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st[1] = StackObj("new obj2")
print(st[2].data)  # obj3
print(st[1].data)  # new obj2
print(st.pop().data)
print(st.pop().data)
print(st.pop().data)
a = st.pop()
print(a.data if a else None)


# Task 7 - slices for classes
class RadiusVector:
    def __init__(self, *coords):
        self.coords = list(coords)

    def __getitem__(self, item):
        res = self.coords[item]
        return tuple(res) if isinstance(res, list) else res

    def __setitem__(self, key, value):
        self.coords[key] = value


v = RadiusVector(1, 1, 1, 1)
print(v[1]) # 1
v[:] = 1, 2, 3, 4
print(v[2]) # 3
print(v[1:]) # (2, 3, 4)
v[0] = 10.5


# Task 8
class Cell:
    def __init__(self):
        self.is_free = True
        self.value = 0

    def __bool__(self):
        return self.is_free

    def __setattr__(self, key, value):
        if key == 'value' and value > 0:
            if not self.is_free:
                raise ValueError('клетка уже занята')
            else:
                self.is_free = False
        super().__setattr__(key, value)


class TicTacToe:
    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    def clear(self):
        for row in self.pole:
            for cell in row:
                cell.is_free = True
                cell.value = 0

    def __check(self, indx):
        for x in indx:
            if type(x) not in (int, slice) or (type(x) == int and (x < 0 or x > 2)):
                raise IndexError('неверный индекс клетки')
        return indx

    def __getitem__(self, item):
        i, j = self.__check(item)
        if type(i) == slice:
            return tuple(x[j].value for x in self.pole)
        if type(j) == slice:
            return tuple(x.value for x in self.pole[i])
        return self.pole[i][j].value

    def __setitem__(self, key, value):
        i, j = self.__check(key)
        self.pole[i][j].value = value


game = TicTacToe()
for row in game.pole:
    print(*(map(lambda x: x.value, row)))
game.clear()
game[0, 0] = 1
game[1, 0] = 2
for row in game.pole:
    print(*(map(lambda x: x.value, row)))
# формируется поле:
# 1 0 0
# 2 0 0
# 0 0 0
# game[3, 2] = 2 # генерируется исключение IndexError
if game[0, 0] == 0:
    game[0, 0] = 2
v1 = game[0, :]  # 1, 0, 0
v2 = game[:, 0]  # 1, 2, 0
print(v1)
print(v2)
print(game[0, 0])

# Variant 2
# def __setitem__(self, key, value):
#     self.__check(key)
#     r, c = key
#     if self.pole[r][c]:
#         self.pole[r][c].value = value
#         self.pole[r][c].is_free = False
#     else:
#         raise ValueError('клетка уже занята')