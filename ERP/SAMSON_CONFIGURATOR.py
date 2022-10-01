# Конфигуратор Самсон Контролс
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
        self.parts = dict.fromkeys(('Body', 'Seat', 'Plug'), [])

    def get_bom(self):
        for part in self.parts:
            print(part)
            tmp = []
            for x in inventory:
                if x.__class__.__name__ == part and all(self.params[p] in x.attrs[p] for p in x.attrs):
                    tmp.append(x)
            print(tmp)
            self.parts[part] += tmp
            # self.parts[part].append(x for x in inventory
            #                         if x.__class__.__name__ == part)



class Part:
    __art_nr = 0

    def __init__(self, name):
        self.art_nr = Part.__art_nr
        Part.__art_nr += 1
        self.name = name

    @staticmethod
    def get_list(value):
        return list(value) if isinstance(value, Iterable) and type(value) != str else [value]

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.art_nr}, {self.name} \n'


class Body(Part):
    def __init__(self, name, dn, pn, mat):
        super().__init__(name)
        self.attrs = {'dn': self.get_list(dn),
                      'pn': self.get_list(pn),
                      'mat': self.get_list(mat)}
        # self.dn = self.get_list(dn)
        # self.pn = self.get_list(pn)
        # self.mat = self.get_list(mat)


class Seat(Part):
    def __init__(self, name, dn, kvs):
        super().__init__(name)
        self.attrs = {'dn': self.get_list(dn),
                      'kvs': self.get_list(kvs)}


class Plug(Part):
    def __init__(self, name, dn, kvs):
        super().__init__(name)
        self.attrs = {'dn': self.get_list(dn),
                      'kvs': self.get_list(kvs)}
        # self.dn = self.get_list(dn)
        # self.kvs = self.get_list(kvs)


inventory = list()
inventory.append(Body('Корпус DN50 PN40', 50, (16, 25, 40), ('20ГЛ', '1.0619', '1.6220')))
inventory.append(Body('Корпус DN50 PN40', 50, (16, 25, 40), ('09Г2С', '1.0619', '1.6220')))
inventory.append(Body('Корпус DN50 PN40', 50, (16, 25, 40), '1.0619'))
inventory.append(Body('Корпус DN50 PN40', 50, (16, 25, 40), '1.6220'))
inventory.append(Seat('Седло DN 32-50 Kvs10', (32, 40, 50), 10))
inventory.append(Seat('Седло DN 32-50 Kvs16', (32, 40, 50), 16))
inventory.append(Seat('Седло DN 32-50 Kvs25', (32, 40, 50), 25))
inventory.append(Plug('Плунжер DN 32-50 Kvs10 lin', (32, 40, 50), 10))
inventory.append(Plug('Плунжер DN 32-50 Kvs10 =%', (32, 40, 50), 10))
inventory.append(Plug('Плунжер DN 32-50 Kvs16 =%', (32, 40, 50), 16))
# print(*(x.__dict__ for x in inventory), sep='\n')
# print()

# valve_param = dict.fromkeys(('тип клапана', 'DN', 'PN', 'материал корпуса', 'Kvs'), None)
# print(valve_param)
# for x in valve_param:
#     valve_param[x] = input(f'Введите {x}: ')
# print(valve_param)
valve_param = {'тип клапана': 3241, 'DN': 50, 'PN': 40, 'материал корпуса': '20ГЛ', 'Kvs': 10}

v1 = Type3241(*valve_param.values())
for item in inventory:
    print(item.__class__.__name__, item.__dict__)
print(v1.__dict__)

v1.get_bom()
print(v1.__dict__)


