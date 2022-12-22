# 5.1 Введение в обработку исключений. Блоки try / except

print('Я к вам пишу - чего же боле?')
print('Что я могу еще сказать?')
print('Теперь, я знаю, в вашей воле')
#  1 / 0  # исключение при компиляции
# 1 / 0  # исключение в момент выполнения
# print(a)  # исключение в момент выполнения
print('Меня презреньем наказать.')
print('Но вы, к моей несчастной доле')
print('Хоть каплю жалости храня,')
print('Вы не оставите меня.')

# Обработка исключений - исключения в момент исполнения
# Не применимо к исключениям в момент компиляции (для того, чтобы их избежать, надо писать правильный код)
# try:
#     f = open("myfile2.txt")
# except FileNotFoundError:
#     print("Невозможно открыть файл")
#
# try:
#     x, y = map(int, input().split())
#     res = x / y
# except ValueError:
#     print("Ошибка типа данных")
# except ZeroDivisionError:
#     print("Деление на ноль")
# # Блоков except может быть сколько угодно, они отрабатывают в зависимости от типа ошибки
# # Можно вводить типы исключений через запятую
# except (ValueError, ZeroDivisionError):
#     print("Ошибка типа данных или деления на ноль")

# Классы исключений, см. Exception_hierarchy
# ZeroDivisionError - дочерний класс ArithmeticError
# try:
#     x, y = map(int, input().split())
#     res = x / y
# except ArithmeticError:
#     print("Арифметическая ошибка")

# try:
#     x, y = map(int, input().split())
#     res = x / y
# except ValueError:
#     print("Ошибка типа данных")
# except Exception:
#     print("Деление на ноль")

# Сначала прописываются блоки со специализированными исключениями, потом с общими (базовыми)
# Иначе специализированные исключения отлавливаться не будут
# try:
#     x, y = map(int, input().split())
#     res = x / y
# except Exception:
#     print("Деление на ноль")
# except ValueError:
#     print("Ошибка типа данных")

# Наиболее общий блок
try:
    x, y = 1, 0
    res = x / y
except:
    print("Общее исключение")

print("Штатное завершение")

print("""
Задачи""")


# Task 5
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y


pt = Point(1, 2)
# pt.z = 4

try:
    print(getattr(pt, 'z'))
except AttributeError:
    print("Атрибут с именем z не существует")


# Task 7
def verify_int(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


s = "1 -5.6 2 abc 0 False 22.5 hello world"
lst_in = s.split()
filtered_list = filter(verify_int, lst_in)
print(sum(map(int, filtered_list)))

# Task 8
def get_number(x):
    try:
        return int(x)
    except ValueError:
        try:
            return float(x)
        except Exception:
            return x

# print(get_number('123.0l') + 3)
s = "1 -5.6 True abc 0 23.56 hello"
# lst_in = input().split()
lst_in = s.split()

lst_out = list(map(get_number, lst_in))
print(lst_out)


# Variant 2 - Fedor Kuzmnenko
def convert(value):
    for T in (int, float, str):
        try:
            return T(value)
        except:
            pass

