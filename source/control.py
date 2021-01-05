import pygame as pg
from . import setup


class Control():
    def __init__(self):
        self.running = True
        self.screen = setup.SCREEN
        self.clock = setup.CLOCK
        self.fps = setup.FPS

    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]

    def flip_state(self):
        self.state.done = False
        previous, self.state_name = self.state, self.state.next
        self.state = self.state_dict[self.state_name]
        self.state.previous = previous

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            self.state.user_input(event)

    def update(self):
        if self.state.quit:
            self.running = False
        elif self.state.done:
            self.flip_state()
        self.state.update(self.screen)

    def game_loop(self):
        while self.running:
            self.event_loop()
            self.update()
            pg.display.update()
            self.clock.tick(self.fps)
