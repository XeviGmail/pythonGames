import random
import pygame
import pymunk
from laser import Laser

screen_width = 600
screen_height = 600

def cc(point):
    return int(point[0]), screen_height-int(point[1])

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, speed, constraint):
        super().__init__()
        self.image = pygame.image.load('../graphics/player-a-0.png')
        self.image_recharge = [pygame.image.load('../graphics/player-a-1.png'),
                               pygame.image.load('../graphics/player-a-2.png'),
                               pygame.image.load('../graphics/player-a-3.png'),
                               pygame.image.load('../graphics/player-a-4.png'),
                               pygame.image.load('../graphics/player-a-5.png'),
                               pygame.image.load('../graphics/player-a-6.png'),]
        # self.image = pygame.transform.scale(image_raw, (80,40))
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = speed
        self.min_x_constraint = constraint[0]
        self.max_x_constraint = constraint[1]
        self.min_y_constraint = constraint[2]
        self.max_y_constraint = constraint[3]

        # Laser
        self.laser_ready = True
        self.laser_time = 0
        self.laser_cooldown = 400
        self.laser_speed = 8
        self.lasers = pygame.sprite.Group()

        # reload player
        self.time_fotogram_zero = 0
        self.fotogram = 0
        self.max_fotograms = 6
        self.time_fotogram = self.laser_cooldown / self.max_fotograms

    def recharge(self):
        if not self.laser_ready:
            current_time = pygame.time.get_ticks()

            if self.time_fotogram_zero == 0:
                self.image = self.image_recharge[self.fotogram]
                self.time_fotogram_zero = current_time # 1000
            else:
                if current_time - self.time_fotogram_zero >= self.time_fotogram and self.fotogram < self.max_fotograms:
                    self.fotogram += 1
                    self.image = self.image_recharge[self.fotogram]
                    self.time_fotogram_zero = current_time

            if (current_time - self.laser_time) >= self.laser_cooldown:
                self.laser_ready = True
                self.fotogram = 0
                self.time_fotogram_zero = 0

    def get_input(self):
        keys = pygame.key.get_pressed()
        # movement of the player
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        # movement of the laser
        if keys[pygame.K_SPACE] and self.laser_ready:
            self.shoot_laser()
            self.laser_ready = False
            self.laser_time = pygame.time.get_ticks()

    def constraint(self):
        if self.rect.right >= self.max_x_constraint - 10:
            self.rect.right = self.max_x_constraint - 10
        if self.rect.left <= self.min_x_constraint + 10:
            self.rect.left = self.min_x_constraint + 10
        if self.rect.top <= self.min_y_constraint + 20:
            self.rect.top = self.min_y_constraint + 20
        if self.rect.bottom >= self.max_y_constraint - 20:
            self.rect.bottom = self.max_y_constraint - 20

    def shoot_laser(self):
        laser = Laser(self.rect.center, self.laser_speed)
        self.lasers.add(laser)

    def update(self):
        self.get_input()
        self.constraint()
        self.recharge()
        self.lasers.update()
