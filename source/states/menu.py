from ..templates import State
import pygame as pg


class Menu(State):

    def __init__(self):
        State.__init__(self)
        self.next = 'game'

    def user_input(self, event):
        if event.type == pg.KEYDOWN:
            self.done = True
            self.selected = 128

    def update(self, screen):
        screen.fill((0, 0, 0))
