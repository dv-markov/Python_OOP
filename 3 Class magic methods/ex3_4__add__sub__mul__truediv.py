# 3.4 Методы __add__, __sub__, __mul__, __truediv__

# сложение объекта с числом
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
        return list_n.get_list() if isinstance(list_n, NewList) else list_n

    @staticmethod
    def __subtract_lists(lst1, lst2):
        # return [x for x in lst1 if all(map(lambda y: x is not y, lst2))]
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

# Variant 2
# return NewList(list(filter(lambda x: x not in lst_sub, self.lst)))