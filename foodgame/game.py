import pygame, sys
from pygame.locals import *

from .player import Player
from .world import World
from .asset_manager import AssetManager
from .camera import Camera
from foodgame.util import Point
from .event_log import EventLog

from foodgame.entities import EntityStatic


class Game():
    def __init__(self): pass


    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode((960, 540))
        pygame.display.set_caption('hungry')

        self.last_update = pygame.time.get_ticks()
        self.fps = 0
        self.fps_time = 0

        AssetManager.load()

        self.camera = Camera(self)
        self.world = World(self)
        self.player = Player(self) # entity automatically created and added to world]
        self.event_log = EventLog(self)

        for x in range(10):
            for y in range(10):
                e = EntityStatic(self)
                e.sprite = "grass"
                self.world.move(e, Point(85+x*5, 85+y*5))


        while True:
            now = pygame.time.get_ticks()
            dt = now - self.last_update
            self.last_update = now

            self.fps_time += dt
            if self.fps_time > 1000:
                self.fps_time = 0
                self.event_log.write(self.fps)
                self.fps = 0
            else:
                self.fps += 1

            self.update(dt)
            self.draw(dt)


    def update(self, dt):
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP or event.key == pygame.K_DOWN
                    or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                        self.player.move(event.key)

    def pass_time(self, seconds):
        self.world.pass_time(seconds)


    def draw(self, dt):
        self.screen.fill((0,0,0))
        self.world.draw(dt)
        self.event_log.draw()
        pygame.display.flip()