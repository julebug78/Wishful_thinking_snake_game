# This is the main game window for Snake Game by J.E. Griffiths.
import pygame.key
from sprites import*


class Game:
    def __init__(self):  # initialize the game
        pygame.init()  # Command initializes pygame
        pygame.display.set_caption('Snake Game by Mrs Griffiths')
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = True
        self.sprites_group = pygame.sprite.Group()
        self.head = SnakeHead(self, 6, 6)
        self.fruit = Fruit()
        self.body = SnakeBody(self, 8, 8)
        self.score_value = 0
        self.font_name = pygame.font.match_font('arial')
        self.snake_boarder = 3
        self.segments_list = []
        self.body_parts = []
        self.head_loc =[]

    def new(self):
        # How to start a new game / resets game
        self.score_value = 0
        self.head_loc.append(SnakeHead(self, 10, 8))
        self.body_parts.append(SnakeBody(self, 7, 8))
        self.body_parts.append(SnakeBody(self, 6, 8))
        self.sprites_group.add(self.head, self.fruit, self.body)
        self.run()

    def run(self):
        # The Game Loop
        self.head.reset()
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Add updates to game loop as game plays
        self.sprites_group.update()
        self.eat_fruit()

    def events(self):
        # for Events in the Game Loop
        # Check to see if user clicked the close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False

            #  If head reaches edge of screen or 'wall', game ends.
            if self.head.rect.right > WINDOW_X or self.head.rect.left < 0:
                self.head.kill()
                self.show_game_over_screen()

            #  Second part of code. Code was too long for one line.
            if self.head.rect.top < 0 or self.head.rect.bottom > WINDOW_Y:
                self.head.kill()
                self.show_game_over_screen()

    def draw_grid(self):  # Not really using this, but thought it made the background look nice.
        for x in range(0, WINDOW_Y, TILE_SIZE):
            pygame.draw.line(screen, DK_PURPLE, (x, 0), (x, WINDOW_Y))
        for y in range(0, WINDOW_X, TILE_SIZE):
            pygame.draw.line(screen, DK_PURPLE, (0, y), (WINDOW_X, y))

    def draw(self):
        # Draws the game pieces and players on the screen
        screen.fill(PURPLE)  # Fills the screen background with purple
        self.draw_grid()
        self.body.draw()
        self.draw_score()
        self.sprites_group.draw(screen)
        pygame.display.flip()  # Updates the screen and rewrites it with whatever is in here.

    def draw_score(self):
        self.font = pygame.font.SysFont('Arial', 30)
        self.message = self.font.render(str(self.score_value), True, YELLOW)
        screen.blit(self.message, (10, 10))

    def draw_text(self, text, size, color, x, y):
        self.font = pygame.font.SysFont(self.font_name, size)
        self.text_surface = self.font.render(text, True, color)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.midtop = (x, y)
        screen.blit(self.text_surface, self.text_rect)

    def eat_fruit(self):
        # Code to 'eat' fruit and respawn also add a snake segment to the snake.
        if self.head.rect.colliderect(self.fruit):
            self.score_value += 5
            self.fruit.respawn()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            key = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                    self.playing = False
                if key[pygame.K_SPACE]:
                    waiting = False
                elif key[pygame.K_ESCAPE]:  # ESC to quit game
                    waiting = False
                    self.running = False
                    self.playing = False

    def show_start_screen(self):
        screen.fill(AQUA)
        self.draw_text('SNAKE GAME', 100, YELLOW, WINDOW_X / 2, WINDOW_Y * 1/4)
        self.draw_text('Arrows to Move', 50, YELLOW, WINDOW_X / 2, WINDOW_Y / 2)
        self.draw_text('Press Space Bar to Play', 50, YELLOW, WINDOW_X / 2, WINDOW_Y * 3/4)
        pygame.display.flip()
        self.wait_for_key()

    def show_game_over_screen(self):
        # Game over screen at end of game. Includes play again?
        screen.fill(BLACK)
        self.draw_text('GAME OVER', 100, YELLOW, WINDOW_X / 2, WINDOW_Y * 1 / 4)
        self.draw_text('Press "esc" quit.', 50, YELLOW, WINDOW_X / 2, WINDOW_Y * 3 / 4)
        pygame.display.flip()
        self.wait_for_key()


# The order for game instructions to make the game run
g = Game()
g.show_start_screen()
while g.running:
    g.new()

pygame.quit()

# Special Thanks to Woowoodabestgnh and Chris Bradfield from  KidsCanCode
