import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, speed, layout):
        super().__init__()
        self.layout_x = layout['x']
        self.layout_y = layout['y']
        self.layout_width = layout['width']
        self.layout_height = layout['height']
        self.image = pygame.Surface((4, 15))
        self.image.fill('red')
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed

    def bounds(self):
        bound_left = self.layout_x - self.rect.width
        bound_right = self.layout_x + self.layout_width + self.rect.width
        bound_top = - self.rect.height
        bound_bottom = self.layout_y + self.layout_height + self.rect.height

        if self.rect.x <= bound_left or self.rect.x >= bound_right or self.rect.y <= bound_top or self.rect.y >= bound_bottom:
            self.kill()

    def update(self):
        self.rect.y -= self.speed
        self.bounds()