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

        # Laser
        self.laser_time = 0
        self.laser_cooldown = random.randrange(500, 2000)
        self.laser_speed = -8
        self.laser_time_shoot = pygame.time.get_ticks()
        self.laser_ready = False
        self.lasers = pygame.sprite.Group()

    def set_velocity(self, velocity):
        self.velocity = velocity

    def recharge(self):
        if self.laser_ready:
            self.shoot_laser(self.rect.center)
            self.laser_ready = False
            self.laser_time_shoot = pygame.time.get_ticks()
        else:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time_shoot > self.laser_cooldown:
                self.laser_ready = True


    def shoot_laser(self, pos):
        laser = Laser(pos, self.laser_speed, 'blue')
        self.lasers.add(laser)

    def update(self):
        self.rect.y += 1
        self.lasers.update()
        self.recharge()



