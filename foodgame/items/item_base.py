class ItemBase():
    def __init__(self, game):
        self.game = game
        self._name = "(untitled item)"


    @property
    def name(self):
        return self._name