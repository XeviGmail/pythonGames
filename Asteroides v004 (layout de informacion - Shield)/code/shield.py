import pygame

class Shield(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        image_raw = pygame.image.load('../graphics/ship/01/shield00.png')
        self.image = pygame.transform.scale(image_raw, (128,64))
        self.rect = self.image.get_rect(center=pos)


    def update(self):
        pass

