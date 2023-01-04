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


# Task 6
class DateString:
    def __init__(self, date_string):
        self.d, self.m, self.y = self.__parse_ds(date_string)

    @staticmethod
    def __parse_ds(ds):
        try:
            d, m, y = map(int, ds.split("."))
        except:
            raise DateError("Неверный формат даты")
        if not (0 < d < 32) or not (0 < m < 13) or not (0 < y < 3001):
            raise DateError("Неверный формат даты")
        return d, m, y

    def __str__(self):
        return f"{self.d:02}.{self.m:02}.{self.y:04}"


class DateError(Exception):
    """Ошибка преобразования даты"""


date_string = "1.2.1812"
try:
    ds = DateString(date_string)
except DateError as e:
    print(e)
else:
    print(ds)


# Variant 2 - Анастасия Короткова
# from datetime import datetime
#
# class DateError(Exception):
#     pass
#
# class DateString:
#     def __init__(self, date):
#         try:
#             self.date = datetime.strptime(date, '%d.%m.%Y').strftime('%d.%m.%Y')
#         except ValueError:
#             raise DateError
#
#     def __str__(self):
#         return self.date
#
#
# date_string = input()
# try:
#     print(DateString(date_string))
# except DateError:
#     print("Неверный формат даты")


# Task 7
class CellException(Exception): ...
class CellIntegerException(CellException): ...
class CellFloatException(CellException): ...
class CellStringException(CellException): ...


class Cell:
    def __init__(self):
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        self._verify_value(val)
        self.__value = val

    def _verify_value(self, val):
        raise NotImplementedError('Метод должен быть переопределен в дочернем классе')


class CellInteger(Cell):
    def __init__(self, min_value, max_value):
        super().__init__()
        self._min_value = min_value
        self._max_value = max_value

    def _verify_value(self, val):
        if type(val) != int or not self._min_value <= val <= self._max_value:
            raise CellIntegerException('значение выходит за допустимый диапазон')


class CellFloat(Cell):
    def __init__(self, min_value, max_value):
        super().__init__()
        self._min_value = min_value
        self._max_value = max_value

    def _verify_value(self, val):
        if type(val) not in (int, float) or not self._min_value <= val <= self._max_value:
            raise CellFloatException('значение выходит за допустимый диапазон')


class CellString(Cell):
    def __init__(self, min_length, max_length):
        super().__init__()
        self._min_length = min_length
        self._max_length = max_length

    def _verify_value(self, val):
        if type(val) != str or not self._min_length <= len(val) <= self._max_length:
            raise CellStringException('длина строки выходит за допустимый диапазон')


class TupleData:
    def __init__(self, *args):
        self.__verify_cells(args)
        self._cells = args

    @staticmethod
    def __verify_cells(args):
        if any(not isinstance(x, Cell) for x in args):
            raise TypeError('Аргументы должны быть объектами класса Cell или его дочерних классов')

    def __verify_indx(self, indx):
        if indx not in range(len(self._cells)):
            raise IndexError('Индекс ячейки выходит за допустимый диапазон')

    def __getitem__(self, item):
        self.__verify_indx(item)
        return self._cells[item].value

    def __setitem__(self, key, value):
        self.__verify_indx(key)
        self._cells[key].value = value

    def __len__(self):
        return len(self._cells)

    def __iter__(self):
        for x in self._cells:
            yield x.value


# эти строчки в программе не менять!
ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")

res = len(ld) # возвращает общее число элементов (ячеек) в объекте ld
print(f"Общее число элементов: {res}")
for d in ld:  # перебирает значения ячеек объекта ld (значения, а не объекты ячеек)
    print(d)

