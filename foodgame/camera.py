from foodgame.util import Point
from .asset_manager import AssetManager


## A structure representing the state of the world viewport.
class Camera():
    ## Camera constructor.
    # @param game The owning Game
    def __init__(self, game):
        ## The owning Game.
        self.game = game
        ## Position of the camera.
        self.pos = Point(90, 90)
        ## (internal)
        self._zoom = 16
        AssetManager.rescale(self.zoom)


    ## Curent zoom level, expressed as the tile width in pixels.
    @property
    def zoom(self):
        return self._zoom


    ## Sets zoom level for camera and rescales tile sprites to match.
    # @param value The new zoom value.
    @zoom.setter
    def zoom(self, value):
        self._zoom = value
        AssetManager.rescale(value)


    ## Track the player if they move off-screen.
    # @param e_pos The player's position as a Point
    def track_player(self, e_pos):
        temp_x = self.pos.x
        temp_y = self.pos.y
        while e_pos.x < temp_x + 5:
            temp_x -= 1
        while e_pos.x > temp_x + self.game.ui_manager.num_tiles[0] - 5:
            temp_x += 1
        while e_pos.y < temp_y + 5:
            temp_y -= 1
        while e_pos.y > temp_y + self.game.ui_manager.num_tiles[1] - 5:
            temp_y += 1
        self.pos = Point(temp_x, temp_y)
