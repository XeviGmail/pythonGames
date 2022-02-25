import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, speed, color, power, screen_width, screen_height):
        super().__init__()
        self.power = power
        self.image = pygame.Surface((4, 20))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed
        self.screen_width = screen_width
        self.screen_height = screen_height

    def destroy(self):
        if self.rect.y <= -50 or self.rect.y >= self.screen_height + 50:
            self.kill()

    def get_power(self):
        return self.power

    def update(self):
        self.rect.y -= self.speed
        self.destroy()
