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

    player_surf = pygame.image.load('./graphics/Player/player_stand.png').convert_alpha()
    player_pos_x = player_surf.get_width()
    player_pos_y = HEIGHT - ground.get_height()
    player_rect = player_surf.get_rect(midbottom=(player_pos_x, player_pos_y))

    snail_surf = pygame.image.load('./graphics/snail/snail1.png').convert_alpha()
    snail_pos_x = WIDTH - snail_surf.get_width()
    snail_pos_y = HEIGHT - ground.get_height()
    snail_rect = snail_surf.get_rect(midbottom=(snail_pos_x, snail_pos_y))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        if snail_rect.left <= 0 - snail_surf.get_width():
            snail_rect.left = WIDTH

        # Collisions
        # Collisioning two rectangles
        if player_rect.colliderect(snail_rect):
            print('snail collision')
        # Collissioning the mouse with a rect
        mouse_pos = pygame.mouse.get_pos()
        if player_rect.collidepoint(mouse_pos):
            print('mouse collission')

        screen.blit(sky, (0,0))
        screen.blit(ground, (0, HEIGHT - ground.get_height()))
        screen.blit(player_surf, player_rect)
        screen.blit(snail_surf, snail_rect)
        snail_rect.left -= 3
        pygame.display.update()
        clock.tick(FPS)