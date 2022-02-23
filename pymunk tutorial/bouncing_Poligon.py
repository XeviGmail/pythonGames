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

    # Circle
    body = pymunk.Body()
    body.position = 400, 600
    shape = pymunk.Circle(body, 10)
    shape.density = 1
    shape.elasticity = 1
    space.add(body, shape)

    # Polygon
    size_x = 50
    size_y = 50
    poly_body = pymunk.Body()
    poly_body.position = 200, 600
    poly_shape = pymunk.Poly.create_box(poly_body,size=(size_x, size_y))
    poly_shape.density = 1
    poly_shape.elasticity = 1
    space.add(poly_body, poly_shape)
    print(poly_shape.get_vertices())

    # segment
    segment_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    segment_shape = pymunk.Segment(segment_body, (0, 250), (800, 250), 5)
    segment_shape.elasticity = 1
    space.add(segment_body, segment_shape)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        display.fill('grey')
        x, y = convert_coordinates(body.position)
        pygame.draw.circle(display, 'red', (int(x), int(y)), 10)
        x, y = convert_coordinates(poly_body.position)

        pygame.draw.rect(display, 'blue', pygame.Rect(poly_body.position.x-size_x/2, 800 - poly_body.position.y-size_y/2, 50, 50))
        pygame.draw.line(display, (0,0,0),(0,800-250), (800, 800-250), 5)
        pygame.display.flip()
        clock.tick(FPS)
        space.step(1/FPS)
