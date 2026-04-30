import pygame
import random
import json
import psycopg2
from datetime import datetime
from color_palette import *

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="1234"
)

pygame.init()
WIDTH, HEIGHT = 600, 600
CELL = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont("Verdana", 24)
clock = pygame.time.Clock()


def init_db():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS players (id SERIAL PRIMARY KEY, username VARCHAR(50) UNIQUE NOT NULL);")
        cur.execute("""CREATE TABLE IF NOT EXISTS game_sessions (
            id SERIAL PRIMARY KEY, player_id INTEGER REFERENCES players(id),
            score INTEGER, level_reached INTEGER, played_at TIMESTAMP DEFAULT NOW());""")
        conn.commit()
        cur.close()
        conn.close()
    except:
        print("DB Connection failed")

def save_result(user, score, lvl):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        cur.execute("INSERT INTO players (username) VALUES (%s) ON CONFLICT (username) DO NOTHING", (user,))
        cur.execute("SELECT id FROM players WHERE username = %s", (user,))
        p_id = cur.fetchone()[0]
        cur.execute("INSERT INTO game_sessions (player_id, score, level_reached) VALUES (%s, %s, %s)", (p_id, score, lvl))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Save error: {e}")

def load_settings():
    try:
        with open("settings.json", "r") as f: return json.load(f)
    except:
        return {"snake_color": colorYELLOW, "grid": True}

settings = load_settings()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0
        self.shield = False

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        for i, seg in enumerate(self.body):
            color = colorRED if i == 0 else settings["snake_color"]
            if self.shield:
                color = colorBLUE
            pygame.draw.rect(screen, color, (seg.x * CELL, seg.y * CELL, CELL, CELL))

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Point(5, 5)
        self.poison = Point(15, 15)
        self.obstacles = []
        self.powerup = None
        self.powerup_type = None
        self.powerup_time = 0
        self.score = 0
        self.level = 1
        self.fps = 5
        self.username = "Player1"
        self.state = "MENU" 
        self.spawn_food()

    def spawn_food(self):
        while True:
            p = Point(random.randint(0, 19), random.randint(0, 19))
            if not any(o.x == p.x and o.y == p.y for o in self.obstacles):
                self.food = p
                break

    def spawn_powerup(self):
        self.powerup = Point(random.randint(0, 19), random.randint(0, 19))
        self.powerup_type = random.choice(["speed", "shield"])
        self.powerup_time = pygame.time.get_ticks()

    def handle_collisions(self):
        head = self.snake.body[0]
        
        hit_obs = any(o.x == head.x and o.y == head.y for o in self.obstacles)
        if head.x < 0 or head.x >= 20 or head.y < 0 or head.y >= 20 or hit_obs:
            if self.snake.shield:
                self.snake.shield = False
            else:
                self.game_over()

        if head.x == self.food.x and head.y == self.food.y:
            self.score += 1
            self.snake.body.append(Point(-1, -1))
            self.spawn_food()
            if self.score % 5 == 0:
                self.level += 1
                self.fps += 1
                if self.level >= 3:
                    self.obstacles.append(Point(random.randint(0, 19), random.randint(0, 19)))
            if random.random() < 0.2:
                self.spawn_powerup()

        if head.x == self.poison.x and head.y == self.poison.y:
            if len(self.snake.body) > 2:
                self.snake.body.pop()
                self.snake.body.pop()
                self.poison = Point(random.randint(0, 19), random.randint(0, 19))
            else:
                self.game_over()

        if self.powerup and head.x == self.powerup.x and head.y == self.powerup.y:
            if self.powerup_type == "shield":
                self.snake.shield = True
            if self.powerup_type == "speed":
                self.fps += 3
            self.powerup = None

    def game_over(self):
        save_result(self.username, self.score, self.level)
        self.state = "GAMEOVER"

    def draw(self):
        screen.fill(colorBLACK)
        if settings["grid"]:
            for i in range(0, WIDTH, CELL):
                for j in range(0, HEIGHT, CELL):
                    pygame.draw.rect(screen, colorGRAY, (i, j, CELL, CELL), 1)
        
        pygame.draw.rect(screen, colorGREEN, (self.food.x * CELL, self.food.y * CELL, CELL, CELL))
        pygame.draw.rect(screen, colorDARK_RED, (self.poison.x * CELL, self.poison.y * CELL, CELL, CELL))
        for o in self.obstacles:
            pygame.draw.rect(screen, colorORANGE, (o.x * CELL, o.y * CELL, CELL, CELL))
        if self.powerup:
            pygame.draw.rect(screen, colorPURPLE, (self.powerup.x * CELL, self.powerup.y * CELL, CELL, CELL))
        
        self.snake.draw()
        txt = font.render(f"Score: {self.score} Lvl: {self.level}", True, colorWHITE)
        screen.blit(txt, (10, 10))

init_db()
game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if game.state == "MENU" and event.key == pygame.K_RETURN:
                game.state = "PLAYING"
            if game.state == "PLAYING":
                if event.key == pygame.K_UP and game.snake.dy == 0:
                    game.snake.dx = 0
                    game.snake.dy = -1
                if event.key == pygame.K_DOWN and game.snake.dy == 0:
                    game.snake.dx = 0
                    game.snake.dy = 1
                if event.key == pygame.K_LEFT and game.snake.dx == 0:
                    game.snake.dx = -1
                    game.snake.dy = 0
                if event.key == pygame.K_RIGHT and game.snake.dx == 0:
                    game.snake.dx = 1
                    game.snake.dy = 0

    if game.state == "PLAYING":
        game.snake.move()
        game.handle_collisions()
    
        if game.powerup and pygame.time.get_ticks() - game.powerup_time > 8000:
            game.powerup = None

        game.draw()
        
    elif game.state == "MENU":
        screen.fill(colorBLACK)
        screen.blit(font.render("SNAKE GAME - PRESS ENTER", True, colorWHITE), (150, 250))
    elif game.state == "GAMEOVER":
        screen.fill(colorRED)
        screen.blit(font.render(f"GAME OVER! Score: {game.score}", True, colorWHITE), (180, 250))

    pygame.display.flip()
    clock.tick(game.fps)