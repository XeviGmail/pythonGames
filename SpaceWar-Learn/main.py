import pygame
from sys import exit

width = 800
height = 800
pygame.init()
screen = pygame.display.set_mode((width, height))
screen.fill('grey')
pygame.display.set_caption('Space War')
clock = pygame.time.Clock()
nave_surf = pygame.image.load('Spaceships/nave-b-0.png').convert_alpha()

nave_surf_x = 350
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                nave_surf_x -= 1

    screen.fill('grey')
    screen.blit(nave_surf, (nave_surf_x,700))

    pygame.display.update()
    clock.tick(60)