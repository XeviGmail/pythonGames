import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, speed, layout):
        super().__init__()
        self.speed = speed
        self.layout_x = layout['x']
        self.layout_y = layout['y']
        self.layout_width = layout['width']
        self.layout_height = layout['height']
        image = pygame.image.load('../graphics/ship/01/nave-1-15.png')
        self.image = pygame.transform.scale(image, (image.get_width()*2, image.get_height()*2))
        self.rect = self.image.get_rect(midbottom=pos)

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

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
