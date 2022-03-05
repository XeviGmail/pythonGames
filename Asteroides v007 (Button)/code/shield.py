import pygame, pymunk

class Shield(pygame.sprite.Sprite):
    def __init__(self, space, pos, velocity, radius, layout):
        super().__init__()
        self.layout_x = layout['x']
        self.layout_y = layout['y']
        self.layout_width = layout['width']
        self.layout_height = layout['height']
        self.space = space
        self.radius = radius
        self.body = pymunk.Body()
        self.body.position = self.cc(pos)  # x, y
        self.body.velocity = velocity
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.elasticity = 1
        self.shape.density = 1
        self.space.add(self.body, self.shape)
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        image_raw = pygame.image.load('../graphics/ship/01/round shield.png')
        self.image = pygame.transform.scale(image_raw, (radius*2, radius*2))
        self.rect = self.image.get_rect(center=pos)

    def cc(self, point):
        return int(point[0]), self.layout_height - int(point[1])

    def update(self):
        self.body.position = self.cc((self.rect.centerx, self.rect.centery))

