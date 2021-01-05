import pygame as pg


HEIGHT = WIDTH = 512
WIN_SIZE = (HEIGHT, WIDTH)
FPS = 15

pg.init()

SCREEN = pg.display.set_mode(WIN_SIZE)
CLOCK = pg.time.Clock()
