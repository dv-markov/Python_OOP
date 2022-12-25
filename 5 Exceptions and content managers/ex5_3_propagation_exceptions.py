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
    def __init__(self, min_length, max_length, chars):
        pass