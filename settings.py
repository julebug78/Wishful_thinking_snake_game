import pygame


# window x and y need to fit the 16 pixel squares evenly
WINDOW_X = 680
WINDOW_Y = 680
FPS = 30
TILE_SIZE = 40
BOARDER = 3
RIGHT = 'right'
LEFT = 'left'
DOWN = 'down'
UP = 'up'
MOVESPEED = 4
ROWS = 17
COLUMNS = 17

up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

# Define colors
AQUA = pygame.Color(66, 224, 245)
SNAKE_GREEN = pygame.Color(66, 245, 147)
PURPLE = pygame.Color(216, 172, 230)
DK_PURPLE = pygame.Color(111, 32, 176)
BLUEBERRY = pygame.Color(38, 60, 224)
WHITE = pygame.Color(255, 255, 255)
YELLOW = pygame.Color(234, 240, 134)
SNAKE_BODY = pygame.Color(105, 157, 240)
BLACK = pygame.Color(0, 0, 0)
APPLE_RED = pygame.Color(207, 8, 8)
BANANA = pygame.Color(219, 187, 70)
LIME = pygame.Color(41, 255, 76)

pygame.font.init()
FONT = pygame.font.SysFont('arial', 20)

screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y))  # Command sets the game window


COLOR = ['APPLE_RED', 'BANANA', 'BLUEBERRY', 'LIME']
