import pygame
from sys import exit

WHIDTH , HEIGHT = 800,800
SIZE = (WHIDTH , HEIGHT)
FPS = 60

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption('Classing the Game')
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            self.get_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
    def update(self):
        pygame.display.update()

    def draw(self):
        pass

if __name__ == '__main__':
    game = Game()
    game.run()