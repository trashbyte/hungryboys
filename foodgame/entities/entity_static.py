from .entity_base import EntityBase


class EntityStatic(EntityBase):
    def __init__(self, game, name):
        super().__init__(game)
        self.friendly_name = name or "(untitled EntityStatic)"
        self.game.world.add(self, False)


    @property
    def name(self):
        return self.friendly_name