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

