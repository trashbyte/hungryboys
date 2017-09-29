from foodgame.entities import EntityLiving
from foodgame.util import Point
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT


class Player():
    def __init__(self, game):
        self.game = game
        self.entity = EntityLiving(game)
        self.entity.sprite = "player"
        self.game.world.move(self.entity, Point(110, 110))


    def update(self, dt):
        self.entity.update()


    def draw(self):
        self.entity.draw()


    def move(self, key):
        newpos = self.entity.pos
        if key == K_UP:
            newpos = newpos + Point(0, -1)
        elif key == K_DOWN:
            newpos = newpos + Point(0, 1)
        elif key == K_LEFT:
            newpos = newpos + Point(-1, 0)
        elif key == K_RIGHT:
            newpos = newpos + Point(1, 0)
        self.game.world.move(self.entity, newpos)
        self.game.camera.track_player(self.entity.pos)
        self.game.pass_time(1)