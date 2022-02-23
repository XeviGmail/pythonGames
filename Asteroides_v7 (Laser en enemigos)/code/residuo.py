import math

import pygame

class Residuo(pygame.sprite.Sprite):
    def __init__(self, x, y, rock_radius, velocity):
        super().__init__()
        self.x = x
        self.y = y
        self.velocity = velocity
        self.rock_radius = rock_radius
        image_raw = pygame.image.load('../graphics/rocks/residuos00.png')
        self.image = pygame.transform.scale(image_raw, (2 * self.rock_radius, 2 * self.rock_radius))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.velocityx = self.x
        self.velocityy = 0

    def update(self):

        self.velocityx += 1/60 * self.velocity[0]
        self.rect.x = self.velocityx

        self.velocityy += 1/60 * self.velocity[1]
        self.rect.y = self.y - self.velocityy
