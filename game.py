import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
SQUARE_SIZE = 20

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

class Snake:
    def __init__(self):
        self.position = [[WIDTH // 2, HEIGHT // 2]]
        self.direction = [SQUARE_SIZE, 0]
        self.length = 1

    def move(self):
        new_head = [self.position[0][0] + self.direction[0],
                    self.position[0][1] + self.direction[1]]

        if new_head[0] >= WIDTH:
            new_head[0] = 0
        elif new_head[0] < 0:
            new_head[0] = WIDTH - SQUARE_SIZE
        if new_head[1] >= HEIGHT:
            new_head[1] = 0
        elif new_head[1] < 0:
            new_head[1] = HEIGHT - SQUARE_SIZE

        self.position.insert(0, new_head)
        if len(self.position) > self.length:
            self.position.pop()

    def eat_food(self):
        self.length += 1

    def has_collided(self):
        return self.position[0] in self.position[1:]

def start_game():
    snake = Snake()
    food = [random.randrange(0, WIDTH, SQUARE_SIZE),
            random.randrange(0, HEIGHT, SQUARE_SIZE)]
    clock = pygame.time.Clock()
    game_running = True

    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and snake.direction != [0, SQUARE_SIZE]:
                    snake.direction = [0, -SQUARE_SIZE]
                elif event.key == pygame.K_s and snake.direction != [0, -SQUARE_SIZE]:
                    snake.direction = [0, SQUARE_SIZE]
                elif event.key == pygame.K_a and snake.direction != [SQUARE_SIZE, 0]:
                    snake.direction = [-SQUARE_SIZE, 0]
                elif event.key == pygame.K_d and snake.direction != [-SQUARE_SIZE, 0]:
                    snake.direction = [SQUARE_SIZE, 0]

        snake.move()

        if snake.position[0] == food:
            snake.eat_food()
            food = [random.randrange(0, WIDTH, SQUARE_SIZE),
                    random.randrange(0, HEIGHT, SQUARE_SIZE)]

        if snake.has_collided():
            game_running = False

        screen.fill(BLACK)

        pygame.draw.rect(screen, RED,
                         [food[0], food[1], SQUARE_SIZE, SQUARE_SIZE])

        for part in snake.position:
            pygame.draw.rect(screen, GREEN,
                             [part[0], part[1], SQUARE_SIZE, SQUARE_SIZE])

        pygame.display.update()
        clock.tick(10)

    pygame.quit()

start_game()