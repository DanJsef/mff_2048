import pygame as pg
from ..templates import State
from ..engine import Engine
from ..setup import WIDTH, HEIGHT


class GameState(State):
    def __init__(self):
        State.__init__(self)
        pg.display.set_caption('2048 - Playing')
        self.DIMENSION = 4
        self.GAP = self.HEIGHT // self.DIMENSION // 8
        self.TILE_SIZE = (self.HEIGHT - 5*self.GAP) // self.DIMENSION
        self.engine = Engine()
        self.COLORS = {
            ' ': 'grey',
            2: (238, 228, 218),
            4: (237, 224, 200),
            8: (242, 177, 121),
            16: (244, 149, 99),
            32: (243, 124, 95),
            64: (241, 93, 60),
            128: (237, 207, 115),
            256: (237, 204, 98),
            512: (237, 204, 98),
            1024: (237, 200, 80),
            2048: (237, 194, 48),
        }

    # RENDERING FUNCTIONS

    def render_board(self, screen):
        for r in range(self.DIMENSION):
            for c in range(self.DIMENSION):
                posX = r*self.TILE_SIZE + (r+1)*self.GAP
                posY = c*self.TILE_SIZE + (c+1)*self.GAP
                value = self.engine.get_board_state()[c][r]
                pg.draw.rect(screen, pg.Color(self.COLORS[value]), pg.Rect(
                    posX, posY, self.TILE_SIZE, self.TILE_SIZE))
                self.center_text(screen, str(value), posX, posY,
                                 self.TILE_SIZE, self.TILE_SIZE)

    def render(self, screen):
        self.render_background(screen)
        self.render_board(screen)

    def user_input(self, event):
        if event.type == pg.KEYDOWN:
            input_key = pg.key.name(event.key)
            if input_key == 'left' or input_key == 'a':
                self.engine.move_left()
            elif input_key == 'right' or input_key == 'd':
                self.engine.move_right()
            elif input_key == 'down' or input_key == 's':
                self.engine.move_down()
            elif input_key == 'up' or input_key == 'w':
                self.engine.move_up()

    def update(self, screen):
        if not self.engine.target:
            self.engine.target = State.target

        if self.engine.check_win():
            print("GAME WON")
            self.next = 'win'
            self.done = True
            self.engine.reset()

        if self.engine.check_lose():
            print("NOT MOVABLE")
            self.next = 'lose'
            self.done = True
            self.engine.reset()

        self.render(screen)
