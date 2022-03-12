import pygame
from sys import exit
from settings import *
from button_class import *
from game_window_class import *
from snake_class import *
from food_class import *

class Game():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.running = True
        self.state = 'intro'
        self.intro_buttons = []
        self.playing_buttons = []
        self.dead_buttons = []

        self.active_buttons = self.intro_buttons
        self.game_window = GameWindow(self)
        self.make_buttons()
        self.snake = Snake(self)
        self.food = Food(self)
        self.frame_count = 0
        self.right, self.left, self.up, self.down = [1, 0], [-1, 0], [0, -1], [0, 1]

    def make_buttons(self):
        # INTRO BUTTONS
        intro_play_button = Button(self, 50, 50, 100, 50, (20, 121, 21), hover_colour=(49, 218, 46), function=self.intro_to_play, text='PLAY')
        self.intro_buttons.append(intro_play_button)
        intro_quit_button = Button(self, SCREEN_WIDTH-50-100, 50, 100, 50, (128, 26, 23), hover_colour=(199, 30, 30), function=self.intro_quit, text='QUIT')
        self.intro_buttons.append(intro_quit_button)
        # PLAYING BUTTONS
        playing_quit_button = Button(self, (SCREEN_WIDTH//2)-50, 20, 100, 30, (128, 26, 23), hover_colour=(199, 30, 30), function=self.playing_quit, text='QUIT')
        self.playing_buttons.append(playing_quit_button)
        # DEAD BUTTONS
        dead_play_again_button = Button(self, (SCREEN_WIDTH//2)-50, 20, 140, 30, (12, 71, 110), hover_colour=(35, 160, 203), function=self.reset, text='PLAY AGAIN')
        self.dead_buttons.append(dead_play_again_button)

    def reset(self):
        self.state = 'play'
        self.active_buttons = self.playing_buttons
        self.frame_count = 0
        self.snake = Snake(self)

    def run(self):
        while self.running:
            self.get_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
            self.frame_count += 1
        pygame.quit()
        exit()

    def get_events(self):
        if self.state == 'intro':
            self.intro_events()
        if self.state == 'play':
            self.playing_events()
        if self.state == 'dead':
            self.dead_events()

    def update(self):
        if self.state == 'intro':
            self.intro_update()
        if self.state == 'play':
            self.playing_update()
        if self.state == 'dead':
            self.dead_update()

    def draw(self):
        self.screen.fill(BG_COLOR)
        if self.state == 'intro':
            self.intro_draw()
        if self.state == 'play':
            self.playing_draw()
        if self.state == 'dead':
            self.dead_draw()

        pygame.display.update()

# ---------------------------------------------- INTRO EVENTS -------------------------------------------------------- #
    def intro_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.active_buttons:
                    if button.hovered:
                        button.click()

    def intro_update(self):
        for button in self.active_buttons:
            button.update()

    def intro_draw(self):
        for button in self.active_buttons:
            button.draw()

    def intro_to_play(self):
        self.state = 'play'
        self.active_buttons = self.playing_buttons

    def intro_quit(self):
        self.running = False

# ---------------------------------------------- PLAYING EVENTS ------------------------------------------------------ #
    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key == pygame.K_LEFT and self.snake.direction != self.right:
                    self.snake.direction = self.left
                if event.key == pygame.K_RIGHT and self.snake.direction != self.left:
                    self.snake.direction = self.right
                if event.key == pygame.K_UP and self.snake.direction != self.down:
                    self.snake.direction = self.up
                if event.key == pygame.K_DOWN and self.snake.direction != self.up:
                    self.snake.direction = self.down
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.playing_buttons:
                    if button.hovered:
                        button.click()

    def playing_update(self):
        for button in self.active_buttons:
            button.update()
        self.game_window.update()

    def playing_draw(self):
        self.game_window.draw()
        for button in self.active_buttons:
            button.draw()

    def playing_quit(self):
        self.running = False

# ---------------------------------------------- DEAD EVENTS -------------------------------------------------------- #
    def dead_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.active_buttons:
                    if button.hovered:
                        button.click()

    def dead_update(self):
        for button in self.active_buttons:
            button.update()

    def dead_draw(self):
        for button in self.active_buttons:
            button.draw()
