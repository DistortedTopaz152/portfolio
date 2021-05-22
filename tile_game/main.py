# pygame template -skeleton for new pygame progect-
import pygame as pg
import random as r
from os import path
from settings import *
from sprites import *
from tilemap import *
#hud
def draw_player_health(surf,x,y,pct):
    if pct <0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 20
    fill = pct*BAR_LENGTH
    outline_rect = pg.Rect(x,y,BAR_LENGTH,BAR_HEIGHT)
    fill_rect = pg.Rect(x,y,fill,BAR_HEIGHT)
    if pct > 0.6:
        col = GREEN
    elif pct > 0.3:
        col = YELLOW
    else:
        col = RED
    pg.draw.rect(surf,col,fill_rect)
    pg.draw.rect(surf,WHITE,outline_rect,2)
class Game(object):
    def __init__(self):
        self.running = True
        #initilizing pygame to create a window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(title)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500,150)
        self.load_data()
    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder,"img")
        map_folder = path.join(game_folder,"maps")
        self.map = Tiledmap(path.join(map_folder, "map_the_first.tmx"))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_img = pg.image.load(path.join(img_folder,PLAYER_IMG)).convert_alpha()
        self.wall_img = pg.image.load(path.join(img_folder,WALL_IMG)).convert_alpha()
        self.mob_img = pg.image.load(path.join(img_folder,MOB_IMG)).convert_alpha()
        self.bullet_img = pg.image.load(path.join(img_folder,BULLET_IMG)).convert_alpha()
        self.wall_img = pg.transform.scale(self.wall_img,(TILESIZE,TILESIZE))
        self.bullet_img = pg.transform.scale(self.bullet_img,(25,25))
        self.gun_flashes = []
        for img in MUZZLE_FLASH:
            self.gun_flashes.append(pg.image.load(path.join(img_folder,img)).convert_alpha())
    def new(self):
        # create sprite groups
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.walls = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        # create game objects
        # for row, tiles in enumerate(self.map.data):
        #     for col, tile in enumerate(tiles):
        #         if tile == "1":
        #             Wall(self, col, row)
        #         if tile == "M":
        #             Mob(self, col, row)
        #         if tile == 'P':
        #             self.player = Player(self, col, row)
        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == "player":
                self.player = Player(self,tile_object.x,tile_object.y)
            if tile_object.name == "zombie":
                Mob(self,tile_object.x,tile_object.y)
            if tile_object.name == "wall":
                Obstical(self,tile_object.x,tile_object.y,
                         tile_object.width,tile_object.height)
        self.camera = Camera(self.map.width,self.map.height)
        self.draw_debug = False
        #start runing game loop
        self.run()
    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS)/1000
            self.events()
            self.update()
            self.draw()
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing=False
                self.running=False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_h:
                    self.draw_debug = not self.draw_debug
    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)
        hits = pg.sprite.spritecollide(self.player,self.mobs,False,collide_hit_rect)
        for hit in hits:
            self.player.health -= MOB_DAMAGE
            hit.vel = vec(0,0)
            if self.player.health<=0:
                self.playing=False
        if hits:
            self.player.pos += vec(MOB_KNOCKBACK,0).rotate(-hits[0].rot)
        hits = pg.sprite.groupcollide(self.mobs,self.bullets,False,True)
        for hit in hits:
            hit.health-=BULLET_DAMAGE
            hit.vel = vec(0,0)
    def draw_grid(self):
        for x in range(0,WIDTH,TILESIZE):
            pg.draw.line(self.screen,PURPLE,(x,0),(x,HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, PURPLE, (0,y),(WIDTH,y))
    def draw(self):
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.blit(self.map_img,self.camera.apply_rect(self.map_rect))
        #self.draw_grid()
        for spite in self.all_sprites:
            if isinstance(spite,Mob):
                spite.draw_health()
            self.screen.blit(spite.image,self.camera.apply(spite))
            if self.draw_debug:
                pg.draw.rect(self.screen,CYAN,self.camera.apply_rect(spite.hit_rect),1)
        if self.draw_debug:
            for wall in self.walls:
                pg.draw.rect(self.screen,CYAN,self.camera.apply_rect(wall.rect),1)
            #hud
        draw_player_health(self.screen,10,10,self.player.health/PLAYER_HEALTH)
        # -after- drawing everything
        pg.display.flip()
    def show_start_screen(self):
        pass
    def show_GO_screen(self):
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_GO_screen()
pg.quit()