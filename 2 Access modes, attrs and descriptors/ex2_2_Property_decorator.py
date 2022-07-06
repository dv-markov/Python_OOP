# 2.2 Свойства property. Декоратор @property

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    age = property(get_age, set_age)


p = Person('Sergey', 20)
p.set_age(35)
print(p.get_age())

# при обращении к объектам класса property происходит автоматический вызов соответствующих функций
# вызов первой функции - геттер
a = p.age
print(a)

# вызов второй функции - сеттер
p.age = 36

print(p.age, p.get_age())
print(p.__dict__)

# Если в классе задан атрибут свойство, в первую очередь будет вызван именно он
# Даже если в локальном экземпляре класса есть свойство с таким же именем
p.__dict__['age'] = 'age in object p'
p.age = 99
print(p.age, p.__dict__)

# Приоритет объекта property выше, чем при обращении к локальным экземплярам класса
# Объект property использовать удобнее, чем стандартные геттеры и сеттеры

x = property()
# Объект класса property имеет 3 встроенных метода, это декораторы
# x.setter()
# x.getter()
# x.deleter()
print()


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    age = property()
    age = age.setter(set_age)
    age = age.getter(get_age)


p = Person('Sergey', 20)
p.age = 35
print(p.age, p.__dict__)
print()


# декораторы можно прописать через @
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @age.deleter
    def age(self):
        del self.__age


p = Person('Sergey', 10)
p.age = 20
print(p.age, p.__dict__)
del p.age
print(p.__dict__)

