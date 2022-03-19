import pygame
from sys import exit

WIDTH, HEIGHT = 800, 800
SIZE = (WIDTH, HEIGHT)
FPS  = 60

class Button1:
    def __init__(self, pos, size, text):
        self.pos = pos
        self.size = size
        self.font = pygame.font.Font(None, 30)
        self.btn_text = self.font.render(text, False, 'yellow',)
        self.btn_rect = self.btn_text.get_rect(center=pos)

    def draw(self):
        pygame.draw.rect(screen, 'black', self.btn_rect)
        screen.blit(self.btn_text, self.btn_rect)
        print(self.btn_rect.height)

class Button:
    def __init__(self, pos, size, text):
        self.pos = pos
        self.size = size
        self.button_rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.font = pygame.font.Font(None, 30)
        self.btn_text = self.font.render(text, False, 'yellow')
        self.btn_text_width = self.btn_text.get_width()
        self.btn_text_height = self.btn_text.get_height()

    def draw(self):
        pygame.draw.rect(screen, 'black', self.button_rect)
        x = self.pos[0] + (self.size[0] - self.btn_text_width)//2
        y = self.pos[1] + (self.size[1] - self.btn_text_height)//2
        screen.blit(self.btn_text,(x, y))


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    screen.fill('white')
    pygame.display.set_caption('Buttons')
    clock = pygame.time.Clock()
    button = Button((300, 300), (200, 100), 'PAPARRUCHAS')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        button.draw()
        pygame.display.flip()
        clock.tick(FPS)
