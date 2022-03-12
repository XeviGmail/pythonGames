import pygame
from settings import *

class Button:
    def __init__(self, game, x, y, width, height, bg_colour, border_colour=(0,0,0), hover_colour=None, function=None, text=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.bg_colour = bg_colour
        self.game = game
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.function = function
        self.hover_colour = hover_colour
        self.border_colour = border_colour
        self.text = text
        self.hovered = False
        self.font = pygame.font.SysFont('arial', BUTTON_TEXT_SIZE, bold=True)

    def update(self):
        cursor = pygame.mouse.get_pos()
        if self.x + self.width > cursor[0] > self.x and self.y + self.height > cursor[1] > self.y:
            self.hovered = True
        else:
            self.hovered = False

    def draw(self):
        if self.hovered:
            pygame.draw.rect(self.game.screen, self.bg_colour, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(self.game.screen, self.hover_colour, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(self.game.screen, self.border_colour,(self.x, self.y, self.width, self.height), 2)
        self.show_text()

    def click(self):
        if self.function != 0:
            self.function()

    def show_text(self):
        if self.text != None:
            text = self.font.render(self.text, True, BUTTON_TEXT_COLOUR)
            text_size = text.get_size()
            text_x = self.x + (self.width / 2) - (text_size[0]/2)
            text_y = self.y + (self.height / 2) - (text_size[1] / 2)
            self.game.screen.blit(text, (text_x, text_y))



