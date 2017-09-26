import pygame,sys,collections


## An on-screen message log to write to instead of writing to the terminal like *monsters*
class EventLog():
    ## Constructor for EventLog.
    # @param game The owning Game.
    def __init__(self, game):
        ## The owning Game.
        self.game = game

        ## How many messages to put onscreen.
        self.log_length = 10

        ## How many messages to store before oldest are deleted.
        self.log_history = 1000

        ## The complete list of messages stored in memory.
        self.message_list = collections.deque("", self.log_history)

        ## The last few messages to display onscreen.
        self.last_messages = collections.deque("", self.log_length)

        ## The font used to render messages.
        self.log_font = pygame.font.SysFont("monospace", 15)
    

    ## Adds a message to the log.
    # @param new_message The message to write.
    def write(self, new_message):
        self.message_list.append(str(new_message))
        self.last_messages.append(str(new_message))
        # This actually just adds the message to appropriate lists. No print yet.


    ## Draws the messages currently in the deque to the screen. Called from Game#draw.
    def draw(self):
        for index, message in enumerate(list(self.last_messages)):
            self.currently_printing = self.log_font.render(message, 1, (255,255,255))
            self.game.screen.blit(self.currently_printing, (self.game.window_size[0]-480, (15*index)))
