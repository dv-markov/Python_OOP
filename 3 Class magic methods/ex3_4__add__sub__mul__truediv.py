# 3.4 Методы __add__, __sub__, __mul__, __truediv__

# сложение объекта с числом
from operator import add, sub, mul, truediv


class Clock:
    __DAY = 86400  # число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")

    def __add__(self, other):
        if not isinstance(other, int):
            raise ArithmeticError("Правый операнд должен быть int")
        return Clock(self.seconds + other)


c1 = Clock(1000)
c1.seconds = c1.seconds + 100
print(c1.get_time())

c1 = c1 + 100
print(c1.get_time())


# сложение двух объектов одного класса
class Clock:
    __DAY = 86400  # число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int или Clock")

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        return Clock(self.seconds + sc)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        print("__iadd__")
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int или Clock")

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        self.seconds += sc
        return self


c1 = Clock(1000)
c2 = Clock(2000)
c3 = c1 + c2
print(c3.get_time())

c4 = Clock(3000)
c5 = c1 + c2 + c3 + c4
print(c5.get_time())

# важен порядок записи
# c1 = 100 + c1  # не сработает по умолчанию
# для складывания с объектом класса, расположенного справа, нужно прописать метод __radd__
# тогда все сработает
c1 = 100 + c1
print(c1.get_time())

# операцию += описывает метод __iadd__
c1 += 100
print(c1.get_time())
# по умолчанию вызывается метод __add__ и создается новый экземпляр класса

# таким образом описываются все операции сложения
# остальные операции - аналогично
# x + y     __add__(self, other)    x += y      __iadd__(self, other)
# x - y     __sub__(self, other)    x -= y      __isub__(self, other)
# x * y     __mul__(self, other)    x *= y      __imul__(self, other)
# x / y     __truediv__(self, other)    x /= y      __itruediv__(self, other)
# x // y    __floordiv__(self, other)   x //= y      __ifloordiv__(self, other)
# x % y     __mod__(self, other)    x %= y      __imod__(self, other)

print("""
Задачи""")


# Task 4
class NewList:
    def __init__(self, lst=None):
        self.lst = lst or []

    def __sub__(self, other):
        lst_2 = self.__check_list(other)
        return NewList(self.__subtract_lists(self.lst, lst_2))

    def __rsub__(self, other):
        lst_1 = self.__check_list(other)
        return NewList(self.__subtract_lists(lst_1, self.lst))

    def __isub__(self, other):
        lst_2 = self.__check_list(other)
        self.lst = self.__subtract_lists(self.lst, lst_2)
        return self

    @staticmethod
    def __check_list(list_n):
        if not isinstance(list_n, (list, NewList)):
            raise ArithmeticError("Правый операнд должен быть list или NewList")
        if isinstance(list_n, NewList):
            return list_n.get_list()
        return list_n

    @staticmethod
    def __subtract_lists(lst1, lst2):
        lst2_tmp = lst2[:]
        res = []
        for i in range(len(lst1)):
            for j in range(len(lst2_tmp)):
                if lst1[i] is lst2_tmp[j]:
                    lst2_tmp.pop(j)
                    break
            else:
                res.append(lst1[i])
        return res

    def get_list(self):
        return self.lst


lst1 = NewList() # пустой список
lst2 = NewList([-1, 0, 7.56, True]) # список с начальными значениями
print(lst1.__dict__)
print(lst2.__dict__)

lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2  # NewList: [-4, 6, 10, 11, 15, False]
print(res_1.get_list())

lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
print(lst1.get_list())

res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
print(res_2.get_list())

res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
print(res_3.get_list())
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
print(res_4.get_list())

print(a.get_list())

# Variant 2 - без учета повторов и True / False == 1 /0
# return NewList(list(filter(lambda x: x not in lst_sub, self.lst)))

# Variant 3 - у учетом bool != int, но без учета повторов
# return [x for x in lst1 if all(map(lambda y: x is not y, lst2))]

# Variant 3 - Balakirev
# @staticmethod
# def __diff_list(lst_1, lst_2):
#     if len(lst_2) == 0:
#         return lst_2
#     sub = lst_2[:]
#     return [x for x in lst_1 if not self.__is_elem(x, sub)]
#
# @staticmethod
# def __is_elem(x, sub):
#     res = any(map(lambda xx: type(x) == type(xx) and x == xx, sub))
#     if res:
#         sub.remove(x)
#     return res


# Task 5
class ListMath:
    def __init__(self, lst_math=None):
        self.lst_math = list(filter(lambda x: type(x) in (int, float), lst_math)) if lst_math else []

    @staticmethod
    def __operate(value1, value2, operator_fn):
        if type(value1) in (int, float):
            return [operator_fn(value1, x) for x in value2]
        elif type(value2) in (int, float):
            return [operator_fn(x, value2) for x in value1]
        else:
            raise ArithmeticError("Операнд должен быть целым или вещественным числом")

    def __add__(self, other):
        return ListMath(self.__operate(self.lst_math, other, add))

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.lst_math = self.__operate(self.lst_math, other, add)
        return self

    def __sub__(self, other):
        return ListMath(self.__operate(self.lst_math, other, sub))

    def __rsub__(self, other):
        return ListMath(self.__operate(other, self.lst_math, sub))

    def __isub__(self, other):
        self.lst_math = self.__operate(self.lst_math, other, sub)
        return self

    def __mul__(self, other):
        return ListMath(self.__operate(self.lst_math, other, mul))

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        self.lst_math = self.__operate(self.lst_math, other, mul)
        return self

    def __truediv__(self, other):
        return ListMath(self.__operate(self.lst_math, other, truediv))

    def __rtruediv__(self, other):
        return ListMath(self.__operate(other, self.lst_math, truediv))

    def __itruediv__(self, other):
        self.lst_math = self.__operate(self.lst_math, other, truediv)
        return self


lst = ListMath([1, "abc", -5, 7.68, True])
print(lst.__dict__)

lst = lst + 76 # сложение каждого числа списка с определенным числом
print(lst.lst_math)
lst = 6.5 + lst # сложение каждого числа списка с определенным числом
print(lst.lst_math)
lst += 76.7  # сложение каждого числа списка с определенным числом
print(lst.lst_math)
lst = lst - 76 # вычитание из каждого числа списка определенного числа
print(lst.lst_math)
lst = 7.0 - lst # вычитание из числа каждого числа списка
print(lst.lst_math)
lst -= 76.3
print(lst.lst_math)

lst = lst * 5 # умножение каждого числа списка на указанное число (в данном случае на 5)
print(lst.lst_math)
lst = 5 * lst # умножение каждого числа списка на указанное число (в данном случае на 5)
print(lst.lst_math)
lst *= 5.54
print(lst.lst_math)
lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
print(lst.lst_math)
lst = 3 / lst # деление числа на каждый элемент списка
print(lst.lst_math)
lst /= 13.0
print(lst.lst_math)


# Variant 2 - можно вызывать магические методы арифметических операций для любых объектов, в т. ч. для чисел
# class ListMath:
#     def __init__(self, arg=[]):
#         self.lst_math = [i for i in arg if type(i) in (int, float)]
#
#     def do(self, fn_name, other, new=True):
#         result = [getattr(i, fn_name)(other) for i in self.lst_math]
#         if new:
#             return ListMath(result)
#         else:
#             self.lst_math = result
#             return self
#
#     def __add__(self, other):
#         return self.do('__add__', other)
#
#     def __sub__(self, other):
#         return self.do('__sub__', other)
#
#     def __rsub__(self, other):
#         return self.do('__rsub__', other)
#
#     def __mul__(self, other):
#         return self.do('__mul__', other)
#
#     def __rmul__(self, other):
#         return self.do('__rmul__', other)
#
#     def __truediv__(self, other):
#         return self.do('__truediv__', other)
#
#     def __iadd__(self, other):
#         return self.do('__add__', other, False)
#
#     def __isub__(self, other):
#         return self.do('__sub__', other, False)
#
#     def __imul__(self, other):
#         return self.do('__mul__', other, False)
#
#     def __idiv__(self, other):
#         return self.do('__truediv__', other, False)


# Task 6
class StackObj:
    def __init__(self, data: str):
        self.__data = data
        self.__next = None

    def set_next(self, obj):
        self.__next = obj

    def get_next(self):
        return self.__next

    def get_data(self):
        return self.__data


class Stack:
    def __init__(self):
        self.top = None

    def push_back(self, obj):
        if self.top:
            tmp = self.top
            while tmp.get_next():
                tmp = tmp.get_next()
            tmp.set_next(obj)
        else:
            self.top = obj

    def pop_back(self):
        if self.top:
            if self.top.get_next() is None:
                tmp = self.top
                self.top = None
                return tmp.get_data()
            else:
                tmp1 = self.top
                tmp2 = self.top.get_next()
                while tmp2.get_next():
                    tmp1 = tmp2
                    tmp2 = tmp2.get_next()
                tmp1.set_next(None)
                return tmp2.get_data()

    def __add__(self, other):
        self.push_back(other)
        return self

    def __mul__(self, other):
        for d in other:
            self.push_back(StackObj(d))
        return self

    def get_stack_items(self):
        tmp = self.top
        res = []
        while tmp:
            res.append(tmp.get_data())
            tmp = tmp.get_next()
        return res

assert hasattr(Stack, 'pop_back'), "класс Stack должен иметь метод pop_back"
st = Stack()
print(st.get_stack_items())
top = StackObj("1")
st.push_back(top)
print(st.get_stack_items())
assert st.top == top, "неверное значение атрибута top"

st = st + StackObj("2")
st = st + StackObj("3")
obj = StackObj("4")
st += obj
print(st.get_stack_items())

st = st * ['data_1', 'data_2']
st *= ['data_3', 'data_4']
print(st.get_stack_items())

d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
h = top
i = 0
while h:
    assert h._StackObj__data == d[i], "неверное значение атрибута __data, возможно, " \
                                      "некорректно работают операторы + и *"
    h = h._StackObj__next
    i += 1

assert i == len(d), "неверное число объектов в стеке"

print(st.pop_back())
print(st.pop_back())
print(st.get_stack_items())


# Variant 2 - refactored
class StackObj:
    def __init__(self, data: str):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        self.__next = obj


class Stack:
    def __init__(self):
        self.top = None

    def push_back(self, obj):
        if self.top:
            tmp = self.top
            while tmp.next:
                tmp = tmp.next
            tmp.next = obj
        else:
            self.top = obj

    def pop_back(self):
        if self.top:
            if self.top.next:
                tmp = self.top
                while tmp.next.next:
                    tmp = tmp.next
                tmp.next = None
            else:
                self.top = None

    def __add__(self, other):
        self.push_back(other)
        return self

    def __mul__(self, other):
        for d in other:
            self.push_back(StackObj(d))
        return self

    def get_stack_items(self):
        tmp = self.top
        res = []
        while tmp:
            res.append(tmp._StackObj__data)
            tmp = tmp.next
        return res


assert hasattr(Stack, 'pop_back'), "класс Stack должен иметь метод pop_back"
st = Stack()
top = StackObj("1")
st.push_back(top)
assert st.top == top, "неверное значение атрибута top"
st = st + StackObj("2")
st = st + StackObj("3")
obj = StackObj("4")
st += obj
st = st * ['data_1', 'data_2']
st *= ['data_3', 'data_4']
d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
h = top
i = 0
while h:
    assert h._StackObj__data == d[i], "неверное значение атрибута __data, возможно, " \
                                      "некорректно работают операторы + и *"
    h = h._StackObj__next
    i += 1

assert i == len(d), "неверное число объектов в стеке"
st.pop_back()
st.pop_back()
print(st.get_stack_items())


# Task 7
class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year


class Lib:
    def __init__(self):
        self.book_list = []

    def __add__(self, other):
        if isinstance(other, Book):
            self.book_list.append(other)
        return self

    def __sub__(self, other):
        if isinstance(other, Book) and other in self.book_list:
            self.book_list.remove(other)
        elif isinstance(other, int) and other < len(self.book_list):
            self.book_list.pop(other)
        return self

    def __len__(self):
        return len(self.book_list)


b1 = Book('Война и мир', 'Лев Толстой', 1867)
b2 = Book('Искусство войны', 'Сунь Цзы', -325)
l1 = Lib()
l1 = l1 + b1
l1 += b2
print(len(l1))
print(l1.__dict__)
l1 -= b1
print(l1.__dict__)
l1 = l1 - 0
print(l1.__dict__)


# Task 8
class Budget:
    def __init__(self):
        self.item_list = []

    def add_item(self, it):
        if isinstance(it, Item):
            self.item_list.append(it)

    def remove_item(self, indx):
        if type(indx) == int and indx < len(self.item_list):
            self.item_list.pop(indx)

    def get_items(self):
        return self.item_list


# аннотация аргументов для нескольких типов работает только начиная с Python3.10
class Item:
    def __init__(self, name: str, money: int | float):
        self.name = name
        self.money = money

    def __add__(self, other):
        addend = 0
        if isinstance(other, Item):
            addend = other.money
        elif isinstance(other, (int, float)):
            addend = other
        return self.money + addend

    def __radd__(self, other):
        return self + other


my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))
# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x
print(s)


# Task 9
class Box3D:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def __add__(self, other):
        if isinstance(other, Box3D):
            return Box3D(*map(sum, zip(self.get_coords(), other.get_coords())))

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Box3D(*map(other.__mul__, self.get_coords()))

    def __rmul__(self, other):
        return self * other

    def __sub__(self, other):
        if isinstance(other, Box3D):
            return Box3D(*map(lambda x: x[0] - x[1], zip(self.get_coords(), other.get_coords())))

    def __floordiv__(self, other):
        if isinstance(other, int):
            return Box3D(*map(lambda x: x // other, self.get_coords()))

    def __mod__(self, other):
        if isinstance(other, int):
            return Box3D(*map(lambda x: x % other, self.get_coords()))

    def get_coords(self):
        return self.width, self.height, self.depth


box1 = Box3D(1, 2, 3)
box2 = Box3D(2, 4, 6)
box = box1 + box2  # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
print(box.__dict__)
box = box1 * 2    # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
print(box.__dict__)
box = 3 * box2    # Box3D: width=6, height=12, depth=18
print(box.__dict__)
box = box2 - box1 # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
print(box.__dict__)
box = box1 // 2   # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
print(box.__dict__)
box = box2 % 3    # Box3D: width=2, height=1, depth=0
print(box.__dict__)

# Variant 2
# class Box3D:
#     def __init__(self, width, height, depth):
#         self.width = width
#         self.height = height
#         self.depth = depth
#
#     def get_attrs(self):
#         return self.width, self.height, self.depth
#
#     def __add__(self, other):
#         return Box3D(*map(sum, zip(self.get_attrs(), other.get_attrs())))
#
#     def __mul__(self, other):
#         return Box3D(*[i * other for i in self.get_attrs()])
#
#     def __rmul__(self, other):
#         return self * other
#
#     def __sub__(self, other):
#         return self + other * (-1)
#
#     def __floordiv__(self, other):
#         return Box3D(*[i // other for i in self.get_attrs()])
#
#     def __mod__(self, other):
#         return Box3D(*[i % other for i in self.get_attrs()])

# Variant 3
# from operator import add, sub, mul, mod, floordiv
#
# class Box3D:
#     def __init__(self, width, height, depth):
#         self.width = width
#         self.height = height
#         self.depth = depth
#
#     def __make_calc(self, other, op):
#         data = self.width, self.height, self.depth
#         if isinstance(other, Box3D):
#             data2 = other.width, other.height, other.depth
#             return (op(s, o) for s, o in zip(data, data2))
#         elif type(other) in (int, float):
#             return (op(b, other) for b in data)
#         return 0, 0, 0
#
#     def __add__(self, other):
#         return Box3D(*self.__make_calc(other, add))
#
#     def __radd__(self, other):
#         return self.__add__(other)
#
#     def __sub__(self, other):
#         return Box3D(*self.__make_calc(other, sub))
#
#     def __mul__(self, num):
#         return Box3D(*self.__make_calc(num, mul))
#
#     def __rmul__(self, num):
#         return self.__mul__(num)
#
#     def __mod__(self, num):
#         return Box3D(*self.__make_calc(num, mod))
#
#     def __floordiv__(self, num):
#         return Box3D(*self.__make_calc(num, floordiv))

# Variant 4
# class Box3D:
#     def __init__(self, width, height, depth):
#         self.width = width
#         self.height = height
#         self.depth = depth
#
#     def do(self, fname, oth):
#         return Box3D(*([getattr(self.__dict__[i], fname)(oth.__dict__[i]
#                                                          if type(oth) is Box3D else oth)
#                         for i in self.__dict__]))
#
#     def __add__(self, other):
#         return self.do('__add__', other)
#
#     def __mul__(self, other):
#         return self.do('__mul__', other)
#
#     def __rmul__(self, other):
#         return self.do('__rmul__', other)
#
#     def __sub__(self, other):
#         return self.do('__sub__', other)
#
#     def __floordiv__(self, other):
#         return self.do('__floordiv__', other)
#
#     def __mod__(self, other):
#         return self.do('__mod__', other)


# Task 10
class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    def __call__(self, matrix, *args, **kwargs):
        len_v, len_h = len(matrix), len(matrix[0])
        if type(matrix) != list or \
                any(len(row) != len_h for row in matrix) or\
                any(type(x) not in (int, float) for row in matrix for x in row):
            raise ValueError("Неверный формат для первого параметра matrix.")
        res = []
        i = 0
        while i + self.size[0] <= len_v:
            res.append([])
            j = 0
            while j + self.size[1] <= len_h:
                res[len(res)-1].append(self.get_max(matrix, i, j))
                j += self.step[1]
            i += self.step[0]
        return res

    def get_max(self, mtx, i, j):
        return max(max(row[j:j+self.size[1]]) for row in mtx[i:i+self.size[0]])


mtrx = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]]
mp = MaxPooling()
print(mp(mtrx))
mp = MaxPooling(step=(1, 1), size=(3, 3))
print(mp(mtrx))
mp = MaxPooling(step=(2, 2), size=(1, 1))
print(mp(mtrx))
