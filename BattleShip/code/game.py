import pygame, os
from sys import exit
from background import B
# def draw_window():
#     SCREEN.blit(BACKGROUND, (0, 0))
#     pygame.display.update()

if __name__ == '__main__':
    pygame.init()
    FPS = 60
    SCREEN_WIDTH, SCREEN_HEIGHT = 900,   500
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Battle Ship')

    CLOCK = pygame.time.Clock()

    SPACE = pygame.image.load('../Assets/space.png').convert()
    BACKGROUND = pygame.transform.scale(SPACE, (SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # draw_window()
        pygame.display.flip()
        CLOCK.tick(FPS)

