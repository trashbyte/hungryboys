from foodgame.util import Point

class Camera():
    def __init__(self, game):
        self.game = game
        self.pos = Point(100, 100)
        self.zoom = 16


    def track_player(self, e_pos):
        temp_x = self.pos.x
        temp_y = self.pos.y
        while e_pos.x < temp_x + 5:
            temp_x -= 1
        while e_pos.x > temp_x + 30:
            temp_x += 1
        while e_pos.y < temp_y + 5:
            temp_y -= 1
        while e_pos.y > temp_y + 30:
            temp_y += 1
        self.pos = Point(temp_x, temp_y)
