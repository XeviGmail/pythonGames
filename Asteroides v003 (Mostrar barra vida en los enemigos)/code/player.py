import random
import pygame
import pymunk
from laser import Laser

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, speed, constraint, images, screen_width, screen_height):
        super().__init__()
        self.life = 100
        self.power = 20
        self.pos = pos
        self.speed = speed
        self.min_x_constraint = constraint[0]
        self.max_x_constraint = constraint[1]
        self.min_y_constraint = constraint[2]
        self.max_y_constraint = constraint[3]
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Laser
        self.laser_ready = True
        self.laser_time = 0
        self.laser_cooldown = 400
        self.laser_speed = 8
        self.lasers = pygame.sprite.Group()

        # reload player
        self.set_images(images)

        self.num_laser = 1

    def substract_life(self, power):
        self.life -= power
        if self.life < 0:
            self.life = 0

    def get_power(self):
        return self.power

    def get_life(self):
        return self.life

    def is_dead(self):
        return True if self.life <= 0 else False

    def set_images(self, images):
        self.max_fotograms = len(images)
        self.image = images[self.max_fotograms-1]
        self.image_recharge = images
        self.rect = self.image.get_rect(midbottom=self.pos)
        self.time_fotogram_zero = 0
        self.fotogram = 0
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
                self.image = self.image_recharge[self.max_fotograms-1]

    def set_num_laser(self, num):
        self.num_laser = num

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
            if self.num_laser == 1:
                self.shoot_laser(self.rect.center)
            elif self.num_laser == 2:
                self.shoot_laser(self.rect.midright)
                self.shoot_laser(self.rect.midleft)
            elif self.num_laser == 3:
                self.shoot_laser((self.rect.centerx, self.rect.centery - 10))
                self.shoot_laser(self.rect.midright)
                self.shoot_laser(self.rect.midleft)

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

    def shoot_laser(self, pos):
        laser = Laser(pos, self.laser_speed, 'red', self.power, self.screen_width, self.screen_height)
        self.lasers.add(laser)

    def cc(self, point):
        return int(point[0]), self.screen_height - int(point[1])

    def update(self):
        self.get_input()
        self.constraint()
        self.recharge()
        self.lasers.update()

