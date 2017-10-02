from .item_base import ItemBase

class ItemTool(ItemBase):
    def __init__(self, game, name):
        super().__init__(game)
        self._name = name


    @property
    def name(self):
        return self._name