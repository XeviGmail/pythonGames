import pygame

class Draw():
    def __init__(self, layout):
        self.layout = layout

    def button_image(self, pos, image, size):
        pos = (self.layout.x + pos[0], self.layout.y + pos[1])
        image = pygame.transform.scale(image, size)
        rect = image.get_rect(topleft=pos)
        self.layout.draw(image, (rect.x, rect.y))

    def line(self, line, label, value, font, colorl, colorv=''):
        colorv = colorl if colorv == '' else colorv
        padding = 10
        # Etiqueta
        image_label = font.render(label, 1, colorl)
        rect_label = image_label.get_rect(
            topleft=(self.layout.x + padding, self.layout.y + line * (font.get_linesize() + int(font.get_linesize() / 2))))
        # Valor
        image_value = font.render(value, 1, colorv)
        rect_value = image_value.get_rect(
            topright=(self.layout.width - padding, self.layout.y + line * (font.get_linesize() + int(font.get_linesize() / 2))))
        self.layout.draw(image_label, rect_label)
        self.layout.draw(image_value, rect_value)

    def line_box(self, pos, text, font, color):
        """
            Dibula el texto donde le digamos
        """
        image = font.render(text, 1, color)
        rect = image.get_rect(topleft=(self.layout.x + pos[0], self.layout.y + pos[1]))
        self.layout.draw(image, rect)