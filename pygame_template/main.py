import pygame as pg
import random
import math

class NPC(pg.sprite.Sprite):
    def __init__(self):
        super(NPC, self).__init__()
        self.image = pg.Surface((15,15))
        self.image.fill(TURQUOISE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)
        self.speedx = 5
        self.speedy = 5
        # center the sprite will orbit
        self.center_x = self.rect.centerx
        self.center_y = self.rect.centery

        self.angle = 1
        self.radius = 75
        self.speed = .1

    def update(self):
        # circle movement
        # if self.angle <= 6.25:
        #     self.rect.centerx = self.radius *math.sin(self.angle)+self.center_x
        #     self.rect.centery = self.radius *math.cos(self.angle)+self.center_y
        #     self.angle += self.speed

        # constant speed
        self.rect.x+=self.speedx
        self.rect.y+=self.speedy

        # bounce
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speedx *= -1
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speedy *= -1

        # V movement
        # if self.rect.center >=WIDTH/2:
        #     self.speedy = -5
        #     self.speedx = 5
        # if self.rect.bottomleft[0] > WIDTH and self.rect.bottomleft[1] >=0:
        #     self.rect.bottomleft = (o,o)
        #     self.speedy = -5
        #     self.speedx = 5

        # square movement
        # if self.rect.right >= WIDTH-1:
        #     self.speedy = -5
        #     self.speedx = 0
        # if self.rect.top <= 1:
        #     self.speedy = 0
        #     self.speedx = -5
        # if self.rect.left <= 1:
        #     self.speedy = 5
        #     self.speedx = 5
        #
        # if self.rect.bottom >= HEIGHT-1 and self.rect.right != WIDTH:
        #     self.speedy = 0
        #     self.speedx = 5

        # warping
        # if self.rect.left > WIDTH:
        #     self.rect.top = HEIGHT
        #     self.rect.center = (WIDTH/2,HEIGHT+25)
        #     self.speedx = 0
        #     self.speedy = -15
        #
        # if self.rect.right < 0:
        #     self.rect.bottom = 0
        #     self.rect.center = (WIDTH/2,0)
        #     self.speedx = 0
        #     self.speedy = 15
        #
        # if self.rect.top > HEIGHT:
        #     self.rect.right = WIDTH
        #     self.rect.center = (WIDTH+25,HEIGHT/2)
        #     self.speedx = -15
        #     self.speedy = 0
        #
        # if self.rect.bottom < 0:
        #     self.rect.left = 0
        #     self.rect.center = (0,HEIGHT/2)
        #     self.speedx = 15
        #     self.speedy = 0

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pg.Surface((50,50))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)
        self.speedx = 0
        self.speedy = 0
    def update(self):
        pass

WIDTH = 360
HEIGHT = 480
FPS = 30
title = "Template"

#colors (RGB)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (128,0,128)
YELLOW = (255,255,0)
CYAN = (0,255,255)
GREY = (220,220,220)
TURQUOISE = (64,224,208)

pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(title)
clock = pg.time.Clock()

# create sprite groups
all_sprites = pg.sprite.Group()
players_group = pg.sprite.Group()
npc_group = pg.sprite.Group()

# create game objects
npc = NPC()
player = Player()

# add objects to sprite groups
all_sprites.add(npc)
all_sprites.add(player)
players_group.add(player)
npc_group.add(npc)


# game loop
running = True
while running:
    clock.tick(FPS)
    # process input
    # getting list of events
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_KP4:
                player.rect.x -= 50
            if event.key == pg.K_KP2:
                player.rect.y += 50
            if event.key == pg.K_KP6:
                player.rect.x += 50
            if event.key == pg.K_KP8:
                player.rect.y -= 50
            if event.key == pg.K_KP1:
                player.rect.x -= 50
                player.rect.y += 50
            if event.key == pg.K_KP3:
                player.rect.x +=50
                player.rect.y += 50
            if event.key == pg.K_KP9:
                player.rect.x += 50
                player.rect.y -= 50
            if event.key == pg.K_KP7:
                player.rect.x -= 50
                player.rect.y -= 50
            if event.key == pg.K_a:
                player.rect.x -= 50
            if event.key == pg.K_s:
                player.rect.y += 50
            if event.key == pg.K_d:
                player.rect.x += 50
            if event.key == pg.K_w:
                player.rect.y -= 50
            if event.key == pg.K_LEFT:
                player.rect.x -= 50
            if event.key == pg.K_DOWN:
                player.rect.y += 50
            if event.key == pg.K_RIGHT:
                player.rect.x += 50
            if event.key == pg.K_UP:
                player.rect.y -= 50
        # checking events for quit
        if event.type == pg.QUIT:
            running = False

    # make updates
    all_sprites.update()

    # render (Draw)
    screen.fill(PURPLE)
    all_sprites.draw(screen)

    # last thing we do in the loop
    pg.display.flip()

# exits the game
pg.quit()
