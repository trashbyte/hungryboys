from foodgame.util import Point
from foodgame import AssetManager


class EntityBase():
    def __init__(self, game):
        self.game = game
        self.pos = Point(0, 0)
        self.sprite = "error"


    def update(self, dt): pass


    def draw(self):
        size = self.game.camera.zoom
        pos = (self.pos - self.game.camera.pos) * 16
        self.game.screen.blit(AssetManager.get_tile(self.sprite), (pos.x, pos.y, size, size))