FPS = 60
WIDTH = 1024
HEIGHT = 800
SIZE = (WIDTH, HEIGHT)
TITLE = 'Asteroides y mas...'
PADDING = 10
PADDING_LINE = 10
RECT_INFO_DICT = {
    'x': PADDING,
    'y': PADDING,
    'width': int((WIDTH-PADDING) / 3) - 2 * PADDING,
    'height': HEIGHT - 2 * PADDING
}
RECT_INFO = (RECT_INFO_DICT['x'], RECT_INFO_DICT['y'], RECT_INFO_DICT['width'], RECT_INFO_DICT['height'])

RECT_PLAY_DICT = {
    'x': int((WIDTH - PADDING) / 3),
    'y': PADDING,
    'width': 2 * int((WIDTH - PADDING) / 3),
    'height': HEIGHT - (2 * PADDING)
}
RECT_PLAY = (RECT_PLAY_DICT['x'], RECT_PLAY_DICT['y'], RECT_PLAY_DICT['width'], RECT_PLAY_DICT['height'])

BUTTON_TEXT_SIZE = 20
BUTTON_TEXT_COLOUR = 'green'