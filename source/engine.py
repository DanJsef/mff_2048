import random


class Engine():

    def __init__(self):
        self.board = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
        self.SIZE = len(self.board)
        self.VEC = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.highest = 2
        self.tiles = 0
        self.moved = False
        self.target = 0

        self.new_tile()
        self.new_tile()

    def reset(self):
        self.__init__()

    # FUNCTIONS FOR WATCHING GAME STATE

    def check_lose(self):
        if self.tiles == 16:
            for r in range(self.SIZE):
                for c in range(self.SIZE):
                    for v in self.VEC:
                        x, y = r+v[0], c+v[1]
                        if x >= 0 and y >= 0 and x <= 3 and y <= 3 and self.board[r][c] == self.board[x][y]:
                            return False
            return True

    def check_win(self):
        if self.target == self.highest:
            return True

    # RANDOM TILE ADDING FUNCTIONS

    def new_tile(self):
        x = random.randrange(0, self.SIZE)
        y = random.randrange(0, self.SIZE)
        while self.board[x][y] != ' ':
            x = random.randrange(0, self.SIZE)
            y = random.randrange(0, self.SIZE)
        self.board[x][y] = random.choice([2, 2, 2, 2, 2, 2, 2, 4, 4, 4])
        self.tiles += 1

    def add_tile(self):
        if self.moved:
            self.new_tile()
            self.moved = False

    # HELPER FUNCTIONS FOR TILE MOVING

    def __compress(self):
        """
        compresses tiles to the left
        """
        for r in range(self.SIZE):
            for c in range(self.SIZE):
                if self.board[r][c] != ' ':
                    x, y = r, c
                    while y > 0 and self.board[x][y-1] == ' ':
                        self.board[x][y -
                                      1], self.board[x][y] = self.board[x][y], self.board[x][y-1]
                        self.moved = True
                        y -= 1

    def __merge(self):
        """
        merges tiles to the left and updates highest reached value
        """
        for r in range(self.SIZE):
            for c in range(self.SIZE):
                if self.board[r][c-1] != ' ' and c > 0 and self.board[r][c-1] == self.board[r][c]:
                    self.board[r][c -
                                  1], self.board[r][c] = self.board[r][c-1]*2, ' '
                    self.tiles -= 1
                    self.moved = True
                    if self.highest < self.board[r][c-1]:
                        self.highest = self.board[r][c-1]

    def __transpose(self):
        """
        transposes tile grid
        """
        result = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
        for r in range(self.SIZE):
            for c in range(self.SIZE):
                if self.board[r][c] != ' ':
                    result[c][r] = self.board[r][c]
        self.board = result

    def __reverse(self):
        """
        reverses tile grid
        """

        for r in range(self.SIZE):
            self.board[r] = self.board[r][::-1]

    # TILE MOVING FUNCTIONS

    def move_left(self):
        self.__compress()
        self.__merge()
        self.__compress()
        self.add_tile()

    def move_up(self):
        self.__transpose()
        self.move_left()
        self.__transpose()
        self.add_tile()

    def move_down(self):
        self.__transpose()
        self.move_right()
        self.__transpose()
        self.add_tile()

    def move_right(self):
        self.__reverse()
        self.move_left()
        self.__reverse()
        self.add_tile()

    # SETTERS AND GETTERS

    def get_board_state(self):
        return self.board

    def set_target(self, value):
        self.target = value
