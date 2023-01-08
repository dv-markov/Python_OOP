# 5.6 Посвящение в объектно-ориентированное программирование
# Морской бой


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


sh = Ship(4)
print(sh.__dict__)