import pygame
from sys import exit
from settings import *
from window_class import *
from button_class import *
from text_class import *

"""
    Using the Button Class:
        1.- Create a list
        2.- Create a Function to make the buttons
            1.- fill the list with the buttons
        3.- Update all the buttons
        4.- Draw all the buttons    
"""

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SIZE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.window_info = Window(self, RECT_INFO, 'grey', 'black')
        self.window_play = Window(self, RECT_PLAY, 'grey', 'black')
        self.buttons = []
        self.make_buttons()
        self.texts = []
        self.make_texts()

    def make_texts(self):
        # Fonts
        size = 25
        consolas = pygame.font.SysFont('consolas', size)

        info_text = TextPos(self, 20, 200, 'Tararini', 'black', consolas)
        self.texts.append(info_text)
        play_text = TextLine(self, RECT_PLAY, 'Linia 0', 'blue', 0, consolas)
        self.texts.append(play_text)
        play_text = TextLineCenter(self, RECT_INFO, 'XXXXXXXXXXXXXXXXXXX', 'black', 1, consolas)
        self.texts.append(play_text)
        play_text = TextLineDouble(self, RECT_PLAY, 'Linia 4', 'blue', 'valor', 'brown', 4, consolas)
        self.texts.append(play_text)

    def make_buttons(self):
        play_button1 = Button(self, WIDTH//2, HEIGHT//2, 100, 50, (20, 121, 21), hover_colour=(49, 218, 46),function=self.play_button, text='PLAY')
        play_button = ButtonCenter(RECT_INFO, self, 100, 50, (20, 121, 21), hover_colour=(49, 218, 46),function=self.play_button, text='PLAY' )
        self.buttons.append(play_button)

    def run(self):
        while self.running:
            self.get_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    if button.hovered:
                        button.click()

    def update(self):
        for button in self.buttons:
            button.update()
        pygame.display.update()

    def draw(self):
        self.window_info.draw()
        self.window_play.draw()
        #self.window_info.write_line(1, 'CASA', 'PAPARRUCHAS')
        #self.window_play.write_line(7, 'CASA', 'PAPARRUCHAS')
        for button in self.buttons:
            button.draw()
        for text in self.texts:
            text.draw()

    def play_button(self):
        print('button pressed')
        self.running = False