from foodgame.util import Point
from foodgame import AssetManager


class EntityBase():
    def __init__(self, game):
        self.game = game
        self.pos = Point(0, 0)
        self.sprite = "uninitialized"


    @property
    def name(self):
        return "(untitled entity)"


    def update(self, dt): pass
    def pass_time(self, seconds): pass


    def draw(self):
        size = self.game.camera.zoom
        pos = (self.pos - self.game.camera.pos) * size
        self.game.screen.blit(AssetManager.get_tile(self.sprite), (pos.x, pos.y, size, size))