import random

import pygame

class Rock(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.original_image = pygame.image.load('../rocks/rock0.png')
        start_angle = random.randrange(0, 360)
        self.image = pygame.transform.rotate(self.original_image, start_angle)
        self.rect = self.image.get_rect()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.rect.x = random.randrange(self.screen_width - self.rect.width)
        self.speedy = random.randrange(1, 4)
        self.speedx = random.randrange(-1, 1)
        self.rotate_speed = random.randrange(-2, 2)
        self.angle = start_angle

    def destroy(self):
        pass

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        self.angle += self.rotate_speed
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        if self.rect.top > self.screen_height + 10 or self.rect.left < -25 or self.rect.right > self.screen_width + 25:
            self.rect.x = random.randrange(self.screen_width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 4)
            self.speedx = random.randrange(-2, 2)
