from math import floor, ceil

from .asset_manager import AssetManager
from .sprite_slicer import SpriteSlicer

## The size of individual UI tiles in pixels.
TILE_SIZE = 24
BOTTOM_BAR_HEIGHT = 24


class UIManager():
    def __init__(self, game):
        self.game = game
        self.num_tiles = (floor((self.game.window_size[0]-500) / self.game.camera.zoom),
                          floor((self.game.window_size[1]-24) / self.game.camera.zoom))


    def update(self):
        self.num_tiles = (floor((self.game.window_size[0]-500) / self.game.camera.zoom),
                          floor((self.game.window_size[1]-24) / self.game.camera.zoom))

    
    ## Draws the UI.
    # Which is currently only the bar at the bottom.
    def draw(self):
        SpriteSlicer.draw(self.game, "bottom-bar",0, self.game.window_size[1]-BOTTOM_BAR_HEIGHT,
            self.game.window_size[0], BOTTOM_BAR_HEIGHT)