# 1.3 Классы и объекты. Атрибуты классов и объектов

# имя класса принято начинать с заглавной буквы
# заглушка класса с оператором pass
# class Point:
#     pass

# класс - это пространство имен
class Point:
    # строка-описание
    """Класс для представления координат точек на плоскости"""
    # также можно задавать строку-описание в простых двойных кавычках
    # атрибуты (свойства) класса
    color = 'red'
    circle = 2


# просмотр и изменение свойств класса
print(Point.color)
print(Point.circle)
Point.color = 'black'
print(Point.color)

# вывод всех атрибутов (свойств) класса
print(Point.__dict__)

# создание объекта (экземпляра) класса
a = Point()
b = Point()

# проверка типа объекта
# имя класса - тип данных
print(type(a))
print(type(a) == Point)
print(isinstance(a, Point))

# атрибуты класса общие для всех его экземпляров
Point.circle = 1
print(a.__dict__)
print(b.__dict__)

# объекты создают пространство имен, но оно пустое до явного изменения или создания свойств
# пока свойства объекта не изменены, они ссылаются на атрибуты класса
# после изменения свойства объект обретает собственное свойство (переменную) в своем пространстве имен
a.color = 'green'
print(a.__dict__)

# по аналогии можно создавать новые аттрибуты в классе
# они будут наследованы для всех объектов класса
Point.type_pt = 'disc'
print(Point.__dict__)

# также можно делать это с помощью метода setattr
setattr(Point, 'prop', 1)
print(Point.__dict__)

# с помощью этого же метода можно менять атрибуты
setattr(Point, 'type_pt', 'square')
print(Point.__dict__)

# чтение значения класса / экземпляра класса
# выдает ошибку при обращении к несуществующим атрибутам
print(Point.circle)
res = a.color
print(res)

# специальная функция для чтения свойств - getattr
# можно указать третий аргумент функции для вывода значения по умолчанию (если атрибут не найден)
print(getattr(Point, 'color'))
print(getattr(Point, 'xyz', False))

# удаление атрибутов
del Point.prop
print(Point.__dict__)
# удалять несуществующий атрибут нельзя
# del Point.prop  # второй раз выдаст ошибку

# проверка атрибутов
print(hasattr(Point, 'circle'))
# через пространство имен можно получить доступ к атрибуту,
# но не видно, собственный это атрибут экземпляра, или атрибут класса
print(hasattr(a, 'color'))
print(hasattr(b, 'color'))

if hasattr(Point, 'color'):
    del Point.color
print(Point.__dict__)
# при удалении атрибутов класса собственные атрибуты экземпляра остаются
print(a.__dict__)

# второй вариант удаления
delattr(Point, 'type_pt')
# несуществующий атрибут также нельзя удалить
# delattr(Point, 'type_pt')
print(Point.__dict__)

setattr(Point, 'color', 'red')
print(Point.__dict__)
print(b.__dict__)
# hasattr не различает атрибут объекта и класса,
# поэтому попытка удаления у объекта свойства, которого нет в его пространстве имен, приведет к ошибке
# удаление атрибута объекта происходит в его пространстве имен
# if hasattr(b, 'color'):
#     del b.color

# при отсутствии собственного атрибута, объект будет ссылаться на атрибут вышестоящего класса

# задача создания объектов на плоскости
# координаты - независимые
# свойства color и circle - общие
a.x = 1
a.y = 2
b.x = 10
b.y = 20

# документация
print(Point.__doc__)


print("""
Задачи""")


# Task 3
class DataBase:
    pk = 1
    title = "Классы и объекты"
    author = "Сергей Балакирев"
    views = 14356
    comments = 12


print(DataBase.__dict__)
# Аннотация типов
# def foo(n: int, condition: bool) -> int:
#     pass


# Task 4
class Goods:
    title = "Мороженое"
    weight = 154
    tp = "Еда"
    price = 1024


# при обращении напрямую по имени (не через переменную) лучше использовать обычный доступ к свойству
# setattr(Goods, 'price', 2048)
# setattr(Goods, 'inflation', 100)
Goods.price = 2048
Goods.inflation = 100
print(Goods.__dict__)

# Variant 2
class Goods:
    title = "Мороженое"
    weight = 154
    tp = "Еда"
    price = 1024
[setattr(Goods, *attr) for attr in (('price', 2048), ('inflation', 100))]


# Task 5
class Car:
    pass


[setattr(Car, *attr) for attr in (('model', "Тойота"), ('color', "Розовый"), ('number', "П111УУ77"))]
print(Car.__dict__)
print(Car.__dict__.get('color'))

# Variant 2
# class Car:
#     pass
# d = {
#     'model': "Тойота",
#     'color': "Розовый",
#     'number': "О111АА77"
# }
# [setattr(Car,k,v) for k,v in d.items()]
# print(Car.__dict__['color'])


# Task 6
class Notes:
    uid = 1005435
    title = "Шутка"
    author = "И.С. Бах"
    pages = 2


print(getattr(Notes, 'author', None))

# Variant 2
# d = {'uid': 1005435,
#      'title': "Шутка",
#      'author': "И.С. Бах",
#      'pages': 2}
# class Notes:
#     pass
# for key, value in d.items():
#     setattr(Notes, key, value)
# print(getattr(Notes, 'author'))


# Task 7
class Dictionary:
    rus = "Питон"
    eng = "Python"


print(getattr(Dictionary, 'rus_word', False))


# Task 8
class TravelBlog:
    total_blogs = 0


tb1 = TravelBlog()
tb1.name = "Франция"
tb1.days = 6
TravelBlog.total_blogs += 1

tb2 = TravelBlog()
tb2.name = "Италия"
tb2.days = 5
TravelBlog.total_blogs += 1

print(TravelBlog.__dict__, tb1.__dict__, tb2.__dict__, sep='\n')

# Variant 2
# class TravelBlog:
#     total_blogs = 0
#
#     @classmethod
#     def count_blog(cls):
#         cls.total_blogs += 1
#
#     def __init__(self, name, days):
#         self.name = name
#         self.days = days
#         self.count_blog()
#
# tb1 = TravelBlog('Франция', 6)
# tb2 = TravelBlog('Италия', 5)
# print(TravelBlog.total_blogs)


# Task 9
class Figure:
    type_fig = 'ellipse'
    color = 'red'


fig1 = Figure()
fig1.start_pt = (10, 5)
fig1.end_pt = (100, 20)
fig1.color = 'blue'
del fig1.color
print(*fig1.__dict__.keys())


# Task 10
class Person:
    name = "Сергей Балакирев"
    job = "Программист"
    city = "Москва"


p1 = Person()
print('job' in p1.__dict__)
