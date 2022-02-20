import pygame
from sys import exit
from player import Player

class Game:
    def __init__(self):
        player_sprite = Player((300, 300))
        self.player = pygame.sprite.GroupSingle(player_sprite)
    def run(self):
        self.player.draw(screen)

if __name__ == '__main__':
    width = 600
    height = 600
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Space War Training')
    clock = pygame.time.Clock()
    game = Game()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill('grey')
        game.run()
        pygame.display.flip() # Update the entire display
        clock.tick(60)