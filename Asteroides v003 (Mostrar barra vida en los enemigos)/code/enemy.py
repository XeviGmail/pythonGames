import random

import pygame
from laser import Laser

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, life, power, screen):
        super().__init__()
        self.life = life
        self.max_life = life
        self.screen = screen
        self.power = power
        self.x = pos[0]
        self.y = pos[1]
        self.size_x = 64
        self.size_y = 32
        image_raw = pygame.image.load('../graphics/enemies/01/enemy01.png')
        self.image = pygame.transform.scale(image_raw, (self.size_x, self.size_y))
        self.rect = self.image.get_rect(midbottom=pos)

    def life_bar(self):
        pygame.draw.rect(self.screen, 'red', (self.rect.x, self.rect.y - 20, self.rect.width, 10))
        num = self.rect.width/self.max_life
        pygame.draw.rect(self.screen, 'green', (self.rect.x, self.rect.y - 20, self.rect.width - (self.rect.width -(num*self.life)) , 10))

    def get_power(self):
        return self.power

    def get_life(self):
        return self.life

    def substract_life(self, power):
        self.life -= power
        if self.life < 0:
            self.life = 0

    def is_dead(self):
        return True if self.life <= 0 else False

    def set_velocity(self, velocity):
        self.velocity = velocity

    def update(self):
        self.rect.y += 1
        self.life_bar()


