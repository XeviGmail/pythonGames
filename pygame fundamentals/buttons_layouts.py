import pygame, sys
width, height = 800, 500
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Button Demo')
btn_image = pygame.image.load('./graphics/Player/player_stand.png')
padding = 10

class Button():
    def __init__(self, pos, image, layout):
        self.pos = layout.x
        self.layout = layout
        self.image = image
        self.rect = self.image.get_rect(topleft=(layout.x + pos[0], layout.y + pos[1]))
    def draw(self):
        self.layout.draw(self.image, (self.rect.x, self.rect.y))

class Layout():
    def __init__(self, screen, rect, color):
        self.screen = screen
        self.x = rect['x']
        self.y = rect['y']
        self.width = rect['width']
        self.height = rect['height']
        self.color = color
        self.layout = pygame.Surface((self.width, self.height))
        # Fonts
        self.size = 25
        self.consolas = pygame.font.SysFont('consolas', self.size)

    def draw(self, image, rect):
        self.screen.blit(image, rect)

    def update(self):
        self.layout.fill(self.color)
        self.screen.blit(self.layout, (self.x, self.y))

if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    end_dock = False
    layout_dock_rect = {
        'x': 200,
        'y': padding,
        'width': 400,
        'height': 400
    }
    layout_dock = Layout(screen, layout_dock_rect, 'white')
    button = Button((0, 0), btn_image, layout_dock)

    while not end_dock:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                end_dock = True
        screen.fill('grey')
        layout_dock.update()
        button.draw()
        pygame.display.update()
        clock.tick(60)