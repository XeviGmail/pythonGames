# https://www.youtube.com/watch?v=A6eSzbllWbM

import pygame
from sys import exit

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('player-a-0.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

padding = 10
width = 1024
height = 800
pygame.init()
screen = pygame.display.set_mode((width, height))
info_surf = {
    'x': padding, # posicion inicial X
    'y': padding, # posicion inicial Y
    'width': int((width-padding) / 3) - 2 * padding, # distancia x
    'height': height - 2 * padding, # distancia y
}
surf_info = pygame.Surface((info_surf['width'], info_surf['height']))
play_surf = {
    'x': int((width-padding) / 3),
    'y': padding,
    'width': 2 * int((width-padding) / 3),
    'height': height - (2 * padding),
}
surf_play = pygame.Surface((play_surf['width'], play_surf['height']))

player_sprite = Player(500, 500)
player = pygame.sprite.GroupSingle(player_sprite)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # layout_info()
    screen.fill('grey')
    surf_info.fill('green')
    screen.blit(surf_info, (info_surf['x'], info_surf['y']))
    surf_play.fill('green')
    screen.blit(surf_play, (play_surf['x'], play_surf['y']))
    player.draw(screen)
    surf_info.fill('green')
    screen.blit(surf_info, (info_surf['x'], info_surf['y']))
    pygame.display.update()

