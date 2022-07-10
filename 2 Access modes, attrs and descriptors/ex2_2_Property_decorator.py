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

pr = property()
# Объект класса property имеет 3 встроенных метода, это декораторы
# pr.setter()
# pr.getter()
# pr.deleter()
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


print("""
Задачи""")


# Task 4
class Car:
    def __init__(self):
        self.__model = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if type(model) == str and 2 <= len(model) <= 100:
            self.__model = model


car = Car()
print(car.model)
car.model = "Toyota"
print(car.model)


# Task 5
class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title if self.__check_title(title) else None
        self.__width = width if self.__check_size(width) else None
        self.__height = height if self.__check_size(height) else None

    @staticmethod
    def __check_title(title):
        return type(title) == str

    @staticmethod
    def __check_size(size):
        return type(size) == int and 0 <= size <= 10_000

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if self.__check_size(width):
            self.__width = width
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if self.__check_size(height):
            self.__height = height
            self.show()

    def show(self):
        print(f"{self.__title}: {self.width}, {self.height}")


wnd = WindowDlg('Title 1', 700, 500)
print(wnd.__dict__)
wnd.show()
wnd.width = 300
wnd.height = 150


# Task 6
class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, nxt):
        if isinstance(nxt, StackObj) or nxt is None:
            self.__next = nxt


class Stack:
    def __init__(self):
        self.top = None
        self.last = None

    def push(self, obj):
        if not self.top:
            self.top = obj
        if self.last:
            self.last.next = obj
        self.last = obj

    def pop(self):
        if self.top is None:
            return None
        elif self.top == self.last:
            current_obj = self.last
            self.top = self.last = None
            return current_obj
        else:
            prev_obj = None
            current_obj = self.top
            while current_obj != self.last:
                prev_obj = current_obj
                current_obj = current_obj.next
            prev_obj.next = None
            self.last = prev_obj
            return current_obj

    def get_data(self):
        obj = self.top
        res = []
        while obj:
            res.append(obj.data)
            obj = obj.next
        return res


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
print(st.pop().data)
# print(st.pop().data)
# print(st.pop().data)
# print(st.pop())
print()

res = st.get_data()    # ['obj1', 'obj2']
print(res)


# Task 7
class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        self.x = x
        self.y = y

    def __check_coord(self, c):
        return type(c) in (int, float) and self.MIN_COORD <= c <= self.MAX_COORD

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if self.__check_coord(x):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if self.__check_coord(y):
            self.__y = y

    @staticmethod
    def norm2(vector):
        if isinstance(vector, RadiusVector2D):
            return vector.x**2 + vector.y**2


v1 = RadiusVector2D()        # радиус-вектор с координатами (0; 0)
print(v1.__dict__)
v2 = RadiusVector2D(1)       # радиус-вектор с координатами (1; 0)
print(v2.__dict__)
v3 = RadiusVector2D(1, 2)    # радиус-вектор с координатами (1; 2)
v3.x = 'asdf'
v3.y = -5000
print(v3.__dict__)
print(RadiusVector2D.norm2(v1))
print(v2.norm2(v2))
print(v2.norm2(v3))

r5 = RadiusVector2D(-102, 2000)
print(r5.__dict__)


# Task 8
print('\n', "Decision Trees", sep='')


class TreeObj:
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, l):
        if isinstance(l, TreeObj):
            self.__left = l

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, r):
        if isinstance(r, TreeObj):
            self.__right = r


class DecisionTree:
    @classmethod
    def predict(cls, root, x):
        obj = root
        while obj.left or obj.right:
            if x[obj.indx] == 1:
                obj = obj.left
            else:
                obj = obj.right
        return obj.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj


root = DecisionTree.add_obj(TreeObj(0))
print('root node: ', root)
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

x = [1, 1, 0]
res = DecisionTree.predict(root, x)  # будет программистом
print(res)

x = [0, 0, 1]
res1 = DecisionTree.predict(root, x)  #не все потеряно
print(res1)


# Task 9
class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PathLines:
    def __init__(self, *args):
        self.line_list = list(args)

    def get_path(self):
        return self.line_list

    def get_length(self):
        return sum(self.__line_len(i) for i in range(len(self.line_list)))

    def add_line(self, line):
        if isinstance(line, LineTo):
            self.line_list.append(line)

    def __line_len(self, i):
        lst = self.line_list
        x0 = lst[i-1].x if i > 0 else 0
        x1 = lst[i].x
        y0 = lst[i-1].y if i > 0 else 0
        y1 = lst[i].y
        return ((x1 - x0)**2 + (y1 - y0)**2)**0.5


p0 = PathLines(1, 2, 3)
print(p0.get_path())
p = PathLines(LineTo(10, 20), LineTo(10, 30))
dist = p.get_length()
print(dist)
p.add_line(LineTo(20, -10))
dist = p.get_length()
print(dist)


# Variant 2
class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self, x0, y0):
        return ((self.x - x0) ** 2 + (self.y - y0) ** 2) ** 0.5


class PathLines:
    def __init__(self, *points):
        self.__points = list(points)

    def add_line(self, point):
        self.__points.append(point)

    def get_path(self):
        return self.__points

    def get_length(self):
        x = y = length = 0
        for point in self.__points:
            length += point.length(x, y)
            x, y = point.x, point.y
        return length


p = PathLines(LineTo(100, 200), LineTo(10, 30))
dist = p.get_length()
print(dist)
p.add_line(LineTo(20, -10))
dist = p.get_length()
print(dist)


# Task 10
class PhoneBook:
    def __init__(self):
        self.phone_list = []

    def add_phone(self, phone):
        if isinstance(phone, PhoneNumber):
            self.phone_list.append(phone)

    def remove_phone(self, indx):
        if type(indx) == int and indx < len(self.phone_list):
            self.phone_list.pop(indx)

    def get_phone_list(self):
        return self.phone_list


class PhoneNumber:
    def __new__(cls, *args, **kwargs):
        if cls.__is_number(args[0]) and cls.__is_fio(args[1]):
            return super().__new__(cls)
        else:
            print('Ошибка входных данных')

    @staticmethod
    def __is_number(n):
        return type(n) == int and len(str(n)) == 11

    @staticmethod
    def __is_fio(f):
        return type(f) == str

    def __init__(self, number, fio):
        self.number = number
        self.fio = fio


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.remove_phone(0)
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
print(phones)
for ph in phones:
    print(ph.number, ph.fio)
