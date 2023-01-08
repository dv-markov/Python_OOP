# 5.6 Посвящение в объектно-ориентированное программирование
# Морской бой
from random import randint
FIELD_SIZE = 10


class Ship:
    def __init__(self, length: int, tp: int = 1, x=None, y=None):
        self._x = x
        self._y = y
        self._length = length
        self._tp = tp
        self._is_move = True
        self._cells = [1] * length

    def __setattr__(self, key, value):
        match key:
            case '_x' | '_y':
                # verify coords
                if value is not None and (type(value) != int or not 0 <= value < FIELD_SIZE):
                    raise ValueError(f'Координаты корабля должны быть '
                                     f'целыми числами в диапазоне от 0 до {FIELD_SIZE-1}')
            case '_length':
                if type(value) != int or not 0 < value < 5:
                    raise ValueError('Длина корабля должна быть целым числом в диапазоне от 1 до 4')
            case '_tp':
                if value not in (1, 2):
                    raise ValueError('Ориентация корабля должна быть 1 (горизонтальная) или 2 (вертикальная)')
        super().__setattr__(key, value)

    def set_start_coords(self, x, y):
        """Установка начальных координат (запись значений в локальные атрибуты _x, _y);"""
        self._x, self._y = x, y

    def get_start_coords(self):
        return self._x, self._y

    def move(self, go):
        """Перемещение корабля в направлении его ориентации на go клеток
        (go = 1 - движение в одну сторону на клетку; go = -1 - движение в другую сторону на одну клетку);
        движение возможно только если флаг _is_move = True"""
        pass

    def is_collide(self, ship):
        """Проверка на столкновение с другим кораблем ship
        (столкновением считается, если другой корабль или пересекается с текущим или просто соприкасается,
        в том числе и по диагонали);
        метод возвращает True, если столкновение есть и False - в противном случае;"""
        pass

    def is_out_pole(self, size):
        """Проверка на выход корабля за пределы игрового поля (size - размер игрового поля, обычно, size = 10);
        возвращается булево значение True, если корабль вышел из игрового поля и False - в противном случае;"""
        pass

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, key, value):
        if value not in (1, 2):
            raise ValueError('Значение статуса палубы корабля должно быть 1 (целый) или 2 (ранен)')
        self._cells[key] = value

    def __repr__(self):
        return f"Корабль {f'{self._length}-х палубный' if self._length > 1 else 'однопалубный'}: {self._cells}"


class GamePole:
    def __init__(self, size: int = FIELD_SIZE):
        self.size = size
        self._ships = []

    def init(self):
        fleet = {4: 1, 3: 2, 2: 3, 1: 4}
        for ship_length, ship_number in fleet.items():
            self._ships.extend(Ship(ship_length, tp=(randint(1, 2))) for _ in range(ship_number))



sh = Ship(4, 2, 1, 2)
print(sh.__dict__)

gp = GamePole()
gp.init()
print(gp.__dict__)
