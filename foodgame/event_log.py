import pygame,sys,collections
'''
#Makes an on-screen debug/message log to write to isntead of writing to the
terminal like *monsters*
'''

class EventLog():
    def __init__(self, game):
        self.game = game
        self.log_length = 10
        #How many messages to put onscreen
        self.message_list = []
        #A list of all messages passed ever.
        self.last_messages = collections.deque("",self.log_length)
        #The last x messages
        self.message_count = 0
        self.log_font = pygame.font.SysFont("monospace", 15)
        print(self.last_messages.maxlen)
    

    def write(self, new_message):
        '''Takes over the standard print, writing to screen instead.'''
        self.message_list.append(str(new_message))
        self.last_messages.append(str(new_message))
        #This actually just adds the message to appropriate lists. No print yet.


    def draw(self):
        '''Draws last x messages onscreen.'''
        #debug print

        for index, message in enumerate(list(self.last_messages)):
            self.currently_printing = self.log_font.render(message, 1, (255,255,255))
            self.game.screen.blit(self.currently_printing, (660,(15*index)))
