import pygame, sys
size = (800, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Button Demo')
btn_image = pygame.image.load('./graphics/Player/player_stand.png')

class Button():
    def __init__(self, pos, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

button = Button((100, 200), btn_image)
if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    end_dock = False
    while not end_dock:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                end_dock = True
        screen.fill('grey')
        button.draw()
        pygame.display.update()
        clock.tick(60)