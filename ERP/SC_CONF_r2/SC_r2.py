# Конфигуратор Самсон Контролс-r2
from collections.abc import Iterable
from inventory_fill import fill_inventory


class TPA:
    def __init__(self, valve_type, dn, pn, mat, kvs):
        self.valve_type = valve_type
        self.params = {'dn': dn,
                       'pn': pn,
                       'mat': mat,
                       'kvs': kvs}


class Type3241(TPA):
    def __init__(self, valve_type, dn, pn, mat, kvs):
        super().__init__(valve_type, dn, pn, mat, kvs)
        self.parts = {key: [] for key in ('Body', 'Bonnet', 'Seat')}

    def get_bom(self):
        for part in self.parts:
            for x in inventory:
                if x.__class__.__name__ == part and \
                        all(self.params[p] in x.attrs[p] for p in x.attrs):
                    self.parts[part].append(x)


class Part:
    def __init__(self, art_nr, name):
        self.art_nr = art_nr
        self.name = name

    @staticmethod
    def get_list(value):
        return list(value) if isinstance(value, Iterable) and type(value) != str else [value]

    def __repr__(self):
        return f' {self.art_nr}: {self.name}'


class Body(Part):
    def __init__(self, art_nr, name, dn, mat):
        super().__init__(art_nr, name)
        self.attrs = {'dn': self.get_list(dn),
                      'mat': self.get_list(mat)}


class Bonnet(Part):
    def __init__(self, art_nr, name, dn, mat):
        super().__init__(art_nr, name)
        self.attrs = {'dn': self.get_list(dn),
                      'mat': self.get_list(mat)}


class Seat(Part):
    def __init__(self, art_nr, name, dn, kvs, mat):
        super().__init__(art_nr, name)
        self.attrs = {'dn': self.get_list(dn),
                      'kvs': self.get_list(kvs),
                      'mat': self.get_list(mat)}


def invite_message():
    def invite():
        print()
        print("Выберите действие и введите соответствующую цифру:", "\n",
              "1 - Задать конфигурацию клапана, 2 - Отобразить доступные детали, 0 - Выход")

        return input("> ")

    s = invite()
    while s not in ('1', '2', '0'):
        print('Ошибка ввода!')
        s = invite()

    return s


def dashes(n):
    return '-' * n


if __name__ == '__main__':
    title = "Конфигуратор Самсон Контролс, версия 0.2а"
    print(dashes(len(title)), title, dashes(len(title)), sep='\n')
    # текстовые переменные
    part_names1 = {'Body': 'КОРПУС', 'Bonnet': 'КРЫШКА', 'Seat': 'СЕДЛО'}
    part_names2 = {'Body': 'корпуса', 'Bonnet': 'крышки', 'Seat': 'седла'}
    # заполнение склада
    inventory = fill_inventory()

    s1 = invite_message()
    while s1 != '0':
        print()

        if s1 == '2':
            print('Доступные детали:')
            print(dashes(50))
            for item in inventory:
                print(item.__class__.__name__, item.__dict__)
            print(dashes(50))

        elif s1 == '1':
            valve_param = dict.fromkeys(('тип клапана', 'DN', 'PN', 'материал корпуса', 'Kvs'), None)
            for x in valve_param:
                value = input(f'Введите {x}: ')
                valve_param[x] = int(value) if x in ('DN', 'PN', 'Kvs') else value.upper()
            print('\n', 'Введены параметры клапана:', sep='')
            print(valve_param)
            # valve_param = {'тип клапана': 3241, 'DN': 50, 'PN': 40, 'материал корпуса': '20ГЛ', 'Kvs': 25}

            v1 = Type3241(*valve_param.values())
            print('\n', 'Создан объект по шаблону "клапан 3241":', sep='')
            print(v1.__dict__, '\n')

            input('...Нажмите клавишу ВВОД для создания BOM...')
            v1.get_bom()
            print()
            print(f'Подобраны подходящие детали для клапана конфигурации {v1.valve_type}',
                  *v1.params.values(), sep='-')

            print(dashes(50))
            for p in v1.parts:
                print(f'{part_names1[p]}:')
                print(*v1.parts[p], sep='\n') if len(v1.parts[p]) > 0 \
                    else print(f' Для данной конфигурации клапана доступные {part_names2[p]} не найдены!')
            print(dashes(50))

        s1 = invite_message()
