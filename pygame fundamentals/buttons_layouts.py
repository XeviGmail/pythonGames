import pygame, sys
vec = pygame.math.Vector2

width, height = 800, 500
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Button Demo')
btn_image = pygame.image.load('./graphics/Player/player_stand.png')
padding = 10

class ButtonText():
    def __init__(self, x, y, w, h, text, color):
        self.font = pygame.font.SysFont('consolas', 30)
        self.color = color
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.top_rect = pygame.Rect((x, y), (w, h))
        self.text_surf = self.font.render(text, True, 'blue')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self, layout):
        pygame.draw.rect(layout, self.color, self.top_rect)
        layout.blit(self.text_surf, self.text_rect)

class Button():
    def __init__(self, pos, image, layout):
        self.pos = layout.x
        self.layout = layout
        self.image = image
        self.rect = self.image.get_rect(topleft=(layout.x + pos[0], layout.y + pos[1]))
    def draw(self):
        self.layout.draw(self.image, (self.rect.x, self.rect.y))

class TextBox():
    def __init__(self, x, y, w, h, bg_color):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.pos = vec(x, y)
        self.size = vec(w, h)
        self.image = pygame.Surface((w, h))
        self.bg_color = bg_color

    def draw(self, screen):
        self.image.fill(self.bg_color)
        screen.blit(self.image, self.pos)

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
        print(self.x, self.y)
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
    text_box = TextBox(100, 200, 200, 200, 'blue')

    while not end_dock:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                end_dock = True
        screen.fill('grey')

        # layout_dock.update()
        text_box.draw(layout_dock.layout)
        # button.draw()
        pygame.display.flip()
        clock.tick(60)