import pygame
from sys import exit

WIDTH, HEIGHT = 800, 400
SIZE = (WIDTH, HEIGHT)
FPS = 60

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Snail')
    clock = pygame.time.Clock()
    running = True

    sky = pygame.image.load('./graphics/Sky.png').convert()
    ground = pygame.image.load('./graphics/ground.png').convert()
    snail = pygame.image.load('./graphics/snail/snail1.png').convert_alpha()
    snail_pos_x = WIDTH-snail.get_width()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        screen.blit(sky, (0,0))
        screen.blit(ground, (0, HEIGHT - ground.get_height()))
        screen.blit(snail, (snail_pos_x, HEIGHT - ground.get_height() - snail.get_height()))
        snail_pos_x -= 1
        pygame.display.update()
        clock.tick(FPS)