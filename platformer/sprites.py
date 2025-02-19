import pygame as pg
import random as r
from os import path
from settings import *
vec = pg.math.Vector2
class Spritesheet:
    #Utility class for loading
    def __init__(self,filename):
        self.spritesheet = pg.image.load(filename).convert()
    def get_image(self,x,y,width,height):
        # grab an image out of a larger spritesheet
        image = pg.Surface((width,height))
        image.blit(self.spritesheet,(0, 0),(x,y,width,height))
        image = pg.transform.scale(image,(width//2,height//2))
        return image
class Player(pg.sprite.Sprite):
    def __init__(self,game):
        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.walking = False
        self.jumping = False
        self.curent_frame = 0
        self.last_update = 0
        self.load_images()
        self.image = self.standing_frames[0]
        self.rect = self.image.get_rect()
        self.rect.center = (40,HEIGHT-100)
        self.pos = vec(40,HEIGHT-100)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    def load_images(self):
        self.standing_frames = [self.game.spritesheet.get_image(581,1265,121,191),
                                self.game.spritesheet.get_image(584,0,121,201)]
        for frame in self.standing_frames:
            frame.set_colorkey(BLACK)
        self.walking_frames_r = [self.game.spritesheet.get_image(584,203,121,201),
                                 self.game.spritesheet.get_image(678,651,121,207)]
        self.walking_frames_l = []
        for frame in self.walking_frames_r:
            frame.set_colorkey(BLACK)
            self.walking_frames_l.append(pg.transform.flip(frame,True,False))
        self.jump_frame = self.game.spritesheet.get_image(416,1660,150,181)
        self.jump_frame.set_colorkey(BLACK)
    def jump_cut(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3
    def jump(self):
        #jump only if on platform
        self.rect.x += 2
        hits = pg.sprite.spritecollide(self,self.game.platforms,False)
        self.rect.x -= 2
        if hits and not self.jumping:
            self.game.jump_snd.play()
            self.jumping = True
            self.vel.y = -PL_JUMP_POW
    def update(self):
        self.animate()
        self.acc = vec(0,PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x=0
        self.pos += self.vel + 0.5 * self.acc
        self.rect.center = self.pos
        # wrap around the sides of the screen
        if self.pos.x > WIDTH+self.rect.width/2:
            self.pos.x = 0 - self.rect.width/2
        if self.pos.x < 0 -self.rect.width/2:
            self.pos.x = WIDTH + self.rect.width/2
        self.rect.midbottom = self.pos
    def animate(self):
        now = pg.time.get_ticks()
        if self.vel.x != 0:
            self.walking=True
        else:
            self.walking=False
        if self.walking:
            if now-self.last_update > 200:
                self.last_update = now
                self.curent_frame = (self.curent_frame+1) % len(self.walking_frames_r)
                bottem = self.rect.bottom
                if self.vel.x > 0:
                    self.image=self.walking_frames_r[self.curent_frame]
                else:
                    self.image=self.walking_frames_l[self.curent_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottem
        if not self.jumping and not self.walking:
            if now - self.last_update > 350:
                self.last_update = now
                self.curent_frame = (self.curent_frame+1) % len(self.standing_frames)
                bottom = self.rect.bottom
                self.image = self.standing_frames[self.curent_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom
        self.mask = pg.mask.from_surface(self.image)
class Cloud(pg.sprite.Sprite):
    def __init__(self, game):
        self._layer = CLOUD_LAYER
        self.groups = game.all_sprites, game.clouds
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = r.choice(self.game.cloud_imgs)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = r.randrange(WIDTH-self.rect.width)
        self.rect.y = r.randrange(-500,-50)
    def update(self):
        if self.rect.top > HEIGHT:
            self.kill()
class Platform(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self._layer = PLATFORM_LAYER
        self.groups = game.all_sprites, game.platforms
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        images = [self.game.spritesheet.get_image(0,96,380,94),
                  self.game.spritesheet.get_image(382,408,200,100),
                  self.game.spritesheet.get_image(0,192,380,94),
                  self.game.spritesheet.get_image(232,1288,200,100)]
        self.image = r.choice(images)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        if r.randrange(100) < POW_SPAWN_PCT:
            Pow(self.game,self)
class Pow(pg.sprite.Sprite):
    def __init__(self,game,plat):
        self._layer = POW_LAYER
        self.groups = game.all_sprites,game.pow_ups
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.plat = plat
        self.type = r.choice(['boost'])
        self.image = self.game.spritesheet.get_image(820, 1805, 71, 70)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.plat.rect.centerx
        self.rect.bottom = self.plat.rect.top - 5
    def update(self):
        self.rect.bottom = self.plat.rect.top-5
        if not self.game.platforms.has(self.plat):
            self.kill()
class Mob(pg.sprite.Sprite):
    def __init__(self,game):
        self._layer = MOB_LAYER
        self.groups = game.all_sprites,game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image_up = self.game.spritesheet.get_image(566, 510, 122, 139)
        self.image_up.set_colorkey(BLACK)
        self.image_down = self.game.spritesheet.get_image(568, 1534, 122, 135)
        self.image_down.set_colorkey(BLACK)
        self.image = self.image_up
        self.rect = self.image.get_rect()
        self.rect.centerx = r.choice([-100,WIDTH+100])
        self.vx = r.randrange(1,4)
        if self.rect.centerx:
            self.vx *= -1
        self.rect.y = r.randrange(HEIGHT/2)
        self.vy = 0
        self.dy = 0.5
    def update(self):
        self.rect.x += self.vx
        self.vy += self.dy
        if self.vy > 3 or self.vy < -3:
            self.dy *= -1
        center = self.rect.center
        if self.dy < 0:
            self.image = self.image_up
        else:
            self.image = self.image_down
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.center = center
        self.rect.y += self.vy
        if self.rect.left > WIDTH+100 or self.rect.right < -100:
            self.kill()