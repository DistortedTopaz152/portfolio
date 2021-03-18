#Attribution
####################################################################
# Code created by: Eric Broadbent
# Art Work Credit: "Kenney.nl" @ "www.kenney.nl"

####################################################################
import pygame as pg
import random as r
from math import *
from os import *

# Game object classes
####################################################################

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.sheild = 100
        self.fuel = 100
        self.lives = 3
        self.hidden = False
        self.hide_timer = pg.time.get_ticks()
        # self.image = pg.Surface((50,40))
        # self.image.fill(GREEN)
        self.image = player_img
        self.image = pg.transform.scale(player_img, (60, 48))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = self.rect.width * .85 / 2
        pg.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = (WIDTH / 2)
        self.rect.bottom = (HEIGHT - (HEIGHT * .05))
        self.speedx = 0
        self.shoot_delay = 250
        self.last_shot = pg.time.get_ticks()

    def shoot(self):
        now = pg.time.get_ticks()
        if (now-self.last_shot) > self.shoot_delay:
            self.last_shot = now
            b = Bullet(self.rect.centerx,self.rect.top-1)
            all_sprites.add(b)
            bullet_group.add(b)
            shoot_sound.play()

    def hide(self):
        #hide player temperaraly
        self.hidden = True
        self.hide_timer = pg.time.get_ticks()
        self.rect.center = (WIDTH/2,HEIGHT+500)

    def update(self):
        if self.hidden and pg.time.get_ticks()-self.hide_timer > 3000:
            self.hidden = False
            self.rect.centerx = (WIDTH / 2)
            self.rect.bottom = (HEIGHT - (HEIGHT * .05))

        self.rect.x += self.speedx

        #basic movement
        self.speedx = 0
        keystate = pg.key.get_pressed()
        if (keystate[pg.K_LEFT] or keystate[pg.K_a]) and self.fuel>0:
            self.speedx = -5
            self.fuel-=.05
        if (keystate[pg.K_RIGHT] or keystate[pg.K_d]) and self.fuel>0:
            self.speedx = 5
            self.fuel-=.05
        #player shoot
        if keystate[pg.K_SPACE]:
            self.shoot()

        # bind player to screen
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH

class Bullet(pg.sprite.Sprite):
    def __init__(self,x,y):
        super(Bullet, self).__init__()
        # self.image = pg.Surface((5,10))
        # self.image.fill(BLUE)
        self.image = bullet_img
        self.image = pg.transform.scale(self.image, (15, 30))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed = -10

    def update(self):
        self.rect.y+=self.speed
        #kill bullet when rect.bottem <= 0
        if self.rect.bottom < 0:
            self.kill()

class Explosions(pg.sprite.Sprite):
    def __init__(self,center,size):
        super(Explosions, self).__init__()
        self.size = size
        self.image = exp_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update =pg.time.get_ticks()
        self.framerate = 50
    def update(self):
        now = pg.time.get_ticks()
        if (now-self.last_update) > self.framerate:
            self.last_update = now
            self.frame+=1
            if self.frame == len(exp_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = exp_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

class NPC(pg.sprite.Sprite):
    def __init__(self):
        super(NPC, self).__init__()
        # self.image = pg.Surface((25,25))
        # self.image.fill(RED)

        self.image_orig = r.choice(meteor_images)
        #self.image_orig = pg.transform.scale(self.image_orig, (50, 50))
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .75 / 2)
        pg.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = (WIDTH / 2)
        self.rect.top = 0
        self.rsx = r.randint(-5, 5)
        self.rsy = r.randint(1, 10)
        self.speedx = self.rsx
        self.speedy = self.rsy
        self.rot = 0
        self.rot_speed = r.randint(-8,8)
        self.last_update = pg.time.get_ticks()

    def rotate(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 60:
            self.last_update = now
            #rotatesprite
            self.rot = (self.rot+self.rot_speed)%360
            new_image = pg.transform.rotate(self.image,self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = r.randrange(WIDTH - self.rect.width)
            self.rect.y = r.randrange(-100, -40)
            self.speedy = r.randrange(1, 8)

####################################################################
# Game Constants
####################################################################
HEIGHT = 900
WIDTH = 600
FPS = 60
font_name = pg.font.match_font("arial")

# Colors (R,G,B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
debug = False

title = "Shmup"

####################################################################
# game functions
####################################################################
def spawn_npc():
    for i in range(2):
        npc = NPC()
        npc_group.add(npc)
        all_sprites.add(npc)
def draw_text(surf,text,size,x,y,color):
    font = pg.font.Font(font_name,size)
    text_surf = font.render(text,True,color)
    text_rect = text_surf.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surf,text_rect)
def draw_bar(surf,x,y,pct,color):
    if pct < 0:
        pct = 0
    bar_len = 180
    bar_height = 40
    fill = (pct/100)*bar_len
    outline = pg.Rect(x,y,bar_len,bar_height)
    fillrect = pg.Rect(x,y,fill,bar_height)
    pg.draw.rect(surf,color,fillrect)
    pg.draw.rect(surf,WHITE,outline,3)

####################################################################
# initialize pygame and create window
####################################################################
pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(title)
clock = pg.time.Clock()
####################################################################
# set up asset folders
game_folder = path.dirname(__file__)
img_dir = path.join(game_folder, 'imgs')
smg_folder = path.join(game_folder,"smgs")
background_img_folder = path.join(img_dir,"background_img_folder")
playerimgs = path.join(img_dir,"playerimgs")
enemy_img_folder = path.join(img_dir,"enemy_img_folder")
animation_folder = path.join(img_dir,"animations")
####################################################################
# load imgs
####################################################################
#back grond img loaded
background = pg.image.load(path.join(background_img_folder,"img.png"))
background = pg.transform.scale(background,(WIDTH,HEIGHT))
background_rect = background.get_rect()
#player img loaded
player_img = pg.image.load(path.join(playerimgs,"img_1.png")).convert()
npc_img = pg.image.load(path.join(enemy_img_folder,"img.png")).convert()
bullet_img = pg.image.load(path.join(playerimgs,"img.png")).convert()
#enemy img loaded
meteor_images = []
meteor_list = ['meteorBrown_big1.png','meteorBrown_big2.png','meteorBrown_big3.png','meteorBrown_med1.png',
               'meteorBrown_med3.png','meteorBrown_small1.png','meteorBrown_tiny1.png','meteorBrown_tiny2.png']
for img in meteor_list:
    meteor_images.append(pg.image.load(path.join(enemy_img_folder,img)).convert())
#animation loaded
exp_anim = {}
exp_anim["lg"] = []
exp_anim["sm"] = []
for i in range(9):
    filename = "regularExplosion0{}.png".format(i)
    img = pg.image.load(path.join(animation_folder,filename)).convert()
    img.set_colorkey(BLACK)
    img_lg = pg.transform.scale(img,(200,200))
    exp_anim["lg"].append(img_lg)
    img_sm = pg.transform.scale(img, (75, 75))
    exp_anim["sm"].append(img_sm)
####################################################################
#load sounds
####################################################################
shoot_sound = pg.mixer.Sound(path.join(smg_folder,''))
expl_snds = []
for snd in ['','']:
    expl_snds.append(pg.mixer.Sound(path.join(smg_folder,snd)))
pg.mixer.music.load(path.join(smg_folder,''))
pg.mixer.music.set_volume(0.4)
####################################################################
# create Sprite groups
####################################################################
all_sprites = pg.sprite.Group()
players_group = pg.sprite.Group()
npc_group = pg.sprite.Group()
bullet_group = pg.sprite.Group()
####################################################################
# create Game Objects
####################################################################
player = Player()
for i in range(12):
    npc = NPC()
    npc_group.add(npc)
bullet = Bullet(WIDTH/2,HEIGHT/2)
####################################################################
# add objects to sprite groups
####################################################################
players_group.add(player)
bullet_group.add(bullet)
all_sprites.add(bullet)
for i in players_group:
    all_sprites.add(i)
for i in npc_group:
    all_sprites.add(i)
####################################################################
# Game Loop
###################
# game update Variables
########################################
playing = True
score = 0
level = 1
pg.mixer.music.play(loops=-1)
########################################
################################################################
while playing:
    # timing
    ##################################################
    clock.tick(FPS)
    ##################################################
    # collecting Input
    ##################################################

    # Quiting the game when we hit the x
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                playing = False
            #player shooting
            # if event.key == pg.K_SPACE:
            #     player.shoot()
        if event.type == pg.QUIT:
            playing = False

    ##################################################
    # Updates
    ##################################################
    # cheking for hit between player and npc
    hits = pg.sprite.spritecollide(player, npc_group, False, pg.sprite.collide_circle)
    if hits:
        exp = Explosions(hits[0].rect.center,"sm")
        all_sprites.add(exp)
        r.choice(expl_snds).play()
        spawn_npc()
        player.sheild-=hits[0].radius*2
        if player.sheild <= 0:
            exp = Explosions(player.rect.center,"lg")
            all_sprites.add(exp)
            player.hide()
            player.lives-=1
            player.sheild = 100
        if player.lives == 0 and not exp.alive():
            playing = False
    #bullet hits npc
    hits = pg.sprite.spritecollide(bullet_group, npc_group,True,True, pg.sprite.collide_circle)
    for hit in hits:
        if hit.radius < 30:
            size = "sm"
        else:
            size = "lg"
        exp = Explosions(hit.rect.center,size)
        all_sprites.add(exp)
        r.choice(expl_snds).play()
        score += 50 - hit.rect.radius
        spawn_npc()
    all_sprites.update()
    ##################################################
    # Render
    ##################################################

    screen.fill(BLACK)
    screen.blit(background,background_rect)
    all_sprites.draw(screen)

    #draw hud
    draw_text(screen,"Score: "+str(score),18,WIDTH/2,15,WHITE)
    draw_bar(screen,5,15,player.sheild,GREEN)
    draw_bar(screen,5,55,player.fuel,BLUE)

    pg.display.flip()
    ##################################################
pg.quit()
################################################################
