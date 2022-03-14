FPS = 60
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
TITLE = 'Asteroides y mas...'
PADDING = 10

PLAY_RECT_DICT = {
    'x': int((SCREEN_WIDTH-PADDING) / 3),
    'y': PADDING,
    'width': 2 * int((SCREEN_WIDTH-PADDING) / 3),
    'height': SCREEN_HEIGHT - (2 * PADDING)
}
PLAY_RECT = (PLAY_RECT_DICT['x'], PLAY_RECT_DICT['y'], PLAY_RECT_DICT['width'], PLAY_RECT_DICT['height'])

INFO_RECT_DICT = {
    'x': PADDING,
    'y': PADDING,
    'width': int((SCREEN_WIDTH - PADDING) / 3) - 2 * PADDING,
    'height': SCREEN_HEIGHT - 2 * PADDING
}
INFO_RECT = (INFO_RECT_DICT['x'], INFO_RECT_DICT['y'], INFO_RECT_DICT['width'], INFO_RECT_DICT['height'])

INTRO_RECT_DICT = {
    'x': PADDING,
    'y': PADDING,
    'width': SCREEN_WIDTH - 2 * PADDING,
    'height': SCREEN_HEIGHT - 2 * PADDING
}
INTRO_RECT = (INTRO_RECT_DICT['x'], INTRO_RECT_DICT['y'], INTRO_RECT_DICT['width'], INTRO_RECT_DICT['height'])