# 3.9 Методы __iter__ и __next__

# __iter__(self) - получение итератора для перебора объекта
# __next__(self) - переход к следующему значению и его считывание

lst = [8, 5, 3, 1, 7]
it = iter(lst)
print(next(it))
print(next(it))

lst2 = list(range(5))
print(lst2)

a = iter(range(5))
print(next(a))
print(next(a))
print(next(a))
print(next(a))


class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration


fr = FRange(0, 2, 0.5)
# __next__ идентичен next
print(fr.__next__())
print(fr.__next__())
print(next(fr))
print(next(fr))
# Stop iteration
# print(fr.__next__())

# Итератор - объект, для которого определен магический метод __next__.
# Итерируемый объект - объект, для которого определен магический метод __iter__.

# По умолчанию объекты (даже итераторы) не являются итерируемыми объектами
# fr = FRange(0, 2, 0.5)
# for x in fr: # не сработает, если функция __iter__ не определена
#     print(x)


class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration


print('\n', 'Итерируемый объект:', sep='')
fr = FRange(0, 2, 0.5)
# цикл работает, потому что определен метод __iter__ и объект является итерируемым
# функция for сначала получает итератор (неявно вызывает метод __iter__),
# а потом с помощью неявного вызова метода __next__ последовательно перебирает итерируемый объект
for x in fr:
    print(x)


class FRange2D:
    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
        self.rows = rows
        self.fr = FRange(start, stop, step)

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            # return iter(self.fr)
            return self.fr
        else:
            raise StopIteration


print('\n', 'Frange2D:', sep='')
fr = FRange2D(0, 2, 0.5, 4)
for row in fr:
    for x in row:
        print(x, end=' ')
    print()


# Task 5
class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job

    @staticmethod
    def __check(indx):
        if not isinstance(indx, int) or not (0 <= indx <= 4):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__check(item)
        return list(self.__dict__.values())[item]

    def __setitem__(self, key, value):
        self.__check(key)
        setattr(self, list(self.__dict__.keys())[key], value)

    def __iter__(self):
        self.values = list(self.__dict__.values())
        self.ln = len(self.values)
        self.i = -1
        return self

    def __next__(self):
        if self.i < self.ln - 1:
            self.i += 1
            return self.values[self.i]
        else:
            raise StopIteration


pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
print(pers.__dict__)

for x in pers:
    print(x)
pers[0] = 'Dmitry Markov'
print(pers[0])
print(pers[1])


# Variant 2 - Balakirev
class Person1:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self._attrs = tuple(self.__dict__)
        self._len_attrs = len(self._attrs)
        self._iter_index = - 1

    def __check_index(self, index):
        if type(index) != int or not (-self._len_attrs <= index < self._len_attrs):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__check_index(item)
        return getattr(self, self._attrs[item])

    def __setitem__(self, key, value):
        self.__check_index(key)
        setattr(self, self._attrs[key], value)

    def __iter__(self):
        self._iter_index = - 1
        return self

    def __next__(self):
        if self._iter_index < self._len_attrs - 1:
            self._iter_index += 1
            return getattr(self, self._attrs[self._iter_index])
        raise StopIteration


pers1 = Person1('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
print(next(pers1))

for x in pers1:
    print(x)
pers1[0] = 'Dmitry Markov'
print(pers1[0])
print(pers1[1])


# Task 6
class TriangleListIterator:
    def __init__(self, lst):
        self.line_lst = [x for i in range(len(lst)) for x in lst[i][:i+1]]
        self._lst_len = len(self.line_lst)
        self._iter_indx = - 1

    def __iter__(self):
        self._iter_indx = - 1
        return self

    def __next__(self):
        if self._iter_indx < self._lst_len - 1:
            self._iter_indx += 1
            return self.line_lst[self._iter_indx]
        raise StopIteration


lst = [[1],
       [2, 3],
       [4, 5, 6],
       [7, 8, 9, 10]]
it = TriangleListIterator(lst)
print(it.__dict__)
print(next(it))

for x in it:
    print(x)

it_iter = iter(it)
x = next(it_iter)
print(x)
print(next(it_iter))
print(next(it_iter))


# Variant 2 - Balakirev
class TriangleListIterator1:
    def __init__(self, lst):
        self._lst = lst

    def __iter__(self):
        for i in range(len(self._lst)):
            for j in range(i + 1):
                yield self._lst[i][j]


it1 = TriangleListIterator1(lst)
for x in it1:
    print(x)

it_iter = iter(it1)
x = next(it_iter)
print(x)


# Task 7
class IterColumn:
    def __init__(self, lst, column):
        self._lst = lst
        self._col = column

    def __iter__(self):
        for i in range(len(self._lst)):
            yield self._lst[i][self._col]


lst = [[11, 12, 13, 14],
       [21, 22, 23, 24],
       [31, 32, 33, 34],
       [41, 42, 43, 44]]

it = IterColumn(lst, 1)
for x in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
    print(x)

it_iter = iter(it)
x = next(it_iter)
print(x)

# # Variant 2 - Balakirev
# def __iter__(self):
#     for row in self._lst:
#         yield row[self._col]


# Task 7 - plane
class IterColumn:
    def __init__(self, lst, column):
        self._lst = lst
        self._column = column

    def __iter__(self):
        for row in self._lst:
            yield row[self._column]


lst = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
it = IterColumn(lst, 1)
for x in it:
    print(x)

it_iter = iter(it)
x = next(it_iter)
print(x)
print(next(it_iter))
print(next(it_iter))


# Task 8 - Stack-like structure
class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.__len = 0

    @staticmethod
    def __check_obj(obj):
        if not isinstance(obj, StackObj):
            raise TypeError('Object should be StackObj type')

    def __check_indx(self, indx):
        if not (0 <= indx < self.__len):
            raise IndexError('неверный индекс')

    def push_back(self, obj):
        self.__check_obj(obj)
        if self.top is None:
            self.top = obj
        else:
            tmp = self.top
            while tmp.next:
                tmp = tmp.next
            tmp.next = obj
        self.__len += 1

    def push_front(self, obj):
        self.__check_obj(obj)
        if self.top:
            obj.next = self.top
        self.top = obj
        self.__len += 1

    def __iter__(self):
        tmp = self.top
        while tmp:
            yield tmp
            tmp = tmp.next

    def __len__(self):
        return self.__len

    def __setitem__(self, key, value):
        self.__check_indx(key)
        it = iter(self)
        for _ in range(key):
            next(it)
        x = next(it)
        x.data = value

    def __getitem__(self, item):
        self.__check_indx(item)
        it = iter(self)
        for _ in range(item):
            next(it)
        x = next(it)
        return x.data


    # def get_stack(self):
    #     if self.top is None:
    #         return None
    #     res = []
    #     tmp = self.top
    #     while tmp:
    #         res.append(tmp.data)
    #         tmp = tmp.next
    #     return res


st = Stack()
st.push_back(StackObj('привет'))
st.push_back(StackObj('как'))
st.push_back(StackObj('дела'))
st.push_front(StackObj('Хэй!'))
# print(*st.get_stack())

for x in st:
    print(x.data)
print(len(st))

st[2] = 'идут'
for x in st:
    print(x.data)
print(st[0])


# Variant 2 - Balakirev
class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class Stack:
    def __init__(self):
        self.top = None
        self.__last = None

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        else:
            self.__last.next = obj
        self.__last = obj

    def push_front(self, obj):
        if self.top is None:
            self.__last = self.top = obj
        else:
            obj.next = self.top
            self.top = obj

    def __iter__(self):
        h = self.top
        while h:
            yield h
            h = h.next

    def __len__(self):
        return sum(1 for _ in self)

    def _get_obj(self, indx):
        if type(indx) != int or not (0 <= indx < len(self)):
            raise IndexError('Неверный индекс')
        for i, obj in enumerate(self):
            if i == indx:
                return obj

    def __getitem__(self, item):
        return self._get_obj(item).data

    def __setitem__(self, key, value):
        self._get_obj(key).data = value


# Task 9
class Cell:
    def __init__(self, data=0):
        self.data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


class TableValues:
    def __init__(self, rows, cols, type_data=int):
        self.type_data = type_data
        self.table_size = rows, cols
        self.table = tuple(tuple(Cell() for _ in range(cols)) for _ in range(rows))

    def __iter__(self):
        for row in self.table:
            yield (x.data for x in row)

    def __check_indx(self, indx):
        for k, k_max in zip(indx, self.table_size):
            if type(k) != int or not (0 <= k < k_max):
                raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__check_indx(item)
        i, j = item
        return self.table[i][j].data

    def __setitem__(self, key, value):
        self.__check_indx(key)
        if type(value) != self.type_data:
            raise TypeError("неверный тип данных")
        i, j = key
        self.table[i][j].data = value


tv1 = TableValues(3, 3)
print(tv1.__dict__)
tv1[1, 2] = 555
print(tv1[0, 0])

for row in tv1:
    for val in row:
        print(val, end=' ')
    print()


# Task 10
class Matrix:
    def __init__(self, *args):
        if len(args) == 3 and type(args[0]) == int and type(args[1]) == int and type(args[2]) in (int, float):
            self.rows, self.cols, fill_value = args
            self.mtx = [[fill_value for _ in range(self.cols)] for _ in range(self.rows)]
        elif len(args) == 1 and type(args[0]) == list:
            self.rows = len(args[0])
            self.cols = len(args[0][1])
            if any(map(lambda x: len(x) != self.cols, args[0])) or \
                    any(type(x) not in (int, float) for row in args[0] for x in row):
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            self.mtx = args[0]
        else:
            raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')

    def __check_indx(self, indx):
        r, c = indx
        if type(r) != int or type(c) != int or not (0 <= r < self.rows) or not (0 <= c < self.cols):
            raise IndexError('недопустимые значения индексов')
        return r, c

    def __getitem__(self, item):
        r, c = self.__check_indx(item)
        return self.mtx[r][c]

    def __setitem__(self, key, value):
        r, c = self.__check_indx(key)
        if type(value) not in (int, float):
            raise TypeError('значения матрицы должны быть числами')
        self.mtx[r][c] = value

    def __add__(self, other):
        if isinstance(other, self.__class__):
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError('операции возможны только с матрицами равных размеров')
            return Matrix([[self.mtx[i][j] + other.mtx[i][j] for j in range(self.cols)] for i in range(self.rows)])
        elif type(other) in (int, float):
            return Matrix([[self.mtx[i][j] + other for j in range(self.cols)] for i in range(self.rows)])

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError('операции возможны только с матрицами равных размеров')
            return Matrix([[self.mtx[i][j] - other.mtx[i][j] for j in range(self.cols)] for i in range(self.rows)])
        elif type(other) in (int, float):
            return self.__add__(-other)


matrix = Matrix(2, 2, 1)
print(matrix.__dict__)

mt = Matrix([[1, 2], [3, 4]])
print(mt.__dict__)

mt2 = matrix + mt
print(mt2.__dict__)

mt3 = matrix + 10
print(mt3.__dict__)

mt4 = matrix - mt
print(mt4.__dict__)

mt5 = matrix - 10
print(mt5.__dict__)


