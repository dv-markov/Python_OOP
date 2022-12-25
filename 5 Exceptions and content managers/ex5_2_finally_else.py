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
# res = None
# try:
#     res = sum(map(int, s1))
# except ValueError:
#     try:
#         res = sum(map(float, s1))
#     except ValueError:
#         res = "".join(s1)
# finally:
#     print(res)


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

