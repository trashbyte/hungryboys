from math import floor, ceil

from .asset_manager import AssetManager
from .sprite_slicer import SpriteSlicer

## The height of the bottom bar, in tiles.
BOTTOM_BAR_HEIGHT = 2
## The size of those tiles.
TILE_SIZE = 12


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
        SpriteSlicer.draw(self.game, "white-line", 0,
            self.game.window_size[1]-BOTTOM_BAR_HEIGHT*TILE_SIZE, self.game.window_size[0]/TILE_SIZE,
            BOTTOM_BAR_HEIGHT)