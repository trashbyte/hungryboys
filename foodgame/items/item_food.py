from .item_base import ItemBase

class ItemFood(ItemBase):
    def __init__(self, game, food):
        super().__init__(game)
        self.food = food


    @property
    def name(self):
        return self.food.name