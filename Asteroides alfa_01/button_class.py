import pygame

class Button:
    def __init__(self, pos, size, font_color, bg_color, content, fsize):
        self.pos = pos
        self.size = size
        self.font_color = font_color
        self.bg_color = bg_color
        self.content = content
        self.fsize = fsize

        self.image = pygame.Surface(self.size, False, self.fsize)
        self.image.fill(self.bg_color)
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.consolas = pygame.font.SysFont('consolas', False, self.size,)
        self.text = self.consolas.render(self.content, False, self.font_color)
        self.text_rect = self.text.get_rect(center=(self.size[0]/2, self.size[1]/2))
        self.image.blit(self.text, self.text_rect)

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False

