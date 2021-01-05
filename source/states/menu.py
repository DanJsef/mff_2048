import pygame as pg
from ..templates import State, Menu


class MainMenu(Menu):

    def __init__(self):
        Menu.__init__(self)
        self.next = 'game'
        self.options = [64, 128, 256, 512, 1024, 2048]
        self.menu_name = 'Choose difficulty'
        self.background = (235, 155, 52)

    def user_input(self, event):
        if event.type == pg.KEYDOWN:
            input_key = pg.key.name(event.key)
            if input_key == 'return':
                self.set_target(self.options[self.selected])
                self.done = True
            self.select_option(input_key)


class LoseMenu(Menu):

    def __init__(self):
        Menu.__init__(self)
        self.next = 'menu'
        self.options = ['YES', 'NO']
        self.menu_name = 'You lost, play again?'
        self.background = (235, 70, 52)

    def user_input(self, event):
        if event.type == pg.KEYDOWN:
            input_key = pg.key.name(event.key)
            if input_key == 'return':
                if self.options[self.selected] == 'YES':
                    self.done = True
                else:
                    self.quit = True
                    self.done = True
            self.select_option(input_key)


class WinMenu(Menu):

    def __init__(self):
        Menu.__init__(self)
        self.next = 'menu'
        self.options = ['YES', 'NO']
        self.menu_name = 'You won, play again?'
        self.background = (52, 235, 100)

    def user_input(self, event):
        if event.type == pg.KEYDOWN:
            input_key = pg.key.name(event.key)
            if input_key == 'return':
                if self.options[self.selected] == 'YES':
                    self.done = True
                else:
                    self.quit = True
                    self.done = True
            self.select_option(input_key)
