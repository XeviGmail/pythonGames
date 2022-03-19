import pygame
from settings import *

class Text:
    def __init__(self, game, text, colour, font):
        self.game = game
        self.text = text
        self.colour = colour
        self.font = font

    def update(self):
        pass

class TextPos(Text):
    def __init__(self, game, x, y, text, colour, font):
        super().__init__(game, text, colour, font)
        self.x = x
        self.y = y

    def draw(self):
        surf = self.font.render(self.text, False, self.colour)
        rect = surf.get_rect(topleft=(self.x, self.y))
        self.game.screen.blit(surf, rect)

class TextLine(Text):
    def __init__(self, game, rect, text, colour, line, font):
        super().__init__(game, text, colour, font)
        self.rect = rect
        self.line = line

    def draw(self):
        surf = self.font.render(self.text, False, self.colour)
        rect = surf.get_rect(topleft=(self.rect[0] + PADDING_LINE, self.rect[1] + self.line * (self.font.get_height() + self.font.get_height() / 2)))
        self.game.screen.blit(surf, rect)

class TextLineDouble(Text):
    def __init__(self, game, rect, text, colour, text_right, colour_right, line, font):
        super().__init__(game, text, colour, font)
        self.rect = rect
        self.line = line
        self.text_right = text_right
        self.colour_right = colour_right

    def draw(self):
        # text left
        surf = self.font.render(self.text, False, self.colour)
        rect = surf.get_rect(topleft=(self.rect[0] + PADDING_LINE, self.rect[1] + self.line * (self.font.get_height() + self.font.get_height() / 2)))
        self.game.screen.blit(surf, rect)
        # text right
        surf = self.font.render(self.text_right, False, self.colour_right)
        rect = surf.get_rect(topright=(self.rect[0]-PADDING + self.rect[2] - PADDING_LINE, self.rect[1] + self.line * (self.font.get_height() + self.font.get_height()/2)))
        self.game.screen.blit(surf, rect)

class TextLineCenter(Text):
    def __init__(self, game, rect, text, colour, line, font):
        super().__init__(game, text, colour, font)
        self.rect = rect
        self.line = line

    def draw(self):
        surf = self.font.render(self.text, False, self.colour)
        x = self.rect[0] + self.rect[2]//2
        y = self.rect[1] + self.line * (self.font.get_height() + self.font.get_height() / 2)
        rect = surf.get_rect(center=(x, 300))
        self.game.screen.blit(surf, rect)