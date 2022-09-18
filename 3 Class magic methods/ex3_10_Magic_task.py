# 3.10 Испытание магией

import random


class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self, f_size=3):
        self.f_size = f_size
        self.pole = tuple(tuple(Cell() for _ in range(self.f_size)) for _ in range(self.f_size))

    def __check_indx(self, indx):
        r, c = indx
        if type(r) != int or type(c) != int or not (0 <= r < self.f_size) or not (0 <= c < self.f_size):
            raise IndexError('некорректно указанные индексы')
        return r, c

    def __getitem__(self, item):
        r, c = self.__check_indx(item)
        return self.pole[r][c].value

    def __setitem__(self, key, value):
        r, c = self.__check_indx(key)
        if self.pole[r][c]:
            self.pole[r][c].value = value

    def init(self):
        for row in self.pole:
            for cell in row:
                cell.value = 0

    def show(self):
        for row in self.pole:
            print(*(x.value for x in row))

    def human_go(self):
        r, c = map(int, input('Введите координаты клетки: ').split())
        self[r, c] = self.HUMAN_X

    def computer_go(self):
        free_coords = tuple((i, j) for i in range(self.f_size) for j in range(self.f_size) if self.pole[i][j])
        print('Ход компьютера:')
        self[random.choice(free_coords)] = self.COMPUTER_O

    def __check_win(self, char):
        row_set = set()
        col_set = set()
        diag_set = set()
        for i in range(self.f_size):
            for j in range(self.f_size):
                if self.pole[i][j].value != char:
                    row_set.add(i)
                    col_set.add(j)
                    if i == j:
                        diag_set.add(1)
                    if j == (self.f_size - 1 - i):
                        diag_set.add(2)
        return len(row_set) < self.f_size or len(col_set) < self.f_size or len(diag_set) < 2

    def __check_free_cells(self):
        return any(bool(x) for row in self.pole for x in row)

    @property
    def is_human_win(self):
        return self.__check_win(self.HUMAN_X)

    @property
    def is_computer_win(self):
        return self.__check_win(self.COMPUTER_O)

    @property
    def is_draw(self):
        return not self.__check_free_cells() and not self.is_human_win and not self.is_computer_win

    def __bool__(self):
        return self.__check_free_cells() and not self.is_human_win and not self.is_computer_win


# game = TicTacToe()
# game[0, 0] = 2
# game[0, 1] = 2
# game[0, 2] = 2
# game.human_go()
# game.computer_go()
# game.show()
# print('Human win: ', game.is_human_win())
# print('Computer win: ', game.is_computer_win())
# print('Draw: ', game.is_draw())
# print('Game not over: ', bool(game))

game = TicTacToe(5)
game.init()
step_game = 0
while game:
    game.show()
    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1

game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Game over. Все получится, со временем")
else:
    print("Ничья.")

