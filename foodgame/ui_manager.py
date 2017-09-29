from math import floor, ceil

from .asset_manager import AssetManager


class UIManager():
    def __init__(self, game):
        self.game = game
        self.num_tiles = (floor((self.game.window_size[0]-500) / self.game.camera.zoom),
                          floor((self.game.window_size[1]-24) / self.game.camera.zoom))


    def update(self):
        self.num_tiles = (floor((self.game.window_size[0]-500) / self.game.camera.zoom),
                          floor((self.game.window_size[1]-24) / self.game.camera.zoom))


    ## Draws the UI.
    # @todo TODO: replace with a slice-drawing util.
    # the bottom bar is currently drawn piecewise, manually.
    # it should be replaced with a general utility for drawing sliced sprites.
    def draw(self):
        # draw bottom bar middle
        bottom_bar_tiles = ceil((self.game.window_size[0]-48)/24)
        for i in range(bottom_bar_tiles):
            self.game.screen.blit(
                AssetManager.get_ui("bottom-bar"),
                ((i+1)*24, self.game.window_size[1]-24),
                (24, 0, 24, 24) )

        # bottom bar end caps
        self.game.screen.blit(
            AssetManager.get_ui("bottom-bar"),
            (0, self.game.window_size[1]-24),
            (0, 0, 24, 24) )
        self.game.screen.blit(
            AssetManager.get_ui("bottom-bar"),
            (self.game.window_size[0]-24, self.game.window_size[1]-24),
            (48, 0, 24, 24) )

        time_surface = AssetManager.fonts["monospace"].render(
            "%02d:%02d:%02d" % (floor(self.game.game_time / 3600) % 24, floor((self.game.game_time % 3600) / 60), floor(self.game.game_time % 60)),
            1, (255,255,255))
        self.game.screen.blit(time_surface, (self.game.window_size[0]-480, 0))
