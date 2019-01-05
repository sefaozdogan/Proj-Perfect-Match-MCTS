import numpy as np

class GameMove(object):
    def __init__(self, x_coordinate, y_coordinate, value):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.value = value

    def __repr__(self):
        return "x:" + str(self.x_coordinate) + " y:" + str(self.y_coordinate) + " v:" + str(self.value)

class GameState(object):
    m = 1
    b = -1

    def __init__(self, state, next_to_move, pmArray):
        self.board = state
        self.board_size = state.shape[0]
        self.next_to_move = next_to_move
        self.pmArray = pmArray

    @property
    def game_result(self):
        mark = 0
        for i in range(len(self.pmArray)):
            if self.board[int(self.pmArray[i][0][0])][int(self.pmArray[i][0][1])] == 1 and \
                    self.board[int(self.pmArray[i][1][0])][int(self.pmArray[i][1][1])] == 1 \
                    and self.board[int(self.pmArray[i][2][0])][int(self.pmArray[i][2][1])] == 1:
                mark = 1.
                break
        if len(self.pmArray) == 0:
            mark = -1

        if mark == 1 or mark == -1:
            return mark
        elif np.count_nonzero(self.board) == (self.board_size * self.board_size) - self.board_size:
            return -1.
        else:
            return None

    def is_game_over(self):
        return self.game_result != None

    def move(self, move):
        new_board = np.copy(self.board)
        new_board[move.x_coordinate, move.y_coordinate] = move.value
        new_board[move.y_coordinate, move.x_coordinate] = move.value
        next_to_move = GameState.b if self.next_to_move == GameState.m else GameState.m
        return GameState(new_board, next_to_move, self.pmArray)

    def get_legal_actions(self):
        indices = np.where(self.board == 0)
        lst = []
        for coords in list(zip(indices[0], indices[1])):
            if (coords[0] != coords[1]):
                lst.append(GameMove(coords[0], coords[1], self.next_to_move))
        return lst
