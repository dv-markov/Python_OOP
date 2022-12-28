# 5.3 Распространение исключений (propagation exceptions)

# стек вызова функций, отображающий распространение исключений
# def func2():
#     return 1 / 0
#
# def func1():
#     return func2()
#
# print('Я к вам пишу - чего же боле?')
# print('Что я могу еще сказать?')
# print('Теперь, я знаю, в вашей воле')
# func1()
# print('Меня презреньем наказать.')
# print('Но вы, к моей несчастной доле')
# print('Хоть каплю жалости храня,')
# print('Вы не оставите меня.')

# обработка исключений в стеке вызова функций на разных уровнях
# уровень main()
def func2():
    return 1 / 0


def func1():
    return func2()


def poem_pt1():
    print('Я к вам пишу - чего же боле?')
    print('Что я могу еще сказать?')
    print('Теперь, я знаю, в вашей воле')


def poem_pt2():
    print('Меня презреньем наказать.')
    print('Но вы, к моей несчастной доле')
    print('Хоть каплю жалости храня,')
    print('Вы не оставите меня.')


poem_pt1()
try:
    func1()
except:
    print("func1 error")
poem_pt2()
print()


# На уровне func1
def func2():
    return 1 / 0


def func1():
    try:
        return func2()
    except:
        print("func1 error")


poem_pt1()
func1()
poem_pt2()
print()


# На уровне func2
def func2():
    try:
        return 1 / 0
    except:
        print("func2 error")


def func1():
    try:
        return func2()
    except:
        print("func1 error")


poem_pt1()
func1()
poem_pt2()
print()


# как только исключение обрабатывается, дальше оно уже не всплывает
# если обработано исключение func2 error, то func1 error уже не появится
# можно обрабатывать исключения на разных уровнях стека вызова

# обычно на уровне критических функций генерируются исключения,
# а обрабатываются они уже на более глобальных уровнях
# это называется распространение исключений (exception propagation)
# и позволяет создавать гибкий и безопасный код


# Task 3
# Variant 0 - my
# def input_int_numbers(line):
#     lst = []
#     for char in line.split():
#         try:
#             lst.append(int(char))
#         except ValueError:
#             raise TypeError('все числа должны быть целыми')
#     return tuple(lst)
#
#
# while True:
#     s = input()
#     try:
#         res = input_int_numbers(s)
#         print(*res)
#         break
#     except TypeError:
#         continue

# Variant 1 - my refactored
# def input_int_numbers(line):
#     try:
#         return map(int, line.split())
#     except ValueError:
#         raise TypeError('все числа должны быть целыми')
#
#
# while True:
#     try:
#         print(*input_int_numbers(input()))
#         break
#     except (ValueError, TypeError):
#         continue


# Task 4
class ValidatorString:
    def __init__(self, min_length: int, max_length: int, chars: str):
        self.min_length = min_length
        self.max_length = max_length
        self.chars = set(chars)

    def is_valid(self, string):
        if not self.min_length <= len(string) <= self.max_length \
                or (self.chars and not self.chars.intersection(string)):
            raise ValueError('недопустимая строка')


class LoginForm:
    def __init__(self, login_validator: ValidatorString, password_validator: ValidatorString):
        self.login_validator = login_validator
        self.password_validator = password_validator
        self._login = self._password = None

    def form(self, request: dict):
        self.verify_request(request)
        login = request.get('login')
        password = request.get('password')
        self.login_validator.is_valid(login)
        self.password_validator.is_valid(password)
        self._login = login
        self._password = password

    @staticmethod
    def verify_request(req):
        if not isinstance(req, dict) or \
                type(req.get('login')) != str or type(req.get('password')) != str:
            raise TypeError('в запросе отсутствует логин или пароль')


login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
# login, password = input().split()
login, password = 'sergey balakirev!'.split()

try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)


# Task 5
class Test:
    def __init__(self, descr):
        self.__verify_descr(descr)
        self.descr = descr

    @staticmethod
    def __verify_descr(d):
        min_len = 10
        max_len = 10_000
        if not isinstance(d, str) or not min_len <= len(d) <= max_len:
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')

    def

