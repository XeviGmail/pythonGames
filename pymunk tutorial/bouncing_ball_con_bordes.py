import pygame, sys
import pymunk

def convert_coordinates(point):
    return point[0], screen_height-point[1]

if __name__ == '__main__':
    pygame.init()
    FPS = 60
    screen_width = 800
    screen_height = 800
    display = pygame.display.set_mode((screen_width,screen_height))
    clock = pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = 0, -1000

    body = pymunk.Body()
    body.position = 400, 600
    shape = pymunk.Circle(body, 10)
    shape.density = 1
    shape.elasticity = 1
    space.add(body, shape)

    segment_right = pymunk.Body(body_type=pymunk.Body.STATIC)
    segment_right_shape = pymunk.Segment(segment_right, (795,0), (795,795), 5)
    segment_right_shape.elasticity = 1
    space.add(segment_right, segment_right_shape)

    segment_bottom = pymunk.Body(body_type=pymunk.Body.STATIC)
    segment_bottom_shape = pymunk.Segment(segment_bottom, (0, 250), (800, 240), 5)
    segment_bottom_shape.elasticity = 1
    space.add(segment_bottom, segment_bottom_shape)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        display.fill('grey')
        x, y = convert_coordinates(body.position)
        pygame.draw.circle(display, 'red', (int(x), int(y)), 10)
        pygame.draw.line(display, (0, 0, 0), (0,800-250), (800, 800-240), 5)
        pygame.draw.line(display, (0, 0, 0), (795, 795), (795, 0), 5)
        pygame.display.flip()
        clock.tick(FPS)
        space.step(1/FPS)
