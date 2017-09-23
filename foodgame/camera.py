from foodgame.util import Point


## A structure representing the state of the world viewport.
class Camera():
    ## Camera constructor.
    # @param game The owning Game
    def __init__(self, game):
        ## The owning Game.
        self.game = game
        ## Position of the camera.
        self.pos = Point(100, 100)
        ## Curent zoom level, expressed as the tile width in pixels.
        self.zoom = 16


    ## Track the player if they move off-screen.
    # @param e_pos The player's position as a Point
    def track_player(self, e_pos):
        temp_x = self.pos.x
        temp_y = self.pos.y
        while e_pos.x < temp_x + 5:
            temp_x -= 1
        while e_pos.x > temp_x + self.game.ui_manager.num_tiles[0] - 5:
            temp_x += 1
        while e_pos.y < temp_y + 5:
            temp_y -= 1
        while e_pos.y > temp_y + self.game.ui_manager.num_tiles[1] - 5:
            temp_y += 1
        self.pos = Point(temp_x, temp_y)
