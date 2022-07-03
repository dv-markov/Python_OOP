# 1.7 Методы класса (classmethod) и статические методы (staticmethod)

class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        # if Vector.validate(x) and Vector.validate(y):
        #     self.x = x
        #     self.y = y

        # аналогичная запись (более универсальный вариант, устойчивый к изменению имени класса):
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

        print(self.norm2(self.x, self.y))

    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        return x*x + y*y  # квадратичная норма


# объявление и вызов методов
# вариант 1
v = Vector(1, 2)
res = v.get_coord()
print(res)

# вариант 2
v2 = Vector(3, 4)
res = Vector.get_coord(v2)
print(res)

# метод класса можно вызывать через сам класс, не указывая параметр self
# для работы с методами на уровне класса
v3 = Vector(5, 6)
print(Vector.validate(5))
res = Vector.get_coord(v3)
print(res)

# staticmethod - методы, не имеющие доступа ни к атрибутам класса, ни к атрибутам его экземпляров
# независимая, самостоятельная функция, объявленная внутри класса
v4 = Vector(1, 200)
print(Vector.norm2(5, 6))
res = Vector.get_coord(v4)
print(res)

# вызов можно прописывать как через класс, так и через экземпляр класса
v5 = Vector(10, 20)
print(v5.norm2(5, 6))
print(v5.validate(20))

# теоретически, из статического метода можно обращаться к атрибутам класса через имя класса,
# но на практике так не рекомендуется делать

# в статическом методе рекомендуется использовать параметры, только заданные как аргументы метода


# Task 6
class Factory:
    @staticmethod
    def build_sequence():
        return []

    @staticmethod
    def build_number(string):
        return int(string)


class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


res = Loader.parse_format("1, 2, 3, -5, 10", Factory)
print(res)


# Task 7:
from string import ascii_lowercase, digits

class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        if self.check_name(name):
            self.name = name
        self.size = size

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):
        if 3 <= len(name) <= 50 and set(name).issubset(cls.CHARS_CORRECT):
            return True
        raise ValueError("некорректное поле name")


class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        if self.check_name(name):
            self.name = name
        self.size = size

    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):
        if 3 <= len(name) <= 50 and set(name).issubset(cls.CHARS_CORRECT):
            return True
        raise ValueError("некорректное поле name")


login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()
print(html)
print(TextInput.check_name("Логин"))
print(PasswordInput.check_name("Пароль"))


# Task 8
from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number: str):
        if len(number) != 19 or '-' not in number:
            return False
        for num in number.split('-'):
            if len(num) != 4 or not set(num).issubset(digits):
                return False
        return True

    @classmethod
    def check_name(cls, name: str):
        if ' ' not in name or not set(name).issubset(cls.CHARS_FOR_NAME + ' ') or len(name.split()) != 2:
            return False
        return True


print(digits)
is_number = CardCheck.check_card_number("1234-5678-9012-0000")
print(is_number)
is_name = CardCheck.check_name("SERGEI BALAKIREV")
print(is_name)

# Variant 2 - регулярные выражения
# import re
#
#
# class CardCheck:
#     @staticmethod
#     def check_card_number(number):
#         return bool(re.fullmatch(r"\d{4}(?:-\d{4}){3}", number))
#
#     @staticmethod
#     def check_name(name):
#         return bool(re.fullmatch(r"[A-Z\d]+ [A-Z\d]+", name))


# Task 9
class Video:
    def create(self, name):
        self.name = name

    def play(self):
        print(f"воспроизведение видео {self.name}")


class YouTube:
    videos = []

    @classmethod
    def add_video(cls, video):
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx):
        if video_indx < len(cls.videos):
            cls.videos[video_indx].play()


v1 = Video()
v2 = Video()
v1.create("Python")
v2.create("Python ООП")
YouTube.add_video(v1)
YouTube.add_video(v2)
YouTube.play(0)
YouTube.play(1)


# Task 10
class AppStore:
    def __init__(self):
        self.app_lst = []
        # можно также хранить перечень приложений в словаре, где ключ это id объекта app, а значение - его адрес

    def add_application(self, app):
        self.app_lst.append(app)

    def remove_application(self, app):
        if app in self.app_lst:
            self.app_lst.remove(app)

    def block_application(self, app):
        if app in self.app_lst:
            app.blocked = True

    def total_apps(self):
        return len(self.app_lst)


class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked


store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
print(store.__dict__)
print(*(x.__dict__ for x in store.app_lst))

store.add_application(Application("VK"))
print(store.__dict__)
print(*(x.__dict__ for x in store.app_lst))

store.block_application(app_youtube)
print(store.__dict__)
print(*(x.__dict__ for x in store.app_lst))

store.remove_application(app_youtube)
print(store.__dict__)

print(id(app_youtube))

# Variant 2
# def block_application(self, app):
#     if isinstance(app, Application):
#         app.blocked = True
#     else:
#         TypeError("Argument is not instance of Application")


# Task 11
class Viber:
    msg_list = []
    # хранить объекты msg можно в словаре, ключ - id объекта msg, значение - сам объект

    @classmethod
    def add_message(cls, msg):
        cls.msg_list.append(msg)

    @classmethod
    def remove_message(cls, msg):
        cls.msg_list.remove(msg)

    @staticmethod
    def set_like(msg):
        msg.fl_like = not msg.fl_like

    @classmethod
    def show_last_message(cls, n=1):
        if type(n) == int and n != 0:
            for m in cls.msg_list[-n:]:
                print(m.text)

    @classmethod
    def total_messages(cls):
        return len(cls.msg_list)


class Message:
    def __init__(self, text):
        self.text = text
        self.fl_like = False


msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.show_last_message()
Viber.show_last_message(3)
Viber.set_like(msg)
Viber.remove_message(msg)

# lst = [1, 2, 3, 4, 5]
# n = 0
# print(*lst[-n:], sep='\n')
