# TUTORIAL
# https://www.youtube.com/watch?v=hDu8mcAlY4E

import pygame, sys

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.gunshoot = pygame.mixer.Sound('./assets/Shot.wav')

    def shoot(self):
        self.gunshoot.play()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

# General Setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 1920 / 2
screen_height = 1080 / 2
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Dianes')
background = pygame.image.load('./assets/space.png')
pygame.mouse.set_visible(False)

# Crosshair
crosshair = Crosshair('./assets/green.png')
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()

    screen.blit(background, (0,0))
    crosshair_group.draw(screen)
    crosshair_group.update()
    pygame.display.flip()
    clock.tick(60)