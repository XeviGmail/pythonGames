import random

import pygame
from laser import Laser

class Enemy(pygame.sprite.Sprite):
    def __init__(self, space, pos):
        super().__init__()
        self.space = space
        self.x = pos[0]
        self.y = pos[1]
        self.size_x = 64
        self.size_y = 32
        image_raw = pygame.image.load('../graphics/enemies/01/enemy01.png')
        self.image = pygame.transform.scale(image_raw, (self.size_x, self.size_y))
        self.rect = self.image.get_rect(midbottom=pos)

    def set_velocity(self, velocity):
        self.velocity = velocity


    def update(self):
        self.rect.y += 1



