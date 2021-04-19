# pygame template -skeleton for new pygame progect-
# art form Kenny.nl
# music credits
# happy tune by http://opengameart.org/user/syncopika
# yippee by http://opengameart.org/user/snabisch
import pygame as pg
import random as r
from os import path
from settings import *
from sprites import *

class Game(object):
    def __init__(self):
        self.running = True
        #initilizing pygame to create a window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(title)
        self.clock = pg.time.Clock()
        self.font_name = pg.font.match_font(FONT_NAME)
        self.load_data()
    def load_data(self):
        self.dir = path.dirname(__file__)
        self.imgdir = path.join(self.dir,'img')
        with open(path.join(self.dir,HS_FILE),'r') as f:
            try:
                self.highschore = int(f.read())
            except:
                self.highschore = 0
        self.spritesheet = Spritesheet(path.join(self.imgdir, SPRITESHEET))
        self.cloud_imgs = []
        for i in range(1, 4):
            self.cloud_imgs.append(pg.image.load(path.join(self.imgdir, 'cloud{}.png'.format(i))).convert())
        #sounds
        self.snd_dir = path.join(self.dir,'snd')
        self.jump_snd = pg.mixer.Sound(path.join(self.snd_dir,"Jump33.wav"))
        self.boost_snd = pg.mixer.Sound(path.join(self.snd_dir, "Boost16.wav"))
    def new(self):
        self.score = 0
        # create sprite groups
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.platforms = pg.sprite.Group()
        self.pow_ups = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.clouds = pg.sprite.Group()
        # create game objects
        self.player = Player(self)
        for plat in PLATFORM_LIST:
            Platform(self,*plat)
        self.mob_timer = 0
        #music
        pg.mixer.music.load(path.join(self.snd_dir,'Happy Tune.ogg'))
        #start runing game loop
        self.run()
    def run(self):
        pg.mixer.music.play(loops=-1)
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        pg.mixer.music.fadeout(500)
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing=False
                self.running=False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
            if event.type == pg.KEYUP:
                if event.key == pg.K_SPACE:
                    self.player.jump_cut()
    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        # mob stuff
        now = pg.time.get_ticks()
        if now - self.mob_timer > 5000+r.choice([-1000, -500, 0, 500, 1000]):
            self.mob_timer = now
            Mob(self)
        mob_hits = pg.sprite.spritecollide(self.player,self.mobs,False,pg.sprite.collide_mask)
        if mob_hits:
            self.playing = False
        # check if player hits a platform - only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player,self.platforms,False)
            if hits:
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom > lowest.rect.bottom:
                        lowest = hit
                if self.player.pos.x < lowest.rect.right+10 and\
                   self.player.pos.x > lowest.rect.left-10:
                    if self.player.pos.y < lowest.rect.centery:
                        self.player.pos.y = lowest.rect.top
                        self.player.vel.y = 0
                        self.player.jumping = False
        # if player reaches top 1/4 of screen
        if self.player.rect.top <= HEIGHT / 4:
            if r.randrange(100) < 1:
                Cloud(self)
            self.player.pos.y += max(abs(self.player.vel.y), 2)
            for cloud in self.clouds:
                cloud.rect.y += max(abs(self.player.vel.y/2),2)
            for mob in self.mobs:
                mob.rect.y += max(abs(self.player.vel.y), 2)
                if mob.rect.top >= HEIGHT:
                    mob.kill()
            for plat in self.platforms:
                plat.rect.y += max(abs(self.player.vel.y), 2)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
                    self.score += 10
        #if player hits pow_up
        pow_hits = pg.sprite.spritecollide(self.player,self.pow_ups,True)
        for pow in pow_hits:
            if pow.type == 'boost':
                self.boost_snd.play()
                self.player.vel.y = -BOOST_POWER
                self.player.jumping = False
        # Died
        if self.player.rect.bottom > HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
            if len(self.platforms) == 0:
                self.playing = False
        # spawn new platforms to keep same average number
        while len(self.platforms) < 6:
            width = r.randrange(50, 100)
            Platform(self,r.randrange(0, WIDTH - width),
                    r.randrange(-75, -30),)
    def draw(self):
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score),22,WHITE,WIDTH/2,15)
        # -after- drawing everything
        pg.display.flip()
    def show_start_screen(self):
        pg.mixer.music.load(path.join(self.snd_dir, 'Yippee.ogg'))
        pg.mixer.music.play(loops=-1)
        self.screen.fill(BGCOLOR)
        self.draw_text(title,48,BLACK,WIDTH/2,HEIGHT/4)
        self.draw_text("arrows to move, space to jump",33,BLACK,WIDTH/2,HEIGHT/2)
        self.draw_text("press a key to play",22,BLACK,WIDTH/2,HEIGHT*3/4)
        self.draw_text("High Score: "+str(self.highschore),22,BLACK,WIDTH/2,15)
        pg.display.flip()
        self.wait_for_key()
        pg.mixer.music.fadeout(500)
    def show_GO_screen(self):
        if not self.running:
            return
        pg.mixer.music.load(path.join(self.snd_dir, 'Yippee.ogg'))
        pg.mixer.music.play(loops=-1)
        self.screen.fill(RED)
        self.draw_text("GAME OVER",48,BLACK,WIDTH/2,HEIGHT/4)
        self.draw_text("Score:"+str(self.score),33,BLACK,WIDTH/2,HEIGHT/2)
        self.draw_text("press a key to play again",22,BLACK,WIDTH/2,HEIGHT*3/4)
        if self.score > self.highschore:
            self.highschore = self.score
            self.draw_text("NEW RECORD!!",22,BLACK,WIDTH/2,HEIGHT/2+40)
            with open(path.join(self.dir, HS_FILE), 'w') as f:
                f.write(str(self.score))
        else:
            self.draw_text("High Score: "+str(self.highschore),22,BLACK,WIDTH/2,HEIGHT/2+40)
        pg.display.flip()
        self.wait_for_key()
        pg.mixer.music.fadeout(500)
    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False
    def draw_text(self,text,size,color,x,y):
        font = pg.font.Font(self.font_name,size)
        text_suf = font.render(text,True,color)
        text_rect = text_suf.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_suf,text_rect)

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_GO_screen()
pg.quit()