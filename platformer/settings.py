import pygame as pg
import random as r
from os import path

game_folder = path.dirname(__file__)
img_folder = path.join(game_folder,"imgs")
sound_folder = path.join(game_folder,"snd")

WIDTH = 480
HEIGHT = 600
FPS = 60
title = "Dodle Bounce"
FONT_NAME = "Comic_Sans"
BGCOLOR = (0, 255, 255)
HS_FILE = "highscore.txt"
SPRITESHEET = "spritesheet_jumper.png"
#player property
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PL_JUMP_POW = 20
#game properties
BOOST_POWER = 60
POW_SPAWN_PCT = 7
MOB_FREQ = 5000
PLAYER_LAYER = 2
PLATFORM_LAYER = 1
POW_LAYER = 1
MOB_LAYER = 2
CLOUD_LAYER = 0
#starting platforms
PLATFORM_LIST = [(0, HEIGHT - 60),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4),
                 (125,HEIGHT-350),
                 (350,200),
                 (175,100)]
# colors (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
GREY = (220, 220, 220)
TURQUOISE = (64, 224, 208)