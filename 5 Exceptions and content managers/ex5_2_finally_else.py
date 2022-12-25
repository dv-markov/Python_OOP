# 5.2 Обработка исключений. Блоки finally и else

# работа с объектами исключений, оператор "as"
# try:
#     x, y = map(int, input().split())
#     res = x / y
# except ZeroDivisionError as z:
#     print(z)
# except ValueError as z:
#     print(z)

# else - штатное завершение работы оператора try
# не срабатывает при возникновении исключений
# try:
#     x, y = map(int, input().split())
#     res = x / y
# except ZeroDivisionError as z:
#     print(z)
# except ValueError as z:
#     print(z)
# else:
#     print("Исключений не произошло")


# блок finally выполняется всегда в последнюю очередь
# try:
#     x, y = map(int, input().split())
#     res = x / y
# except ZeroDivisionError as z:
#     print(z)
# except ValueError as z:
#     print(z)
# finally:
#     print("блок Finally выполняется всегда")


# Пример реального использования блока finally
try:
    f = open("myfile.txt")
    f.write("hello")
except FileNotFoundError as z:
    print(z)
except:
    print("Другая ошибка")
finally:
    if f:
        f.close()
        print("Файл закрыт")

# На практике для работы с файлами используется менеджер контекста with
# Функционал тот же - закрыть файл после использования
# Обработка ошибок - с помощью тех же блоков try и except
try:
    with open("myfile.txt") as f:
        f.write("hello")
except FileNotFoundError as z:
    print(z)
except:
    print("Другая ошибка")

# Работа блока finally связана с обработкой исключений внутри функции
# она происходит до срабатывания оператора return
# def get_values():
#     try:
#         x, y = map(int, input().split())
#         return x, y
#     except ValueError as z:
#         print(z)
#         return 0, 0
#     finally:
#         print("finally выполняется до return")
#
# x, y = get_values()
# print(x, y)


# Вложенные блоки try / except
# try:
#     x, y = map(int, input().split())
#     try:
#         res = x / y
#     except ZeroDivisionError:
#         print("Деление на ноль")
# except ValueError as z:
#     print(z)


# Вариант 2 для вложенных блоков
# def div(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "Деление на ноль"
#
#
# res = 0
# try:
#     x, y = map(int, input().split())
#     res = div(x, y)
# except ValueError as z:
#     print(z)
#
# print(res)


print("""
Задачи""")

# Task 4
# s1 = input().split()
s1 = "8 11".split()
res = None
try:
    res = sum(map(int, s1))
except ValueError:
    try:
        res = sum(map(float, s1))
    except ValueError:
        res = "".join(s1)
finally:
    print(res)


# Вариант 2 - Михаил Орлов
# a, b = input().split()
# try:
#     a, b = map(int, (a, b))
# except ValueError:
#     try:
#         a, b = map(float, (a, b))
#     except ValueError:
#         pass
# finally:
#     print(a + b)

# Вариант 3 - Андрей Паршин
# def val(q):
#     for F in (int, float):
#         try:
#             return F(q)
#         except:
#             continue
#     return q
#
#
# a, b = map(val, input().split())
# print(a + b)


# Task 5
# Variant 0 - my
# class Point:
#     def __init__(self, x=0, y=0):
#         self._x = x
#         self._y = y
#
#     @property
#     def x(self):
#         return self._x
#
#     @property
#     def y(self):
#         return self._y
#
#
# def get_number(x):
#     for f in (int, float):
#         try:
#             return f(x)
#         except ValueError:
#             continue
#     return x
#
#
# a, b = map(get_number, input().split())
# pt = Point(a, b) if all(map(lambda x: type(x) in (int, float), (a, b))) else Point()
# print(f"Point: x = {pt.x}, y = {pt.y}")


# Variant 1 - my refactored
class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __repr__(self):
        return f"{self.__class__.__name__}: x = {self._x}, y = {self._y}"


def get_number(x):
    for f in (int, float):
        try:
            return f(x)
        except ValueError:
            continue
    raise ValueError


try:
    # pt = Point(*map(get_number, input().split()))
    pt = Point(*map(get_number, "123 321".split()))
except:
    pt = Point()
finally:
    print(pt)


# Task 6 - finally выполняется перед return, но не меняет результата, возвращаемого в return
def get_div(x, y):
    try:
        res = x / y
        return res
    except ZeroDivisionError:
        res = 100
        return res
    finally:
        res = -1
        print(f"finally: {res}")


print(get_div(3, 5))


# Task 7
def get_loss(w1, w2, w3, w4):
    try:
        y = w1 // w2
    except ZeroDivisionError:
        return "деление на ноль"
    else:
        return 10 * y - 5 * w2 * w3 + w4


# Task 8
class Rect:
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def __setattr__(self, key, value):
        if type(value) not in (int, float) or key in ('_width', '_height') and value <= 0:
            raise ValueError('некорректные координаты и параметры прямоугольника')
        super().__setattr__(key, value)

    def is_collision(self, rect):
        def axis_collision(coord1, d1, coord2, d2):
            return coord2 <= coord1 <= coord2 + d2 or coord1 <= coord2 <= coord1 + d1

        if not isinstance(rect, self.__class__):
            raise ValueError(f'Аргумент должен быть объектом класса {self.__class__.__name__}')
        if axis_collision(self._x, self._width, rect._x, rect._width) and \
                axis_collision(self._y, self._height, rect._y, rect._height):
            raise TypeError('прямоугольники пересекаются')


def check_rectangle_collision(r0, indx, lst):
    for r in lst[:indx] + lst[indx+1:]:
        try:
            r0.is_collision(r)
        except TypeError:
            return False
    return True


# r1 = Rect(100, 100, 100, 100)
# r2 = Rect(150, 0, 10, 20)
# r1.is_collision(r2)


lst_in = """0; 0; 5; 3
6; 0; 3; 5
3; 2; 4; 4
0; 8; 8; 1"""
lst_rect = [Rect(*map(int, line.split("; "))) for line in lst_in.splitlines()]
lst_not_collision = [x for i, x in enumerate(lst_rect) if check_rectangle_collision(x, i, lst_rect)]

print(lst_not_collision)
for r in lst_not_collision:
    print(r.__dict__)


# тесты
# r = Rect(1, 2, 10, 20)
# assert r._x == 1 and r._y == 2 and r._width == 10 and r._height == 20, \
#     "неверные значения атрибутов объекта класса Rect"
#
# r2 = Rect(1.0, 2, 10.5, 20)
#
# try:
#     r2 = Rect(0, 2, 0, 20)
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError при создании объекта Rect(0, 2, 0, 20)"
#
#
# assert len(lst_rect) == 4, "список lst_rect содержит не 4 элемента"
# assert len(lst_not_collision) == 1, "неверное число элементов в списке lst_not_collision"
#
# def not_collision(rect):
#     for x in lst_rect:
#         try:
#             if x != rect:
#                 rect.is_collision(x)
#         except TypeError:
#             return False
#     return True
#
# f = list(filter(not_collision, lst_rect))
# assert lst_not_collision == f, "неверно выделены не пересекающиеся прямоугольники, " \
#                                "возможно, некорректно работает метод is_collision"
#
# r = Rect(3, 2, 2, 5)
# rr = Rect(1, 4, 6, 2)
#
# try:
#     r.is_collision(rr)
# except TypeError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение TypeError при вызове метода is_collision() " \
#                   "для прямоугольников Rect(3, 2, 2, 5) и Rect(1, 4, 6, 2)"
