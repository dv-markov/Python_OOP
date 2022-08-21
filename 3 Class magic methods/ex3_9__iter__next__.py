# 3.9 Методы __iter__ и __next__


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

# Итератор - объект, для которого определена функция __next__.
# Итерируемый объект - объект, для которого определена функция __iter__.

# По умолчанию объекты (даже итераторы) не являются итерируемыми объектами
# fr = FRange(0, 2, 0.5)
# for x in fr: # не сработает, если функция __iter__ не определена
#     print(x)


class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration

    def __iter__(self):
        self.value = self.start - self.step
        return self


print('\n', 'Итерируемый объект:', sep='')
fr = FRange(0, 2, 0.5)
for x in fr: # не сработает, если функция __iter__ не определена
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
            return iter(self.fr)
        else:
            raise StopIteration


print('\n', 'Frange2D:', sep='')
fr = FRange2D(0, 2, 0.5, 4)
for row in fr:
    for x in row:
        print(x, end=' ')
    print()



