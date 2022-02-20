import pygame

class Background():
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        image = pygame.image.load('../Assets/space.png')
        self.image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.image.get_rect(midbottom=(0,0))
