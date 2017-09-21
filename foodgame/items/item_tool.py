from .item_base import ItemBase

def ItemTool(ItemBase):
    def __init__(self, game):
        super().__init__(game)