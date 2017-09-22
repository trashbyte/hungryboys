WORLD_SIZE = 1000


## The game world, which contains all entities.
class World():
    ## World constructor
    # @param game The owning Game.
    def __init__(self, game):
        ## The owning Game.
        self.game = game

        ## The grid which all entities reside in
        #
        # All entities in the World exist on a 2D plane, expressed here as an interlaced list.
        # Coordinates are y*WORLD_SIZE+x. Each element in the grid is a list, containing all
        # entities on that grid space.
        self.grid = [ [] for x in range(WORLD_SIZE*WORLD_SIZE) ]

        ## A list of all entities which need to be updated when time passes in-game.
        #
        # Most entities are things like dirt and grass that don't need to be kept updated. We keep
        # a separate list of entities to update when pass_time is called so we don't have to
        # iterate over the entire grid on each update.
        self.needs_updates = []


    ## Returns the list of entities at the given coordinates
    # @param x x coordinate
    # @param y y coordinate
    def at_xy(self, x, y):
        return self.grid[y*WORLD_SIZE+x]


    ## Returns the list of entities at the given coordinates
    # @param i A precomputed index (y*WORLD_SIZE+x)
    def at_index(self, i):
        return self.grid[i]


    ## Returns the list of entities at the given coordinates
    # @param pos Requested position as a Point
    def at_pos(self, pos):
        return self.grid[pos.y*WORLD_SIZE+pos.x]


    ## Adds an entity to the grid, and optionally to the needs_updates list.
    # @param new Entity to be added.
    # @param needs_update If True, also add the entity to the needs_updates list.
    def add(self, new, needs_update):
        self.at_pos(new.pos).append(new)
        if needs_update:
            self.needs_updates.append(new)


    ## Moves an entity to another position on the grid
    #
    # ONLY MOVE ENTITIES WITH World#move. This keeps world pos and entity pos synchronised.
    #
    # @param ent The entity to be moved
    # @param new_pos The position to move the entity to, as a Point
    def move(self, ent, new_pos):
        self.at_pos(ent.pos).remove(ent)
        ent.pos = new_pos
        self.at_pos(ent.pos).append(ent)


    ## Passes time for all entities in self.needs_updates
    def pass_time(self, seconds):
        for e in self.needs_updates:
            e.pass_time(seconds)


    ## Draws all on-screen entities in the world.
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