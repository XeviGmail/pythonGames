# https://www.youtube.com/watch?v=cCiXqK9c18g&list=PL_N_kL9gRTm8lh7GxFHh3ym1RXi6I6c50&index=5
import random
import pygame, sys
import pymunk

def cc(point):
    return int(point[0]), screen_height-int(point[1])

class Ball():
    def __init__(self, x, y, collision_type):
        self.body = pymunk.Body()
        self.body.position = x, y
        self.body.velocity = random.uniform(-200, 200), random.uniform(-200, 200)

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

    def change_to_blue(self, arbiter, space, data):
        self.shape.collision_type = 2

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

    balls = [Ball(random.randint(0, 600), random.randint(0, 600), i + 3) for i in range(100)]
    balls.append(Ball(400, 400, 2))
    handlers = [space.add_collision_handler(2, i+3) for i in range(100)]
    for i, handler in enumerate(handlers):
        handler.separate = balls[i].change_to_blue

    edge_bottom = Edge((0, 10), (585,10))
    edge_top = Edge((10, 585), (585, 585))
    edge_left = Edge((10, 10), (10, 585))
    edge_right = Edge((585, 0), (585, 585))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill('grey')
        [ball.draw() for ball in balls]
        edge_bottom.draw()
        edge_top.draw()
        edge_left.draw()
        edge_right.draw()
        pygame.display.flip()
        clock.tick(FPS)
        space.step(1/FPS)
