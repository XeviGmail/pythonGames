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

    score_font = pygame.font.Font('./font/Pixeltype.ttf', 50)
    score_surf = score_font.render('My Score', False, 'Black')
    score_rect = score_surf.get_rect(center=(WIDTH//2, score_surf.get_height()))

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
            if event.type == pygame.MOUSEMOTION:
                print(event.pos)
                if player_rect.collidepoint(event.pos):
                    print('mouse sobre player')
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('mouse down')
            if event.type == pygame.MOUSEBUTTONUP:
                print('mouse UP')
        if snail_rect.left <= 0 - snail_surf.get_width():
            snail_rect.left = WIDTH

        # Collisions
        # Collisioning two rectangles
        if player_rect.colliderect(snail_rect):
            print('snail collision')
            running = False

        screen.blit(sky, (0,0))
        screen.blit(ground, (0, HEIGHT - ground.get_height()))
        screen.blit(player_surf, player_rect)
        screen.blit(snail_surf, snail_rect)
        screen.blit(score_surf, score_rect)
        snail_rect.left -= 1
        pygame.display.update()
        clock.tick(FPS)