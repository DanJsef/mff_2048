import pygame as pg
from .setup import WIDTH, HEIGHT


class State():
    target = None

    def __init__(self):
        self.quit = False
        self.done = False
        self.next = None
        self.previous = None
        self.WIDTH, self.HEIGHT = WIDTH, HEIGHT
        self.background = (128, 128, 128)

    def center_text(self, screen, text, posX, posY, width=0, height=0, size=32):
        font = pg.font.Font('freesansbold.ttf', size)
        text = font.render(text, True, pg.Color(
            255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (posX + width // 2,
                           posY + height // 2)
        screen.blit(text, textRect)

    def render_background(self, screen):
        screen.fill(self.background)


class Menu(State):

    def __init__(self):
        State.__init__(self)
        self.BASE_X = self.WIDTH // 2
        self.BASE_Y = self.HEIGHT * 0.25
        self.OFFSET = self.HEIGHT // 8
        self.menu_name = 'menu'
        self.options = []
        self.selected = 0

    def set_target(self, target):
        State.target = target

    def render_menu_name(self, screen):
        self.center_text(screen, self.menu_name, self.BASE_X,
                         self.HEIGHT * 0.1, size=48)

    def render_cursor(self, screen):
        self.center_text(screen, 'X', self.BASE_X * 0.40,
                         self.BASE_Y + self.OFFSET * self.selected)

    def render_options(self, screen):
        for i, option in enumerate(self.options):
            self.center_text(screen, str(option), self.BASE_X,
                             self.BASE_Y + self.OFFSET * i)

    def select_option(self, input_key):
        if input_key == 'down' or input_key == 's':
            self.selected = (self.selected + 1) % len(self.options)
        elif input_key == 'up' or input_key == 'w':
            self.selected = (self.selected - 1) % len(self.options)

    def render(self, screen):
        self.render_background(screen)
        self.render_menu_name(screen)
        self.render_options(screen)
        self.render_cursor(screen)

    def update(self, screen):
        self.render(screen)
