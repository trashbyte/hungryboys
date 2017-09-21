import pygame

class AssetManager():
    tiles = {}

    
    @staticmethod
    def load():
        AssetManager.tiles["player"] = pygame.image.load("assets/tiles/default/player.png")
        AssetManager.tiles["player"].convert()
        AssetManager.tiles["grass"] = pygame.image.load("assets/tiles/default/grass.png")
        AssetManager.tiles["grass"].convert()


    @staticmethod
    def get_tile(name):
        return AssetManager.tiles[name]