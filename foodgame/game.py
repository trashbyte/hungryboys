import pygame, sys
from pygame.locals import *

from .player import Player
from .world import World
from .asset_manager import AssetManager
from .ui_manager import UIManager
from .camera import Camera
from foodgame.util import Point
from .event_log import EventLog

from foodgame.entities import EntityStatic


## The main game class.
#
# Most major game components hold a reference to their parent Game, to access other components.
# Miscellaneous todo items go here.
#
# @todo TODO: InputManager
# @todo TODO: Remappable controls
# @todo TODO: Config file
# @todo TODO: In-game time
# @todo TODO: Hold move key to run
class Game():
    ## Constructor for Game
    def __init__(self): pass


    ## Runs a constructed Game. Should only ever be called once.
    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode((960, 540), HWSURFACE|DOUBLEBUF|RESIZABLE)
        pygame.display.set_caption('hungry')
        self.window_size = (960, 540)

        self.last_update = pygame.time.get_ticks()
        self.fps = 0
        self.fps_time = 0

        AssetManager.load()

        self.camera = Camera(self)
        self.world = World(self)
        self.player = Player(self) # entity automatically created and added to world
        self.event_log = EventLog(self)
        self.ui_manager = UIManager(self) # must be initialized after camera

        # temp: add grass so we can see what we're doing
        for x in range(25):
            for y in range(25):
                e = EntityStatic(self)
                e.sprite = "grass"
                self.world.move(e, Point(85+x*2, 85+y*2))

        while True:
            now = pygame.time.get_ticks()
            dt = now - self.last_update
            self.last_update = now

            self.fps_time += dt
            if self.fps_time > 1000:
                self.fps_time = 0
                self.event_log.write("FPS: %i" % self.fps)
                self.fps = 0
            else:
                self.fps += 1

            self.update(dt)
            self.draw(dt)


    ## Updates things that should be updated every frame.
    def update(self, dt):
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==VIDEORESIZE:
                self.window_size = event.dict['size']
                self.screen = pygame.display.set_mode(self.window_size, HWSURFACE|DOUBLEBUF|RESIZABLE)
                self.ui_manager.update()
                self.event_log.write("Tiles: %s" % str(self.ui_manager.num_tiles))
                self.event_log.update()
                self.camera.track_player(self.player.entity.pos)
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP or event.key == pygame.K_DOWN
                    or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                        self.player.move(event.key)


    ## Updates things that need to change over time in the game.
    #
    # Updates things that need to change over time in the game, such as creatures and food spoilage.
    # Only called when the player moves or performs an action.
    def pass_time(self, seconds):
        self.world.pass_time(seconds)


    ## Draws game components to the screen.
    def draw(self, dt):
        self.screen.fill((0,0,0))
        self.world.draw(dt)
        self.event_log.draw()
        self.ui_manager.draw()
        pygame.display.flip()    
