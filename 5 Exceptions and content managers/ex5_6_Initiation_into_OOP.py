# 5.6 Посвящение в объектно-ориентированное программирование
# Морской бой
from random import randint, shuffle

FIELD_SIZE = 10


class ShipError(Exception): pass
class ShipCollisionError(ShipError): pass
class ShipValueError(ShipError): pass


class Ship:
    def __init__(self, length: int, tp: int = 1, x=None, y=None):
        self._x = x
        self._y = y
        self._length = length
        self._tp = tp
        self._is_move = True
        self._cells = ['O'] * length

    def __setattr__(self, key, value):
        match key:
            case '_x' | '_y':
                # verify coords
                if value is not None and (type(value) != int or not 0 <= value < FIELD_SIZE):
                    raise ShipValueError(f'Координаты корабля должны быть '
                                     f'целыми числами в диапазоне от 0 до {FIELD_SIZE - 1}')
            case '_length':
                if type(value) != int or not 0 < value < 5:
                    raise ShipValueError('Длина корабля должна быть целым числом в диапазоне от 1 до 4')
            case '_tp':
                if value not in (1, 2):
                    raise ShipValueError('Ориентация корабля должна быть 1 (горизонтальная) или 2 (вертикальная)')
        super().__setattr__(key, value)

    @property
    def length(self):
        return self._length

    @property
    def tp(self):
        return self._tp

    @property
    def cells(self):
        return self._cells

    def set_start_coords(self, x, y):
        self._x, self._y = x, y

    def get_start_coords(self):
        return self._x, self._y

    def move(self, go):
        """Перемещение корабля в направлении его ориентации на go клеток
        (go = 1 - движение в одну сторону на клетку; go = -1 - движение в другую сторону на одну клетку);
        движение возможно только если флаг _is_move = True"""
        if self._is_move and self._tp == 1:
            self._x += go
        elif self._is_move and self._tp == 2:
            self._y += go
        # else:
        #     return False
        #
        # return True

    def is_collide(self, ship):
        def collision(x1, y1, dx, dy, x2, y2):
            return x1 <= x2 <= x1 + dx and y1 <= y2 <= y1 + dy

        rect_x, rect_y = (coord - 1 for coord in ship.get_start_coords())
        ship_dx, ship_dy = (ship.length + 1, 2)[::(-1, 1)[ship.tp == 1]]
        self_dx, self_dy = (self.length - 1, 0)[::(-1, 1)[self._tp == 1]]
        return collision(rect_x, rect_y, ship_dx, ship_dy, self._x, self._y) \
               or collision(rect_x, rect_y, ship_dx, ship_dy, self._x + self_dx, self._y + self_dy)
        # проверяем попадает ли своя голова или хвост в область вокруг другого корабля

    def is_out_pole(self, size):
        if self._tp == 1:
            return self._x + self._length > size
        elif self._tp == 2:
            return self._y + self._length > size

    def is_alive(self):
        return self._is_move

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, key, value):
        if value not in (1, 2):
            raise ValueError('Значение статуса палубы корабля должно быть 1 (целый) или 2 (ранен)')
        self._cells[key] = value

    def __repr__(self):
        return f"Корабль {f'{self._length}-х палубный' if self._length > 1 else 'однопалубный'} / " \
               f"x={self._x} y={self._y} / ориентация {('горизонтальная', 'вертикальная')[self._tp - 1]}: {self._cells}"

    def __bool__(self):
        return self._x is not None and self._y is not None


class GamePole:
    def __init__(self, size: int = FIELD_SIZE):
        self.size = size
        self._ships = []

    def init(self):
        fleet = {4: 1, 3: 2, 2: 3, 1: 4}
        for ship_length, ship_number in fleet.items():
            self._ships.extend(Ship(ship_length, tp=(randint(1, 2))) for _ in range(ship_number))

        for ship in self._ships:
            while not ship or ship.is_out_pole(self.size):
                try:
                    ship.set_start_coords(randint(0, 9), randint(0, 9))
                    self.check_collision(ship)
                except ShipCollisionError:
                    ship.set_start_coords(None, None)
                    continue

    def check_collision(self, ship1):
        temp_fleet = [s for s in self._ships if s and s is not ship1]
        for ship2 in temp_fleet:
            # print(f'Пересечение {ship1} и {ship2}: {ship1.is_collide(ship2)}')
            if ship1.is_collide(ship2):
                raise ShipCollisionError

    def get_ships(self):
        return self._ships

    def move_ships(self):
        directions = [-1, 1]
        for ship in self._ships:
            if ship.is_alive():
                tmp_coords = ship.get_start_coords()
                shuffle(directions)
                for d in directions:
                    try:
                        ship.move(d)
                        self.check_collision(ship)
                        if ship.is_out_pole(self.size):
                            raise ShipValueError('Выход за пределы поля')
                    except ShipError as e:
                        # print(e)
                        ship.set_start_coords(*tmp_coords)
                    else:
                        # print(f'{ship} перемещен на {d} клетку с {tmp_coords}')
                        break
                # else:
                #     print(f'{ship} не может быть перемещен')

    def show(self):
        for line in self.get_pole():
            print(*line)

    def get_pole(self):
        pole = [['.' for _ in range(self.size)] for _ in range(self.size)]
        for ship in self._ships:
            x, y = ship.get_start_coords()
            if ship.tp == 1:
                pole[y][x:x+ship.length] = ship.cells
            elif ship.tp == 2:
                for i in range(ship.length):
                    pole[y + i][x] = ship.cells[i]
        return tuple(tuple(line) for line in pole)


SIZE_GAME_POLE = 10

pole = GamePole(SIZE_GAME_POLE)
pole.init()
pole.show()

pole.move_ships()
print()
pole.show()
