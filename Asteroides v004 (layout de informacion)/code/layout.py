import pygame

class Layout():
    def __init__(self, screen, x, y, width, height, color):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.layout = pygame.Surface((width, height))
        # Fonts
        self.size = 25
        self.consolas = pygame.font.SysFont('consolas', self.size)

    def write(self, line, label, value=''):
        padding = 10
        # Etiqueta
        image = self.consolas.render(label, 1, 'red')
        rect = image.get_rect(topleft=(self.x + padding, self.y + line * (self.size + self.size/2)))
        self.draw(image, rect)
        # Valor
        image = self.consolas.render(value, 1, 'red')
        rect = image.get_rect(topright=(self.width - padding, self.y + line * (self.size + self.size/2)))
        self.draw(image, rect)

    def draw(self, image, rect):
        self.screen.blit(image, rect)

    def update(self):
        self.layout.fill(self.color)
        self.screen.blit(self.layout, (self.x, self.y))
