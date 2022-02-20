# https://www.youtube.com/watch?v=cCiXqK9c18g&list=PL_N_kL9gRTm8lh7GxFHh3ym1RXi6I6c50&index=5
import random
import pygame, sys
import pymunk

def collide(arbiter, space, data):
    print('hello')

def cc(point):
    return int(point[0]), screen_height-int(point[1])

class Ball():
    def __init__(self, x, y, collision_type, up):
        self.body = pymunk.Body()
        self.body.position = x, y
        # self.body.velocity = random.uniform(-200, 200), random.uniform(-200, 200)
        self.body.velocity = 6, up*100
        self.shape = pymunk.Circle(self.body, 10)
        self.shape.elasticity = 1
        self.shape.density = 1
        self.shape.collision_type = collision_type
        space.add(self.body, self.shape)
    def draw(self):
        if self.shape.collision_type == 2:
            pygame.draw.circle(screen, 'blue', cc(self.body.position), 10)
        else:
            pygame.draw.circle(screen, 'red', cc(self.body.position), 10)

class Edge():
    def __init__(self, pos_i, pos_f):
        self.pos_i = pos_i
        self.pos_f = pos_f
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape = pymunk.Segment(self.body, self.pos_i, self.pos_f, 1)
        self.shape.elasticity = 1
        space.add(self.body, self.shape)
    def draw(self):
        pygame.draw.line(screen, 'black', cc(self.pos_i), cc(self.pos_f))


if __name__ == '__main__':
    pygame.init()
    FPS = 60
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width,screen_height))
    clock = pygame.time.Clock()
    space = pymunk.Space()
    ball_1 = Ball(200, 200, 1, 1)
    ball_2 = Ball(210, 400, 2, -1)
    edge_bottom = Edge((0, 10), (585,10))
    edge_top = Edge((10, 585), (585, 585))
    edge_left = Edge((10, 10), (10, 585))
    edge_right = Edge((585, 0), (585, 585))

    handler = space.add_collision_handler(1, 2)
    handler.separate = collide
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill('grey')
        ball_1.draw()
        ball_2.draw()
        edge_bottom.draw()
        edge_top.draw()
        edge_left.draw()
        edge_right.draw()
        pygame.display.flip()
        clock.tick(FPS)
        space.step(1/FPS)
