import math

import pygame

class Residuo(pygame.sprite.Sprite):
    def __init__(self, pos, radius, velocity, layout):
        super().__init__()
        self.x = pos[0]
        self.y = pos[1]
        self.layout_x = layout['x']
        self.layout_y = layout['y']
        self.layout_width = layout['width']
        self.layout_height = layout['height']
        self.velocity = velocity
        self.radius = radius
        image_raw = pygame.image.load('../graphics/rocks/residuos00.png')
        self.image = pygame.transform.scale(image_raw, (2 * self.radius, 2 * self.radius))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.velocityx = self.x
        self.velocityy = 0

    def bounds(self):
        bound_left = self.layout_x - self.rect.width
        bound_right = self.layout_x + self.layout_width + self.rect.width
        bound_top = - self.rect.height
        bound_bottom = self.layout_y + self.layout_height + self.rect.height

        if self.rect.x <= bound_left or self.rect.x >= bound_right or self.rect.y <= bound_top or self.rect.y >= bound_bottom:
            self.out_of_bounds = True

    def update(self):
        self.velocityx += 1/60 * self.velocity[0]
        self.rect.x = self.velocityx
        self.velocityy += 1/60 * self.velocity[1]
        self.rect.y = self.y - self.velocityy
        self.bounds()
