from foodgame.entities import EntityLiving
from foodgame.util import Point
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT


## Class for the player.
class Player():
    ## Player Constructor.
    def __init__(self, game):
        self.game = game
        self.entity = EntityLiving(game)
        self.entity.sprite = "player"
        self.game.world.move(self.entity, Point(103, 103))


    ## Updates the player.
    def update(self, dt):
        self.entity.update()


    ## Draws the player entity.
    def draw(self):
        self.entity.draw()


    ## Moves the player, according to the key pressed.
    # @param key The key pressed.
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


    ## Gets a list of entities on the player's tile (minus itself).
    # @todo TODO: currently lists all EntityStatic's, it should list only the one with the highest priority.
    def get_standing_on(self):
        return [e.name for e in self.game.world.at_pos(self.entity.pos) if e != self.entity]