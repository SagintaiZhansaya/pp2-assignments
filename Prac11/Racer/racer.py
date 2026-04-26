import pygame
import random
import time

pygame.init()

WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 

image_background = pygame.image.load('resources/AnimatedStreet.png')
image_player = pygame.image.load('resources/Player.png')
image_enemy = pygame.image.load('resources/Enemy.png')
image_coin_1 = pygame.image.load('resources/coin_1.png')
image_coin_5 = pygame.image.load('resources/coin_5.png')
image_coin_10 = pygame.image.load('resources/coin_10.png')

# loading and playing background music endlessly
pygame.mixer.music.load('resources/background.wav')
pygame.mixer.music.play(-1)

sound_crash = pygame.mixer.Sound('resources/crash.wav')

font = pygame.font.SysFont("Verdana", 60)
image_game_over = font.render("Game Over", True, "black")
image_game_over_rect = image_game_over.get_rect(center = (WIDTH // 2, HEIGHT // 2))

coins = 0
coin_font = pygame.font.SysFont("Verdana", 30)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_player
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT
        self.speed = 5

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        # screen restriction 
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_enemy
        self.rect = self.image.get_rect()
        self.speed = 5
        self.generate_random_rect()

    def generate_random_rect(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.bottom = 0

    def move(self):
        self.rect.move_ip(0, self.speed)
        # if it goes off the screen it appears again from the top
        if self.rect.top > HEIGHT:
            self.generate_random_rect()

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_coin_1
        self.rect = self.image.get_rect()
        self.value = 1
        self.speed = 5
        self.respawn()

    def respawn(self):
        # random choice of coin type 
        self.value = random.choice([1, 5, 10])

        # assign the picture and speed
        if self.value == 1:
            self.image = image_coin_1
            self.speed = 6
        elif self.value == 5:
            self.image = image_coin_5
            self.speed = 5
        else:
            self.image = image_coin_10
            self.speed = 4

        self.rect = self.image.get_rect()

        # position
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.top = random.randint(-600, -50)

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.respawn()

running = True

clock = pygame.time.Clock()
FPS = 60

player = Player()
enemy = Enemy()
coin = Coin()

all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()

all_sprites.add(player, enemy, coin)
enemy_sprites.add(enemy)
coin_sprites.add(coin)

level = 1
next_level = 50

while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

    player.move()

    screen.blit(image_background, (0, 0))

    # movement and rendering of all objects
    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(player, coin_sprites):
        coins += coin.value
        coin.respawn() 
        # increase in complexity
        if coins >= next_level:
            level += 1
            coins -= 50
            enemy.speed += 1

    if pygame.sprite.spritecollideany(player, enemy_sprites):
        sound_crash.play()
        time.sleep(1)

        running = False
        screen.fill("red")
        screen.blit(image_game_over, image_game_over_rect)
        pygame.display.flip()

        time.sleep(3)
        
    coin_text = coin_font.render(f"Coins: {coins}", True, "black")
    screen.blit(coin_text, (WIDTH - 150, 45))
    level_text = coin_font.render(f"Level: {level}", True, "black")
    screen.blit(level_text, (WIDTH - 150, 10))

    pygame.display.flip() 
    clock.tick(FPS) 

pygame.quit()