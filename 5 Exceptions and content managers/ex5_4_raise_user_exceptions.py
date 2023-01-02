# 5.4 Инструкция raise и пользовательские исключения

# Вызов исключения
# print("Куда ты скачешь, гордый конь,")
# print("И где опустишь ты копыта?")
# print("О мощный властелин судьбы!")
# raise ZeroDivisionError("Деление на ноль")
# print("Не так ли ты над самой бездной")
# print("На высоте, уздой железной")
# print("Россию поднял на дыбы?")

# Эквивалент
print("Куда ты скачешь, гордый конь,")
print("И где опустишь ты копыта?")
print("О мощный властелин судьбы!")
# e = ZeroDivisionError("Деление на ноль")
# raise e
print("Не так ли ты над самой бездной")
print("На высоте, уздой железной")
print("Россию поднял на дыбы?")
print()

# Объявление raise "Деление на ноль"
# вызовет ошибку TypeError, т. к. исключения должны наследоваться от класса BaseException


# Генерация пользовательского исключения с помощью метода raise от класса Exception
class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f"печать: {str(data)}")

    def send_data(self, data):
        if not self.send_to_print(data):
            raise Exception("Принтер не отвечает")

    def send_to_print(self, data):
        return False


p = PrintData()

# обработка ошибки
try:
    p.print(123)
except Exception as e:
    print("принтер не отвечает")


# Можно создать пользовательский класс исключений
class ExceptionPrintSendData(Exception):
    """Класс исключения при отправке данных принтеру"""


class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f"печать: {str(data)}")

    def send_data(self, data):
        if not self.send_to_print(data):
            raise ExceptionPrintSendData("Принтер не отвечает")

    def send_to_print(self, data):
        return False


p = PrintData()
try:
    p.print(123)
except ExceptionPrintSendData as e:
    print(e)


# Кастомизация пользовательского класса исключения (расширение функционала)
class ExceptionPrintSendData(Exception):
    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"Ошибка: {self.message}"


p = PrintData()
try:
    p.print(123)
except ExceptionPrintSendData as e:
    print(e)


# Иерархия классов исключений
class ExceptionPrint(Exception):
    pass


class ExceptionPrintSendData(ExceptionPrint):
    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"Ошибка: {self.message}"


p = PrintData()
try:
    p.print(123)
except ExceptionPrintSendData as e:
    print(e)
except ExceptionPrint:
    print("Общая ошибка печати")


print("""
Задачи""")


# Task 4
class StringException(Exception):
    pass


class NegativeLengthString(StringException):
    pass


class ExceedLengthString(StringException):
    pass


try:
    raise NegativeLengthString
except NegativeLengthString:
    print("NegativeLengthString")
except ExceedLengthString:
    print("ExceedLengthString")
except StringException:
    print("StringException")


# Task 5
class PrimaryKeyError(Exception):
    def __init__(self, **kwargs):
        if not kwargs or type(kwargs) != dict:
            self.st = "Первичный ключ должен быть целым неотрицательным числом"
        else:
            k = list(kwargs.keys())[0]
            self.st = f"Значение первичного ключа {k} = {kwargs.get(k)} недопустимо"

    def __str__(self):
        return self.st


try:
    raise PrimaryKeyError(id=-10.5)
except PrimaryKeyError as e:
    print(e)
