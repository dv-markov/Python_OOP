# Конфигуратор Самсон Контролс-r2
from collections.abc import Iterable


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
        return f'\n{self.__class__.__name__}: {self.art_nr}; {self.name} \n'


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


# заполнение склада
inventory = list()
inventory.append(Body('0100-8530', 'Корпус тип 3241 DN50 PN25-40 Исполнение F DIN (1.0619)', 50, ('1.0619', 'A216 WCC')))
inventory.append(Body('0104-1246', 'Корпус тип 3241 DN50 PN25-40 Исполнение F DIN (1.5638)', 50, ('1.5638', 'A352 LC3')))
inventory.append(Body('0103-6354', 'Корпус тип 3241 DN50 PN25-40 Исполнение F DIN (1.4408)', 50, ('1.4408', 'A351 CF8M')))
inventory.append(Body('00100-8560', 'Корпус тип 3241 DN80 PN25-40 Исполнение F DIN (1.0619)', 80, ('1.0619', 'A216 WCC')))
inventory.append(Body('0104-1250', 'Корпус тип 3241 DN80 PN25-40 Исполнение F DIN (1.5638)', 80, ('1.5638', 'A352 LC3')))
inventory.append(Body('0103-7430', 'Корпус тип 3241 DN80 PN25-40 Исполнение F DIN (1.4408)', 80, ('1.4408', 'A351 CF8M')))
inventory.append(Body('0100-8530-RU', 'Корпус тип 3241 DN50 PN25-40 Исполнение F ГОСТ (20ГЛ)', 50,
                      ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3')))
inventory.append(Body('0103-6354-RU', 'Корпус тип 3241 DN50 PN25-40 Исполнение F ГОСТ (12Х18Н9ТЛ)', 50,
                      ('12Х18Н9ТЛ', '1.4408', 'A351 CF8M')))
inventory.append(Body('0100-8560-RU', 'Корпус тип 3241 DN80 PN25-40 Исполнение F ГОСТ (20ГЛ)', 80,
                      ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3')))
inventory.append(Body('0103-7430-RU', 'Корпус тип 3241 DN80 PN25-40 Исполнение F ГОСТ (12Х18Н9ТЛ)', 80,
                      ('12Х18Н9ТЛ', '1.4408', 'A351 CF8M')))

inventory.append(Bonnet('1590-8445', 'Крышка тип 3241 DN32-50 (1.0460) с втулкой (1.4104)', (32, 40, 50),
                        ('20ГЛ', '1.0619', 'A216 WCC')))
inventory.append(Bonnet('1993-0739', 'Крышка тип 3241 DN32-50 (1.5638) с втулкой (1.4404)', (32, 40, 50),
                        ('20ГЛ', '1.5638', 'A352 LC3')))
inventory.append(Bonnet('1991-6457', 'Крышка тип 3241 DN32-50 (1.4404) с втулкой (1.4404)', (32, 40, 50),
                        ('12Х18Н9ТЛ', '1.4408', 'A351 CF8M')))
inventory.append(Bonnet('1590-8445-RU', 'Крышка тип 3241 DN32-50 (09Г2С) с втулкой (12Х17)', (32, 40, 50),
                        ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3')))
inventory.append(Bonnet('1991-6457-RU', 'Крышка тип 3241 DN32-50  (08Х18Н10Т) с втулкой (08Х17Н13М2Т)', (32, 40, 50),
                        ('12Х18Н9ТЛ', '1.4408', 'A351 CF8M')))
inventory.append(Bonnet('1590-8447', 'Крышка тип 3241 DN65-80 (1.0460) с втулкой (1.4104)', (65, 80),
                        ('20ГЛ', '1.0619', 'A216 WCC')))
inventory.append(Bonnet('1993-0741', 'Крышка тип 3241 DN65-80 (1.5638) с втулкой (1.4404)', (65, 80),
                        ('20ГЛ', '1.5638', 'A352 LC3')))
inventory.append(Bonnet('1991-7755', 'Крышка тип 3241 DN65-80 (1.4404) с втулкой (1.4404)', (65, 80),
                        ('12Х18Н9ТЛ', '1.4408', 'A351 CF8M')))
inventory.append(Bonnet('1590-8447-RU', 'Крышка тип 3241 DN65-80 (09Г2С) с втулкой (12Х17)', (65, 80),
                        ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3')))
inventory.append(Bonnet('1991-7755-RU', 'Крышка тип 3241 DN65-80 (08Х18Н10Т) с втулкой (08Х17Н13М2Т)', (65, 80),
                        ('12Х18Н9ТЛ', '1.4408', 'A351 CF8M')))

inventory.append(Seat('0110-1798', 'Седло тип 3241 DN32-50 SB38 me (1.4006)', (32, 40, 50), 25,
                      ('20ГЛ', '1.0619', 'A216 WCC')))


print('Доступные детали:')
# # print(*(x.__dict__ for x in inventory), sep='\n')
# # print()
for item in inventory:
    print(item.__class__.__name__, item.__dict__)
#
#
# valve_param = dict.fromkeys(('тип клапана', 'DN', 'PN', 'материал корпуса', 'Kvs'), None)
# print(valve_param)
# for x in valve_param:
#     value = input(f'Введите {x}: ')
#     valve_param[x] = int(value) if x in ('DN', 'PN', 'Kvs') else value
# print(valve_param)
# # valve_param = {'тип клапана': 3241, 'DN': 50, 'PN': 40, 'материал корпуса': '20ГЛ', 'Kvs': 10}
#
# v1 = Type3241(*valve_param.values())
# print(v1.__dict__)
# v1.get_bom()
# print(v1.__dict__)


