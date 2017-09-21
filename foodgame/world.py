WORLD_SIZE = 1000


class World():
    def __init__(self, game):
        self.game = game
        self.grid = [ [] for x in range(WORLD_SIZE*WORLD_SIZE) ]
        self.needs_updates = []


    def at_xy(self, x, y):
        return self.grid[y*WORLD_SIZE+x]


    def at_index(self, i):
        return self.grid[i]


    def at_pos(self, pos):
        return self.grid[pos.y*WORLD_SIZE+pos.x]


    def add(self, new, needs_update):
        self.at_pos(new.pos).append(new)
        if needs_update:
            self.needs_updates.append(new)


    '''
    ONLY MOVE ENTITIES WITH World#move. This keeps world pos and entity pos synchronised.
    '''
    def move(self, ent, new_pos):
        self.at_pos(ent.pos).remove(ent)
        ent.pos = new_pos
        self.at_pos(ent.pos).append(ent)


    def pass_time(self, seconds):
        for e in self.needs_updates:
            e.pass_time(seconds)


    def draw(self, dt):
        #FIXME: currently draws everything on top of each other (needs priority)

        x1 = self.game.camera.pos.x
        x2 = x1 + 40
        y1 = self.game.camera.pos.y
        y2 = y1 + 40

        for x in range(x1, x2):
            for y in range(y1, y2):
                for e in self.grid[y*WORLD_SIZE+x]:
                    e.draw()