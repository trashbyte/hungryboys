import pygame

class AssetManager():
    tiles = {}
    ui = {}
    fonts = {}

    
    @staticmethod
    def load():
        # tiles
        AssetManager.tiles["uninitialized"] = pygame.image.load("assets/default/tiles/uninitialized.png")
        AssetManager.tiles["uninitialized"].convert()
        AssetManager.tiles["missing"] = pygame.image.load("assets/default/tiles/missing.png")
        AssetManager.tiles["missing"].convert()

        AssetManager.tiles["player"] = pygame.image.load("assets/default/tiles/player.png")
        AssetManager.tiles["player"].convert()
        AssetManager.tiles["grass"] = pygame.image.load("assets/default/tiles/grass.png")
        AssetManager.tiles["grass"].convert()

        # ui
        AssetManager.ui["bottom-bar"] = pygame.image.load("assets/default/ui/bottom-bar.png")
        AssetManager.ui["bottom-bar"].convert()

        # fonts
        AssetManager.fonts["monospace"] = pygame.font.SysFont("monospace", 15)


    @staticmethod
    def get_tile(name):
        if AssetManager.tiles[name]:
            return AssetManager.tiles[name]
        else:
            return AssetManager.tiles["missing"]


    @staticmethod
    def get_ui(name):
        return AssetManager.ui[name]