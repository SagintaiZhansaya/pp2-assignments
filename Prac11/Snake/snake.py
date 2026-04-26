import pygame
from color_palette import *
import random

pygame.init()

WIDTH = 600
HEIGHT = 600
CELL = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 5
clock = pygame.time.Clock()

score = 0
level = 1

def draw_grid():
    # draws grid lines for visual reference
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    def move(self):
        # move snake body forward
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        # move head
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))

        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_wall_collision(self):
        # game over if snake hits border
        head = self.body[0]

        if head.x < 0 or head.x >= WIDTH // CELL:
            return True
        if head.y < 0 or head.y >= HEIGHT // CELL:
            return True

        return False

    def check_self_collision(self):
        # game over if snake hits itself
        head = self.body[0]
        for segment in self.body[1:]:
            if head.x == segment.x and head.y == segment.y:
                return True
        return False

    def check_collision_food(self, food):
        # check if snake eats food
        global score, level, FPS
        head = self.body[0]

        if head.x == food.pos.x and head.y == food.pos.y:
            score += food.value

            # add new segment
            self.body.append(Point(head.x, head.y))

            food.generate_random_pos(self.body)

            # increase level every 10 score
            if score // 10 + 1 > level:
                level += 1
                FPS += 1  # increase speed

class Food:
    def __init__(self):
        self.pos = Point(5, 5)
        self.value = 1
        self.spawn_time = pygame.time.get_ticks()  # time of appearance
        self.lifetime = 5000  # 5 seconds
        self.generate_random_pos([])  # initial spawn

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_random_pos(self, snake_body):
        # randomly choose food value
        self.value = random.choice([1, 2, 3])

        # reset timer when food spawns
        self.spawn_time = pygame.time.get_ticks()

        while True:
            x = random.randint(1, WIDTH // CELL - 2)
            y = random.randint(1, HEIGHT // CELL - 2)

            collision = False
            for segment in snake_body:
                if segment.x == x and segment.y == y:
                    collision = True
                    break

            if not collision:
                self.pos.x = x
                self.pos.y = y
                break

    def check_timer(self, snake_body):
        # if food lives 5 seconds respawn
        current_time = pygame.time.get_ticks()

        if current_time - self.spawn_time > self.lifetime:
            self.generate_random_pos(snake_body)


snake = Snake()
food = Food()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1

    screen.fill(colorBLACK)
    draw_grid()

    snake.move()

    if snake.check_wall_collision() or snake.check_self_collision():
        print("Game Over!")
        running = False

    snake.check_collision_food(food)
    food.check_timer(snake.body)
    snake.draw()
    food.draw()

    print(f"Score: {score} | Level: {level}")

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()