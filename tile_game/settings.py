import pygame as pg
import random as r
from os import path
vec = pg.math.Vector2

game_folder = path.dirname(__file__)
img_folder = path.join(game_folder,"imgs")
sound_folder = path.join(game_folder,"snd")

WIDTH = 1024
HEIGHT = 768
FPS = 60
title = "Template"
TILESIZE = 64
GRIDWIDTH = WIDTH/TILESIZE
GRIDHEIGHT = HEIGHT/TILESIZE
WALL_IMG = 'tile_100.png'
#player settings
PLAYER_HEALTH = 100
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 250
PLAYER_IMG = "manBlue_gun.png"
PLAYER_HIT_RECT = pg.Rect(0,0,35,35)
BARREL_OFFSER = vec(30,10)
#GUN!!!
BULLET_IMG = 'tile_214.png'
BULLET_SPEED = 500
BULLET_LIFETIME = 1000
BULLET_RATE = 150
KICKBACK = 200
GUN_SPREAD = 5
BULLET_DAMAGE = 10
#mob settings
MOB_IMG = "zoimbie1_hold.png"
MOB_SPEEDS = [150,100,100,80,125,125,200,150]
MOB_HIT_RECT = pg.Rect(0,0,30,30)
MOB_HEALTH = 100
MOB_DAMAGE = 10
MOB_KNOCKBACK = 20
AVOID_RAD = 50
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
#effects
MUZZLE_FLASH = ["fire_01.png","fire_02.png"]
FLASH_DER = 40
#layers
WALL_LAYER = 1
PLAYER_LAYER = 2
MOB_LAYER = 2
BULLET_LAYER = 3
EFFECTS_LAYER = 4