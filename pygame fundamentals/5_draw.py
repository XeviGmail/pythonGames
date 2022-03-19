import pygame
from sys import exit

WIDTH, HEIGHT = 800, 800
SIZE = (WIDTH, HEIGHT)
FPS = 60

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    screen.fill('white')
    pygame.display.set_caption('Draw method')
    clock = pygame.time.Clock()
    image1_surf = pygame.image.load('./graphics/Player/player_stand.png')
    image1_rect = image1_surf.get_rect(center=(500, 200))
    image2_surf = pygame.image.load('./graphics/Player/player_walk_1.png')
    image2_rect = image2_surf.get_rect(center=(500, 400))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        pygame.draw.line(screen, 'green', (0, 0), (WIDTH, HEIGHT), 10)
        pygame.draw.circle(screen, 'red', (100, 100), 100)
        pygame.draw.rect(screen, 'blue', image1_rect)
        pygame.draw.rect(screen, 'magenta', image2_rect, 5, 60) # dibuja el marco con ancho de linia 5 con borde redondeado de radio 60
        pygame.draw.ellipse(screen, 'brown', pygame.Rect(50, 300, 100, 200))
        screen.blit(image1_surf, image1_rect)
        screen.blit(image1_surf, (200, 500))
        pygame.display.update()
        clock.tick(FPS)

