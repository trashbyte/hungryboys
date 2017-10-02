from .entity_base import EntityBase


class EntityItem(EntityBase):
    def __init__(self, game, item):
        super().__init__(game)
        self.item = item
        self.game.world.add(self, True)


    @property
    def name(self):
        return self.item.name
