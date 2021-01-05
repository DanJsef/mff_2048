import pygame as pg


class State():
    def __init__(self):
        self.quit = False
        self.done = False
        self.next = None
        self.previous = None

    def center_text(self, screen, text, posX, posY, width, height):
        font = pg.font.Font('freesansbold.ttf', 32)
        text = font.render(text, True, pg.Color(
            255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (posX + width // 2,
                           posY + height // 2)
        screen.blit(text, textRect)
