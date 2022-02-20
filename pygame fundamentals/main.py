# https://www.youtube.com/watch?v=AY9MnQ4x3zk
import pygame
from sys import exit

# pygame.mouse.get_pressed() -> which mouse button is pressed

def display_score():
    current_time = pygame.time.get_ticks()
    print(current_time)

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Titulo del juego')
clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf',50)
game_active = True

sky_surface =  pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

score_surface = font.render('My game', False, 'Black')
score_rectangle = score_surface.get_rect(center=(400, 50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom=(600, 300))

player_surface = pygame.image.load('graphics/Player/player_walk_1.png')
player_rectangle = player_surface.get_rect(midbottom=(80, 300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rectangle.collidepoint(event.pos):
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rectangle.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rectangle.x = 800

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0,300))

        pygame.draw.rect(screen, 'Pink', score_rectangle)
        pygame.draw.rect(screen, 'Pink', score_rectangle, 20)
        # pygame.draw.line(screen, 'Gold', (0,0), pygame.mouse.get_pos(),10)
        # pygame.draw.ellipse(screen, 'Brown', pygame.Rect(50, 200, 100, 100))
        screen.blit(score_surface, score_rectangle)
        snail_rectangle.right -= 4
        if snail_rectangle.right <= -0:
            snail_rectangle.left = 800
        screen.blit(snail_surface, snail_rectangle)

        # player
        player_gravity += 1
        player_rectangle.y += player_gravity

        if player_rectangle.bottom >= 300:
            player_rectangle.bottom = 300
        screen.blit(player_surface, player_rectangle)

        #collision
        if snail_rectangle.colliderect(player_rectangle):
            game_active = False
    else:
        screen.fill('Yellow')
    pygame.display.update()
    clock.tick(60)