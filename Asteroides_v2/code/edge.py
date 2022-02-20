import pygame
import pymunk

screen_width = 600
screen_height = 600

def cc(point):
    return int(point[0]), screen_height-int(point[1])

class Edge():
    def __init__(self, space, screen, pos_i, pos_f):
        self.space = space
        self.screen = screen
        self.pos_i = pos_i
        self.pos_f = pos_f
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape = pymunk.Segment(self.body, self.pos_i, self.pos_f, 1)
        self.shape.elasticity = 1
        self.space.add(self.body, self.shape)
    def draw(self):
        pygame.draw.line(self.screen, 'black', cc(self.pos_i), cc(self.pos_f))