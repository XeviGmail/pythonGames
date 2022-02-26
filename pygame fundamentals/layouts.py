# https://www.youtube.com/watch?v=A6eSzbllWbM

import pygame
from sys import exit

padding = 10
width = 1024
height = 800
pygame.init()
screen = pygame.display.set_mode((width, height))
rect_info = {
    'x': padding, # posicion inicial X
    'y': padding, # posicion inicial Y
    'width': int((width-padding) / 3) - 2 * padding, # distancia x
    'height': height - 2 * padding, # distancia y
}
rect_info = pygame.Rect(rect_info['x'], rect_info['y'], rect_info['width'], rect_info['height'])
rect_play = {
    'x': int((width-padding) / 3),
    'y': padding,
    'width': 2 * int((width-padding) / 3),
    'height': height - (2 * padding),
}
rect_play = pygame.Rect(rect_play['x'], rect_play['y'], rect_play['width'], rect_play['height'])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # layout_info()
    screen.fill('grey')
    pygame.draw.rect(screen, 'black', rect_info)
    # pygame.draw.rect(screen, 'red', rect_info, 2)
    pygame.draw.rect(screen, 'black', rect_play)
    # pygame.draw.rect(screen, 'red', rect_play, 2)
    pygame.display.update()

