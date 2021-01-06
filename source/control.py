import pygame as pg
from . import setup


class Control():
    """
    State management
    """

    def __init__(self):
        self.running = True
        self.screen = setup.SCREEN
        self.clock = setup.CLOCK
        self.fps = setup.FPS

    def setup_states(self, state_dict, start_state):
        """
        Sets possible states and selects the initial state.

        Parameters:
            state_dict: dictionary of created states
            start_state: name of state which should be executed first
        """
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]

    def flip_state(self):
        """
        Handles switching to a next state.
        """
        self.state.done = False  # Reset the done indicator, so the state can run again in future.
        previous, self.state_name = self.state, self.state.next
        self.state = self.state_dict[self.state_name]
        self.state.previous = previous

    def event_loop(self):
        """
        Handles reading inputs.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            # Specific event handling from current state.
            self.state.user_input(event)

    def update(self):
        """
        Handles updating states.
        """
        if self.state.quit:  # Quits the app if state triggers quit.
            self.running = False
        elif self.state.done:  # Calls state switch logic after current state is done.
            self.flip_state()
        # Calls the specific update on current state.
        self.state.update(self.screen)

    def game_loop(self):
        """
        Main game loop. Handles executing previous methods in correct order.
        """
        while self.running:
            self.event_loop()
            self.update()
            # Pygame method to actually update render content.
            pg.display.update()
            self.clock.tick(self.fps)
