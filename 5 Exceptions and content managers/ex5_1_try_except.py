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


# lst_in = input().split()
s = "1 -5.6 True abc 0 23.56 hello"
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


# Task 9
class Triangle:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
        self.__verify_triangle(a, b, c)

    def __setattr__(self, key, value):
        if type(value) not in (int, float) or value <= 0:
            raise TypeError('стороны треугольника должны быть положительными числами')
        super().__setattr__(key, value)

    @staticmethod
    def __verify_triangle(a, b, c):
        if 2 * max(a, b, c) >= a + b + c:
            raise ValueError('из указанных длин сторон нельзя составить треугольник')


def get_triangle(args):
    try:
        return Triangle(*args)
    except:
        return None


input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]
lst_tr = list(filter(None, map(get_triangle, input_data)))

print(lst_tr)


# Task 10
class Validator:
    VALIDATOR_TYPE = None

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if type(value) != self.VALIDATOR_TYPE or not (self.min_value <= value <= self.max_value):
            raise ValueError('значение не прошло валидацию')


class FloatValidator(Validator):
    VALIDATOR_TYPE = float


class IntegerValidator(Validator):
    VALIDATOR_TYPE = int


def is_valid(lst, validators):
    lst_valid = []
    for x in lst:
        for val in validators:
            try:
                val(x)
                lst_valid.append(x)
                break
            except ValueError:
                continue
    return lst_valid


fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])  # [1, 4.5]
print(lst_out)


# Variant 1 - my_refactored
def is_valid(lst, validators):
    def verify_number(x):
        for v in validators:
            try:
                v(x)
                return True
            except:
                continue
        return False
    return list(filter(verify_number, lst))


print(is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], [fv, iv]))


# Varaint 2 - Vittorio Zanzara
# def is_valid(lst, validators):
#     def validate(x):
#         for val in validators:
#             try: return val(x)
#             except ValueError: continue
#         return False
#     return [*filter(validate, lst)]

# Variant 3 - Mikhail Iofik (без try/except)
# def is_valid(lst, validators):
#     return [item for item in lst if any(validator(item, True) for validator in validators)]



