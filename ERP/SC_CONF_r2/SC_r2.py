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
    def __init__(self, art_nr, name, attrs=None):
        self.art_nr = art_nr
        self.name = name
        self.attrs = attrs

    @staticmethod
    def get_list(value):
        return list(value) if isinstance(value, Iterable) and type(value) != str else [value]

    def __repr__(self):
        return f'{self.art_nr}: {self.name}, {self.attrs}'


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


if __name__ == '__main__':
    # текстовые переменные
    part_names1 = {'Body': 'КОРПУС', 'Bonnet': 'КРЫШКА', 'Seat': 'СЕДЛО'}
    part_names2 = {'Body': 'корпуса', 'Bonnet': 'крышки', 'Seat': 'седла'}

    def invite_message():
        def invite():
            print()
            print("Введите одну из указанных ниже цифр для выполнения соответствующего действия:", "\n",
                  "1 - Задать конфигурацию клапана, 2 - Отобразить доступные параметры клапана, "
                  "3 - Отобразить доступные детали, 0 - Выход")
            return input("> ")
        s = invite()
        while s not in ('1', '2', '3', '0'):
            print('Ошибка ввода!')
            s = invite()
        return s

    def dashes(n):
        return '-' * n

    def get_value(x):
        val = input(f'Введите {x}: ')
        while True:
            try:
                val = int(val) if x in ('DN', 'PN', 'Kvs') else val.upper()
            except ValueError:
                print(f"Ошибка ввода! {x} должен быть числом")
                val = input(f'Введите {x}: ')
            else:
                break
        return val

    title = "Конфигуратор Самсон Контролс, версия 0.2а"
    print(dashes(len(title)), title, dashes(len(title)), sep='\n')

    # заполнение склада
    inventory = fill_inventory()
    # создание наборов параметров:
    avl_params = {key: set() for key in ('тип клапана', 'DN', 'PN', 'материал корпуса', 'Kvs')}
    atr_names = {'dn': 'DN', 'pn': 'PN', 'mat': 'материал корпуса', 'kvs': 'Kvs'}
    for part in inventory:
        for attr, values in part.attrs.items():
            avl_params[atr_names[attr]].update(values)
    avl_params['тип клапана'] = {'3241', }
    avl_params['PN'] = {25, 40}

    # просмотр склада
    print(*inventory, sep='\n')

    # начало работы с пользователем
    s1 = invite_message()
    while s1 != '0':
        print()

        if s1 == '3':
            print('Доступные детали:')
            print(dashes(50))
            for item in inventory:
                print(item, *(f'{atr_names[key]}: {value}' for key, value in item.attrs.items()), sep=';\n--> ')
            print(dashes(50))

        elif s1 == '2':
            print('Доступные параметры клапана:')
            print(dashes(50))
            for pr in avl_params:
                print(f' {pr}: {sorted(avl_params[pr])}')
            print(dashes(50))

        elif s1 == '1':
            valve_param = dict.fromkeys((avl_params.keys()), None)
            for x in valve_param:
                value = get_value(x)
                while not {value, }.issubset(avl_params[x]):
                    print(f'Ошибка ввода! Данный {x} недоступен для внесенного перечня деталей')
                    print(f"Доступные значения для параметра '{x}': ", end='')
                    print(*sorted(avl_params[x]), sep=', ')
                    value = get_value(x)
                valve_param[x] = value

            print('\n', 'Введены параметры клапана:', sep='')
            print(valve_param, '\n')
            # valve_param = {'тип клапана': 3241, 'DN': 50, 'PN': 40, 'материал корпуса': '20ГЛ', 'Kvs': 25}

            v1 = Type3241(*valve_param.values())
            # print('\n', f'Создан объект по шаблону "клапан {v1.valve_type}":', sep='')
            # print(v1.__dict__, '\n')

            input('...Нажмите клавишу ВВОД для создания BOM...')
            v1.get_bom()
            print()
            print(f'Подобраны подходящие детали для клапана конфигурации {v1.valve_type}',
                  *v1.params.values(), sep='-')

            print(dashes(50))
            for p in v1.parts:
                print(f'{part_names1[p]}:', '\n ', end='')
                print(*v1.parts[p], sep='\n ') if len(v1.parts[p]) > 0 \
                    else print(f' Для данной конфигурации клапана доступные {part_names2[p]} не найдены!')
            print(dashes(50))

        s1 = invite_message()
