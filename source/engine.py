import random


class Engine():
    """
    Engine of the whole game. Stores the game board, handles proccess and updating the game board.
    """

    def __init__(self):
        self.board = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
        self.SIZE = len(self.board)
        self.VEC = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.highest = 2
        self.tiles = 0
        self.moved = False
        self.target = None

        self.new_tile()
        self.new_tile()

    def reset(self):
        """
        Resets the game to default parameters.
        """
        self.__init__()

    # BOARD STATE WATCHING METHODS

    def check_lose(self):
        """
        Verifies if the game board is still playable.

        Returns True if game is not playable anymore (False if is).
        """
        if self.tiles == 16:
            for r in range(self.SIZE):
                for c in range(self.SIZE):
                    for v in self.VEC:
                        x, y = r+v[0], c+v[1]
                        if x >= 0 and y >= 0 and x <= 3 and y <= 3 and self.board[r][c] == self.board[x][y]:
                            return False
            return True

    def check_win(self):
        """
        Verifies if the player won the game.

        Returns True if game was won.
        """
        if self.target == self.highest:
            return True

    # RANDOM TILE ADDING METHODS

    def new_tile(self):
        """
        Adds a new tile to random position on game board. 
        Tile value is either 2 (0.7 chance) or 4 (0.3 chance).  
        """
        x = random.randrange(0, self.SIZE)
        y = random.randrange(0, self.SIZE)

        # Generates new X,Y for as long as the possition is occupied on game board.
        # This approach might cause slow runtime for bigger boards, when almost all possitions are occupied.
        while self.board[x][y] != ' ':
            x = random.randrange(0, self.SIZE)
            y = random.randrange(0, self.SIZE)
        self.board[x][y] = random.choice([2, 2, 2, 2, 2, 2, 2, 4, 4, 4])
        self.tiles += 1

    def add_tile(self):
        """
        Handles adding new tile during game. 

        Tile won't be added if any of current tiles didn't move.
        """
        if self.moved:
            self.new_tile()
            self.moved = False

    # HELPER FUNCTIONS FOR TILE MOVING

    def __compress(self):
        """
        Compresses tiles to the left.
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
        Merges tiles to the left and updates highest reached value.
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
        Transposes tile grid.
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
        Reverses tile grid.
        """

        for r in range(self.SIZE):
            self.board[r] = self.board[r][::-1]

    # TILE MOVING FUNCTIONS

    def move_left(self):
        """
        Handles moving and merging tiles left.
        """
        self.__compress()
        self.__merge()
        self.__compress()
        self.add_tile()

    def move_up(self):
        """
        Handles moving and merging tiles up.
        """
        self.__transpose()
        self.move_left()
        self.__transpose()
        self.add_tile()

    def move_down(self):
        """
        Handles moving and merging tiles down.
        """
        self.__transpose()
        self.move_right()
        self.__transpose()
        self.add_tile()

    def move_right(self):
        """
        Handles moving and merging tiles right.
        """
        self.__reverse()
        self.move_left()
        self.__reverse()
        self.add_tile()

    # SETTERS AND GETTERS

    def get_board_state(self):
        """
        Returns the current board state.
        """
        return self.board
