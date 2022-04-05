# Sprites for the game or the objects:
from settings import*
import pygame.sprite
import random
import pygame.key


class SnakeHead(pygame.sprite.Sprite):
    def __init__(self, Game, head_x, head_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('head_right.png').convert()
        self.image.set_colorkey(WHITE)  # Makes white transparent
        self.rect = self.image.get_rect()
        self.rect.x = WINDOW_X / 2 + TILE_SIZE
        self.rect.y = WINDOW_Y / 2
        self.vx = 0
        self.vy = 0
        self.head_x, self.head_y = head_x, head_y
        self.game = Game

    def move_right(self):
        self.image = pygame.image.load('head_right.png').convert()
        self.image.set_colorkey(WHITE)

    def move_left(self):
        self.image = pygame.image.load('head_left.png').convert()
        self.image.set_colorkey(WHITE)

    def move_up(self):
        self.image = pygame.image.load('head_up.png').convert()
        self.image.set_colorkey(WHITE)

    def move_down(self):
        self.image = pygame.image.load('head_down.png').convert()
        self.image.set_colorkey(WHITE)

    def reset(self):
        self.rect.center = ((WINDOW_X / 2 + TILE_SIZE), (WINDOW_Y / 2))

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.move_left()
            self.vx = - MOVESPEED
            self.vy = 0
        if key[pygame.K_RIGHT]:
            self.move_right()
            self.vx = MOVESPEED
            self.vy = 0
        if key[pygame.K_UP]:
            self.move_up()
            self.vx = 0
            self.vy = - MOVESPEED
        if key[pygame.K_DOWN]:
            self.move_down()
            self.vx = 0
            self.vy = MOVESPEED
        self.game.head_loc.append((self.rect.x, self.rect.y))


class SnakeBody(pygame.sprite.Sprite):
    def __init__(self, game, body_x, body_y):
        self.groups = game.sprites_group
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.body_x, self.body_y = body_x, body_y
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(SNAKE_BODY)
        self.rect = self.image.get_rect()

    def draw(self):
        pass

    def update(self):
        self.rect.x = self.body_x * TILE_SIZE
        self.rect.y = self.body_y * TILE_SIZE


class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 40))
        self.rect = self.image.get_rect()
        self.image.fill(BLUEBERRY)  # Makes the blueberry solid blue
        # Next two codes make the blueberry show up in random places on the screen
        self.rect.x = random.randrange((WINDOW_X - self.rect.width))
        self.rect.y = random.randrange(WINDOW_Y - self.rect.width)

    def respawn(self):  # Fruit respawns after it is eaten to another random location
        self.rect.x = random.randrange((WINDOW_X - self.rect.width))
        self.rect.y = random.randrange(WINDOW_Y - self.rect.width)

    def update(self):
        pass

# Special thanks to Code Basics and The New Boston
# Graphics from Kenny at https://www.kenney.nl/assets/animal-pack-redux
# and instructions from Tech & Gaming
