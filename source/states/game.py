from ..templates import State
from ..engine import Engine
from ..setup import WIDTH, HEIGHT
import pygame as pg


class GameState(State):
    def __init__(self):
        State.__init__(self)
        pg.display.set_caption('2048 - Playing')
        self.WIDTH, self.HEIGHT = WIDTH, HEIGHT
        self.DIMENSION = 4
        self.GAP = self.HEIGHT // self.DIMENSION // 8
        self.TILE_SIZE = (self.HEIGHT - 5*self.GAP) // self.DIMENSION
        self.engine = Engine()
        self.engine.set_target(2048)
        self.COLORS = {
            ' ': 'grey',
            2: 'red',
            4: 'yellow',
            8: 'brown',
            16: 'green',
            32: 'blue',
            64: 'orange',
            128: 'purple',
            256: 'white',
            512: 'pink',
            1024: 'cyan',
            2048: 'black',
        }

    # RENDERING

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

    def user_input(self, event):
        if event.type == pg.KEYDOWN:
            input_key = pg.key.name(event.key)
            if input_key == 'left':
                self.engine.move_left()
            elif input_key == 'right':
                self.engine.move_right()
            elif input_key == 'down':
                self.engine.move_down()
            elif input_key == 'up':
                self.engine.move_up()
            elif input_key == 'r':
                self.engine.reset()

    def update(self, screen):

        if self.engine.check_win():
            print("GAME WON")

        if self.engine.check_lose():
            print("NOT MOVABLE")
            self.next = 'menu'
            self.done = True

        self.render_board(screen)
