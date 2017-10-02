import pygame


## Global asset manager
# @todo TODO: cache tiles at zoom levels to save rescale time.
class AssetManager():
    tiles = {}
    tiles_scaled = {}
    ui = {}
    fonts = {}

    
    @staticmethod
    def load():
        # tiles
        tile_path = "assets/default/tiles/"
        tiles_to_load = ["uninitialized", "missing", "player", "grass", "tile-floor"]

        for name in tiles_to_load:
            AssetManager.tiles[name] = pygame.image.load(tile_path+name+".png")
            AssetManager.tiles[name].convert()

        # ui
        AssetManager.ui["bottom-bar"] = pygame.image.load("assets/default/ui/bottom-bar.png")
        AssetManager.ui["bottom-bar"].convert()

        # fonts
        AssetManager.fonts["monospace"] = pygame.font.SysFont("monospace", 15)


    @staticmethod
    def rescale(size):
        for key in AssetManager.tiles:
            AssetManager.tiles_scaled[key] = pygame.transform.scale(AssetManager.tiles[key], (size, size))

    @staticmethod
    def get_tile(name):
        if AssetManager.tiles_scaled[name]:
            return AssetManager.tiles_scaled[name]
        else:
            return AssetManager.tiles_scaled["missing"]


    @staticmethod
    def get_ui(name):
        return AssetManager.ui[name]