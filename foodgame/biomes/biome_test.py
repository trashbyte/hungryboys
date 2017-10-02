from .biome_base import BiomeBase
from foodgame.entities import EntityStatic
from foodgame.util import Point


class BiomeTest(BiomeBase):
    def __init__(self):
        super().__init__()


    def generate(self, game):

        for x in range(50):
            for y in range(50):
                e = EntityStatic(game)
                e.sprite = "grass"
                game.world.move(e, Point(50+x*2, 50+y*2))
        for x in range(8):
            for y in range(8):
                e = EntityStatic(game)
                e.sprite = "tile-floor"
                game.world.move(e, Point(100+x, 100+y))