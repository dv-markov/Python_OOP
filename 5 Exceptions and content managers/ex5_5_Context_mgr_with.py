# 5.5 Менеджеры контекстов. Оператор with

# Вариант с классическим try/except
fp = None
try:
    fp = open("myfile.txt")
    for t in fp:
        print(t)
except Exception as e:
    print(e)
finally:
    if fp is not None:
        fp.close()

# Вариант с менеджером контекста with
try:
    with open("myfile.txt") as fp:
        for t in fp:
            print(t)
except Exception as e:
    print(e)

# Менеджер контекста with - это класс
# В при вызове срабатывает два метода:
# __enter__() - в момент создания объекта менеджера контекста
# __exit__() - в момент завершения работы менеджера контекста
# или возникновения исключения (подобно блоку finally)
# as - опциональная часть конструкции


# пример - свой класс
class DefendedVector:
    def __init__(self, v):
        self.__v = v

    def __enter__(self):
        self.__temp = self.__v[:]
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v[:] = self.__temp

        return False


v1 = [1, 2, 3]
v2 = [2, 3]
# v2 = [2, 3, 4]

try:
    with DefendedVector(v1) as dv:
        for i, a in enumerate(dv):
            dv[i] += v2[i]
except:
    print("Ошибка")

print(v1)
