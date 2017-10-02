from .biome_base import BiomeBase
from foodgame.entities import EntityStatic, EntityItem
from foodgame.util import Point
from foodgame.items import ItemTool, ItemFood
from foodgame.foods import Food


class BiomeTest(BiomeBase):
    def __init__(self):
        super().__init__()


    def generate(self, game):
        for x in range(50):
            for y in range(50):
                e = EntityStatic(game, "Grass")
                e.sprite = "grass"
                game.world.move(e, Point(50+x*2, 50+y*2))

        for x in range(8):
            for y in range(8):
                e = EntityStatic(game, "Kitchen Tile")
                e.sprite = "tile-floor"
                game.world.move(e, Point(100+x, 100+y))

        item_sp = ItemTool(game, "Spatula")
        ent_sp = EntityItem(game, item_sp)
        ent_sp.sprite = "spatula"
        game.world.move(ent_sp, Point(96, 102))

        food_flour = Food()
        food_flour.name = "Wheat Flour"
        item_flour = ItemFood(game, food_flour)
        ent_flour = EntityItem(game, item_flour)
        ent_flour.sprite = "powder-white"
        game.world.move(ent_flour, Point(96, 104))