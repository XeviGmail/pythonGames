import pygame, sys
import pymunk

if __name__ == '__main__':
    pygame.init()
    FPS = 60
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width,screen_height))
    clock = pygame.time.Clock()
    space = pymunk.Space()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill('grey')
        pygame.display.flip()
        clock.tick(FPS)
        space.step(1/FPS)
