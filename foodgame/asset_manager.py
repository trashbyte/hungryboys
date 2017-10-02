import pygame


## Global asset manager
class AssetManager():
    tiles = {}
    tile_cache = {}
    ui = {}
    fonts = {}
    size = 16

    
    @staticmethod
    def load():
        # tiles
        tile_path = "assets/default/tiles/"
        tiles_to_load = ["uninitialized", "missing", "player", "grass", "tile-floor", "powder-white", "spatula"]

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
        AssetManager.size = size
        if size not in AssetManager.tile_cache:
            AssetManager.tile_cache[size] = {}
            for key in AssetManager.tiles:
                AssetManager.tile_cache[size][key] = pygame.transform.scale(AssetManager.tiles[key], (size, size))


    @staticmethod
    def get_tile(name):
        if name in AssetManager.tile_cache[AssetManager.size]:
            return AssetManager.tile_cache[AssetManager.size][name]
        else:
            return AssetManager.tile_cache[AssetManager.size]["missing"]


    @staticmethod
    def get_ui(name):
        return AssetManager.ui[name]