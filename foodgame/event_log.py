import pygame,sys,collections
from .sprite_slicer import SpriteSlicer


## An on-screen message log to write to instead of writing to the terminal like *monsters*
class EventLog():
    ## Constructor for EventLog.
    # @param game The owning Game.
    def __init__(self, game):
        ## The owning Game.
        self.game = game

        ## How many messages to put onscreen.
        self.log_length = 10

        ## The height of each message in the log.
        self.message_height = 15

        ## The width of the log screen
        self.log_width = 480

        ## The x position of the log's top left corner.
        self.log_x = self.game.window_size[0]-self.log_width

        ## The y position of the log's top left corner.
        self.log_y = 0

        ## A list of all messages passed ever.
        # @todo FIXME: currently stores every message ever. Should be replaced with a deque.
        self.message_list = []

        ## The last x messages.
        self.last_messages = collections.deque("", self.log_length)

        ## The font used to render messages.
        self.log_font = pygame.font.SysFont("monospace", 15)
    

    ## Adds a message to the log.
    # @param new_message The message to write.
    def write(self, new_message):
        self.message_list.append(str(new_message))
        self.last_messages.append(str(new_message))
        # This actually just adds the message to appropriate lists. No print yet.


    ## Updates x/y coordinates.
    # Another reason to get everything into the UI manager.
    def update(self):
        self.log_x = self.game.window_size[0]-self.log_width


    ## Draws the messages currently in the deque to the screen. Called from Game#draw.
    # @todo TODO: figure out onscreen object layering so the event log doesn't draw its own background. UI manager should.
    def draw(self):
        SpriteSlicer.draw(self.game, "bottom-bar", self.log_x, self.log_y, self.log_width,
            self.message_height*self.log_length+5) #the +5 creates a bottom margin
        for index, message in enumerate(list(self.last_messages)):
            self.currently_printing = self.log_font.render(message, 0, (255,255,255))
            self.game.screen.blit(self.currently_printing, (self.log_x,
                (self.message_height*index)+self.log_y+3) ) #the +3 nudges the words off top edge
