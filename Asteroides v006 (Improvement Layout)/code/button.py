import pygame

class Button():
    def __init__(self, layout, pos, image, size):
        self.layout = layout
        self.pos = pos
        self.image = pygame.transform.scale(image, size)
        self.rect = self.image.get_rect(topleft=pos)

    def draw(self):
        self.layout.draw(self.image, self.rect)
