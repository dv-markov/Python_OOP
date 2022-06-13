# 1.4 Методы классов. Параметр self

# свойства - данные (существительные)
# методы - действия (глаголы)

class Point:
    color = 'red'
    circle = 2

    def set_coords():
        print("вызов метода set_coords")


print(Point.set_coords)
Point.set_coords()

pt = Point()
print(pt.set_coords)
# вызов метода экземпляра класса без аргумента self в описании класса выдает ошибку
# pt.set_coords()


# поэтому при объявлении метода внутри класса нужно всегда указывать параметр self
class Point2:
    color = 'red'
    circle = 2

    def set_coords(self):
        print("вызов метода set_coords" + str(self))


# тогда все будет работать
pt2 = Point2()
print(pt2.set_coords)
# ссылка self ведет на объект pt2, через который был вызван данный метод
pt2.set_coords()

# при вызове метода из класса нужно передавать ссылку на экземпляр класса
# это эквивалент записи pt2.set_coords()
Point2.set_coords(pt2)


# через параметр self можно задавать локальные свойства объекта класса
class Point3:
    color = 'red'
    circle = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)


pt3 = Point3()
pt3.set_coords(1, 2)
print(pt3.__dict__)

pt4 = Point3()
pt4.set_coords(20, 30)
print(pt4.__dict__)

print(pt3.get_coords())

# доступ к методам класса можно получить через функцию getattr
# но обычно используется синтаксис через точку
f = getattr(pt3, "get_coords")
print(f)
print(f())

print()
print()

