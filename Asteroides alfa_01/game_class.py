import pygame
from sys import exit
from settings import *
from game_window_class import *
from intro_window_class import *

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.game_window = GameWindow(self)
        self.intro_window = IntroWindow(self)
        self.running = True
        self.state = 'game'

    def run(self):
        while self.running:
            self.get_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
        exit()

    def get_events(self):
        if self.state == 'intro':
            self.intro_events()

    def update(self):
        pass

    def draw(self):
        if self.state == 'intro':
            self.intro_window.draw()
        if self.state == 'game':
            self.game_window.draw()
        pygame.display.update()

# ------------------------------------------------- INTRO ------------------------------------------------------------ #

    def intro_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                print('aquistoiy')
                self.state == 'game'

