# 3.8 Методы __getitem__, __setitem__ и __delitem__

# __getitem__(self, item) - получение значения по ключу item
# __setitem__(self, key, value) - запись значения value по ключу key
# __delitem__(self, key) - удаление элемента по ключу key

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)


s1 = Student("Сергей", [5, 5, 3, 2, 5])
print(s1.marks[2])


# __getitem__
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item <= len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Неверный индекс")


s1 = Student("Иван", [1, 2, 3, 2, 5])
print(s1[2])
# несуществующий индекс вызовет ошибку
# print(s1[20])


# __setitem__
# __delitem__
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item <= len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Неверный индекс")

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым неотрицательным числом")

        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None]*off)

        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Индекс должен быть целым неотрицательным числом")

        del self.marks[key]


s1 = Student("Петр", [5, 5, 3, 2, 5])
s1[4] = 4
s1[10] = 4
print(s1.marks)
del s1[2]
print(s1.marks)


print("""
Задачи""")


# Task 2
class Record:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def __chk_indx(self, indx):
        if not isinstance(indx, int) or indx < 0 or indx > len(self.__dict__):
            raise IndexError('неверный индекс поля')

    def __getitem__(self, item):
        self.__chk_indx(item)
        return tuple(self.__dict__.values())[item]

    def __setitem__(self, key, value):
        self.__chk_indx(key)
        setattr(self, tuple(self.__dict__.keys())[key], value)


r = Record(pk=1, title='Python ООП', author='Балакирев')
print(r.__dict__)
print(r[0])
r[0] = 2 # доступ к полю pk
r[1] = 'Супер курс по ООП'
print(r[0], r[1])



