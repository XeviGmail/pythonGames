import pygame, pymunk

class Rock(pygame.sprite.Sprite):
    def __init__(self, space, pos, velocity, radius, layout):
        super().__init__()
        self.space = space
        self.x = pos[0]
        self.y = pos[1]
        self.layout_x = layout['x']
        self.layout_y = layout['y']
        self.layout_width = layout['width']
        self.layout_height = layout['height']
        self.radius = radius
        self.body = pymunk.Body()
        self.body.position = self.cc(pos) # x, y
        self.body.velocity = velocity
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.elasticity = 1
        self.shape.density = 1
        self.space.add(self.body, self.shape)

        image_raw = pygame.image.load('../graphics/rocks/rock0.png')
        self.image = pygame.transform.scale(image_raw, (2 * radius, 2 * radius))
        self.rect = self.image.get_rect()

        self.out_of_bounds = False

    def bounds(self):
        bound_left = self.layout_x - self.rect.width
        bound_right = self.layout_x + self.layout_width + self.rect.width
        bound_top = - self.rect.height
        bound_bottom = self.layout_y + self.layout_height + self.rect.height

        if self.rect.x <= bound_left or self.rect.x >= bound_right or self.rect.y <= bound_top or self.rect.y >= bound_bottom:
            print(f'eliminar {self.rect.x} <= {bound_left} >= {bound_right} {self.rect.y}<={bound_top} >= {bound_bottom}')
            self.out_of_bounds = True

    def get_out_of_bounds(self):
        return self.out_of_bounds

    def set_out_of_bounds(self, value):
        self.out_of_bounds = value

    def eliminar(self):
        self.kill()
        self.space.remove(self.body, self.shape)

    def cc(self, point):
        return int(point[0]), self.layout_height - int(point[1])

    def update(self):
        x, y = self.cc(self.body.position)
        self.rect.x = x - self.radius
        self.rect.y = y - self.radius
        self.bounds()

