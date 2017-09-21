from .entity_base import EntityBase


class EntityLiving(EntityBase):
    def __init__(self, game):
        super().__init__(game)
        self.game.world.add(self, True)