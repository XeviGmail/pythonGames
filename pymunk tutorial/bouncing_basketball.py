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

    ball_radius = 30
    body = pymunk.Body()
    body.position = 400, 600
    shape = pymunk.Circle(body, ball_radius)
    shape.density = 1
    shape.elasticity = 1
    space.add(body, shape)

    segment_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    segment_shape = pymunk.Segment(segment_body, (0, 250), (800, 50), 5)
    segment_shape.elasticity = 1
    space.add(segment_body, segment_shape)

    image_raw = pygame.image.load('./assets/basketball3.png')
    image =pygame.transform.scale(image_raw, (2*ball_radius,2*ball_radius))
    image.set_colorkey((255,255,255))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        display.fill('grey')
        x, y = convert_coordinates(body.position)
        display.blit(image, (int(x)-ball_radius, int(y)-ball_radius))
        # pygame.draw.circle(display, 'red', (int(x), int(y)), ball_radius)
        pygame.draw.line(display, (0,0,0),(0,800-250), (800, 750), 5)
        pygame.display.update()
        clock.tick(FPS)
        space.step(1/FPS)
