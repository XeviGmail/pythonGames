import pygame, sys
import pymunk

def convert_coordinates(point):
    return point[0], screen_height-point[1]

class Ball():
    def __init__(self, pos_x, ball_radius):
        self.ball_radius = ball_radius
        self.body = pymunk.Body()
        self.body.position = pos_x, 600
        self.shape = pymunk.Circle(self.body, ball_radius)
        self.shape.density = 1
        self.shape.elasticity = 1
        space.add(self.body, self.shape)
        image_raw = pygame.image.load('./assets/basketball3.png')
        self.image = pygame.transform.scale(image_raw, (2 * self.ball_radius, 2 * self.ball_radius))
        self.image.set_colorkey((255, 255, 255))

    def draw(self):
        x, y = convert_coordinates(self.body.position)
        display.blit(self.image, (int(x) - self.ball_radius, int(y) - self.ball_radius))

class Floor():
    def __init__(self):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape = pymunk.Segment(self.body, (0, 250), (800, 50), 5)
        self.shape.elasticity = 1
        space.add(self.body, self.shape)

    def draw(self):
        pygame.draw.line(display, (0, 0, 0), (0, 800 - 250), (800, 750), 5)

if __name__ == '__main__':
    pygame.init()
    FPS = 60
    screen_width = 800
    screen_height = 800
    display = pygame.display.set_mode((screen_width,screen_height))
    clock = pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = 0, -1000

    ball = Ball(200, 20)
    ball2 = Ball(400, 40)
    floor = Floor()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        display.fill('grey')

        # pygame.draw.circle(display, 'red', (int(x), int(y)), ball_radius)
        ball.draw()
        ball2.draw()
        floor.draw()
        pygame.display.update()
        clock.tick(FPS)
        space.step(1/FPS)
