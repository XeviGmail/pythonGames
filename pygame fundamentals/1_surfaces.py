import pygame
from sys import exit

WIDTH, HEIGHT = 800, 800
SIZE = (WIDTH, HEIGHT)
FPS = 60

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('BUTTONS')
    clock = pygame.time.Clock()

# surface with plain color
    rectangle = pygame.Surface((100,100))
    rectangle.fill('green') #by default is filled with 'black'
# Surface with image
    player_image = pygame.image.load('./graphics/Player/player_stand.png') # Image incluye una superficie
# Surface with text (first create the image of the text and then place it on the display surface)
# 1.- create a font
# 2.- write text on a surface
# 3.- blit the text surface
    font_text = pygame.font.Font('./font/Pixeltype.ttf', 50) # None = default font
    text = font_text.render('Hello Pygame', False, 'blue')

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        screen.blit(rectangle, (300,300))
        screen.blit(player_image, (100,100))
        screen.blit(text, (400, 100))

        pygame.display.update() # updatea lo que hay en display
        clock.tick(FPS)