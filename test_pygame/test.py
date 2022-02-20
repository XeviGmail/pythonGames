import pygame
from sys import exit

class Pelota(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('basketball.png').convert_alpha()
        self.rect = self.image.get_rect(center=pos)

class Game:
    def __init__(self):
        pelota_sprite = Pelota((300,300))
        self.pelota = pygame.sprite.Group()
        self.pelota.add(pelota_sprite)

    def run(self):
        self.pelota.draw(screen)

if __name__ == '__main__':
    pygame.init()
    speed = 5
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Testing Pygame')
    clock = pygame.time.Clock()
    game = Game()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill((30,30,30))
        game.run()
        pygame.display.flip()
        clock.tick(60)
