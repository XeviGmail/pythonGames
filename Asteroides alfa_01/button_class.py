import pygame
from settings import *

class Button:
    def __init__(self, game, x, y, width, height, bg_colour, border_colour='white', hover_colour=None, function=None, text=None):
        self.game = game
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.bg_colour = bg_colour
        self.border_colour = border_colour
        self.hover_colour = hover_colour
        self.hovered = False
        self.function = function
        self.text = text
        self.font = pygame.font.SysFont('arial', BUTTON_TEXT_SIZE, bold=True)

    def update(self):
        cursor = pygame.mouse.get_pos()
        if self.x + self.width > cursor[0] > self.x and self.y + self.height > cursor[1] > self.y:
            self.hovered = True
        else:
            self.hovered = False

    def draw(self):
        if not self.hovered:
            pygame.draw.rect(self.game.screen, self.bg_colour, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(self.game.screen, self.hover_colour, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(self.game.screen, self.border_colour, (self.x, self.y, self.width, self.height), 2)
        self.show_text()

    def click(self):
        if self.function != None:
            print('function')
            self.function()
        else:
            pass

    def show_text(self):
        if self.text != None:
            text = self.font.render(self.text, True, BUTTON_TEXT_COLOUR)
            text_size = text.get_size()
            text_x = self.x + (self.width/2) - (text_size[0]/2)
            text_y = self.y + (self.height / 2) - (text_size[1] / 2)
            self.game.screen.blit(text, (text_x, text_y))

class ButtonCenter(Button):
    def __init__(self, rect, game, width, height, bg_colour, border_colour='white', hover_colour=None, function=None, text=None):
        super().__init__(game, width, height, bg_colour, border_colour, hover_colour, function, text)
        self.rect = rect
        self.game = game
        self.x = rect[0] + rect[2]//2 - width//2
        self.y = rect[1] + rect[3]//2 - height//2
        self.width = width
        self.height = height
        self.bg_colour = bg_colour
        self.border_colour = border_colour
        self.hover_colour = hover_colour
        self.hovered = False
        self.function = function
        self.text = text
        self.font = pygame.font.SysFont('arial', BUTTON_TEXT_SIZE, bold=True)


