import pygame
from laser import Laser
from shield import Shield

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, speed, layout, screen, images):
        super().__init__()
        self.pos = pos
        self.screen = screen
        self.speed = speed
        self.layout = layout
        self.layout_x = layout['x']
        self.layout_y = layout['y']
        self.layout_width = layout['width']
        self.layout_height = layout['height']

        # Laser
        self.laser_speed = 8
        self.laser_ready = True
        self.laser_time = 0
        self.laser_cooldown = 400
        self.lasers = pygame.sprite.Group()

        # reload player
        self.set_images(images)

        # shield
        self.shield = pygame.sprite.GroupSingle()
        self.shield_up = False
        self.shield_time = 3000
        self.shield_start = 0

    def get_input(self):
        keys = pygame.key.get_pressed()
        # movement
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            if self.shield_up:
                self.shield_sprite.rect.centerx = self.rect.centerx
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            if self.shield_up:
                self.shield_sprite.rect.centerx = self.rect.centerx
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            if self.shield_up:
                self.shield_sprite.rect.centery = self.rect.centery
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            if self.shield_up:
                self.shield_sprite.rect.centery = self.rect.centery
        # Laser
        if keys[pygame.K_SPACE] and self.laser_ready:
            self.shoot_laser(self.rect.center)
            self.laser_ready = False
            self.laser_time = pygame.time.get_ticks()

        # Shield
        if keys[pygame.K_s]:
            if not self.shield_up:
                self.shield_sprite = Shield((self.rect.centerx,self.rect.centery ), (64, 32))
                self.shield.add(self.shield_sprite)
                self.shield_up = True
                self.shield_start = pygame.time.get_ticks()

        if self.shield_up and pygame.time.get_ticks() - self.shield_start >= self.shield_time:
            self.shield_sprite.kill()
            self.shield_up = False
            # self.shield_start = 0

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

    def shoot_laser(self, pos):
        laser = Laser(pos, self.laser_speed, self.layout)
        self.lasers.add(laser)

    def constraint(self):
        if self.rect.right >= self.layout_x + self.layout_width:
            self.rect.right = self.layout_x + self.layout_width
        if self.rect.left <= self.layout_x:
            self.rect.left = self.layout_x
        if self.rect.top <= self.layout_y:
            self.rect.top = self.layout_y
        if self.rect.top >= self.layout_y + self.layout_height - self.rect.height:
            self.rect.top = self.layout_y + self.layout_height - self.rect.height

    def update(self):
        self.get_input()
        self.constraint()
        self.shield.update()
        self.shield.draw(self.screen)
        self.recharge()
        self.lasers.update()
        self.lasers.draw(self.screen)

