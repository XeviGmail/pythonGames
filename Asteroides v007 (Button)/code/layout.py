import pygame

class Layout():
    def __init__(self, screen, rect, color):
        self.screen = screen
        self.x = rect['x']
        self.y = rect['y']
        self.width = rect['width']
        self.height = rect['height']
        self.color = color
        self.layout = pygame.Surface((self.width, self.height))

    def draw(self, image, rect):
        self.screen.blit(image, rect)

    def update(self):
        self.layout.fill(self.color)
        self.screen.blit(self.layout, (self.x, self.y))
