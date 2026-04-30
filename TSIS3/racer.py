import pygame
import random
import time
import json 
import os 

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
image_oil = pygame.image.load('resources/oil_spill.png')
image_nitro = pygame.image.load('resources/nitro.png')
image_shield = pygame.image.load('resources/shield.png')
image_repair = pygame.image.load('resources/repair.png')

pygame.mixer.music.load('resources/background.wav')
pygame.mixer.music.play(-1)
sound_crash = pygame.mixer.Sound('resources/crash.wav')

font = pygame.font.SysFont("Verdana", 50)
ui_font = pygame.font.SysFont("Verdana", 20)
coin_font = pygame.font.SysFont("Verdana", 30)

def save_score(score):
    leaderboard = []
    if os.path.exists('leaderboard.json'):
        with open('leaderboard.json', 'r') as f:
            leaderboard = json.load(f)
    
    leaderboard.append({"score": score, "date": time.strftime("%d/%m %H:%M")})
    leaderboard = sorted(leaderboard, key=lambda x: x['score'], reverse=True)[:10]
    
    with open('leaderboard.json', 'w') as f:
        json.dump(leaderboard, f)

def get_leaderboard():
    if os.path.exists('leaderboard.json'):
        with open('leaderboard.json', 'r') as f:
            return json.load(f)
    return []

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_player
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT
        self.speed = 5
        self.sliding = False
        self.slide_time = 0
        self.powerup = None
        self.powerup_time = 0
        self.shield = False

    def move(self):
        keys = pygame.key.get_pressed()
        current_speed = self.speed

        if self.powerup == "Nitro":
            current_speed += 5
            if pygame.time.get_ticks() > self.powerup_time:
                self.powerup = None

        if self.sliding:
            current_speed = 1
            if pygame.time.get_ticks() > self.slide_time:
                self.sliding = False

        if keys[pygame.K_RIGHT]: 
            self.rect.move_ip(current_speed, 0)
        if keys[pygame.K_LEFT]: 
            self.rect.move_ip(-current_speed, 0)
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
        self.spawn()

    def spawn(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.bottom = 0

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT: 
            self.spawn()

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.respawn()

    def respawn(self): 
        self.value = random.choice([1, 5, 10])
        self.image = {1: image_coin_1, 5: image_coin_5, 10: image_coin_10}[self.value]
        self.speed = {1: 6, 5: 5, 10: 4}[self.value]
        self.rect = self.image.get_rect()
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.top = random.randint(-600, -50)

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT: 
            self.respawn()

class Oil_spill(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_oil
        self.rect = self.image.get_rect()
        self.speed = 5
        self.spawn()

    def spawn(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.top = random.randint(-600, -50)

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT: 
            self.spawn()
 
class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.type = random.choice(["Nitro", "Shield", "Repair"])
        self.image = {"Nitro": image_nitro, "Shield": image_shield, "Repair": image_repair}[self.type]
        self.rect = self.image.get_rect()
        self.speed = 5
        self.spawn_time = pygame.time.get_ticks()
        self.spawn()

    def spawn(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.top = random.randint(-600, -50)
        self.spawn_time = pygame.time.get_ticks()

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT or (pygame.time.get_ticks() - self.spawn_time > 5000):
            self.kill()

def main_menu():
    while True:
        screen.fill("white")
        title = font.render("STREET RACER", True, "black")
        screen.blit(title, (10, 100))
        
        play_txt = ui_font.render("Press 1 to PLAY", True, "black")
        lead_txt = ui_font.render("Press 2 for LEADERBOARD", True, "black")
        quit_txt = ui_font.render("Press ESC to QUIT", True, "black")
        
        screen.blit(play_txt, (WIDTH//2 - 80, 300))
        screen.blit(lead_txt, (WIDTH//2 - 120, 350))
        screen.blit(quit_txt, (WIDTH//2 - 80, 400))
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                return "QUIT"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1: 
                    return "GAME"
                if event.key == pygame.K_2: 
                    return "SCORES"
                if event.key == pygame.K_ESCAPE: 
                    return "QUIT"

def leaderboard_screen():
    while True:
        screen.fill("white")
        title = coin_font.render("TOP 10 SCORES", True, "black")
        screen.blit(title, (WIDTH//2 - 100, 50))
        
        scores = get_leaderboard()
        for i, entry in enumerate(scores):
            txt = ui_font.render(f"{i+1}. {entry['score']} pts ({entry['date']})", True, "black")
            screen.blit(txt, (50, 120 + i*30))
            
        back_txt = ui_font.render("Press ESC to BACK", True, "gray")
        screen.blit(back_txt, (WIDTH//2 - 80, 500))
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                return "QUIT"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: 
                    return "MENU"

def game_loop():
    player = Player()
    enemy = Enemy()
    coin = Coin()
    oil = Oil_spill()
    all_sprites = pygame.sprite.Group(player, enemy, coin, oil)
    enemy_sprites = pygame.sprite.Group(enemy)
    coin_sprites = pygame.sprite.Group(coin)
    hazard_sprites = pygame.sprite.Group(oil)
    powerup_sprites = pygame.sprite.Group()

    POWERUP_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(POWERUP_EVENT, 10000)

    coins = 0
    distance = 0
    level = 1
    next_level = 50
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()

    while True:
        current_time = pygame.time.get_ticks()
        distance = (current_time - start_time) // 100 
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                return "QUIT"
            if event.type == POWERUP_EVENT:
                new_p = PowerUp()
                powerup_sprites.add(new_p)
                all_sprites.add(new_p)

        player.move()
        screen.blit(image_background, (0, 0))

        for entity in all_sprites:
            entity.move()
            screen.blit(entity.image, entity.rect)
    
        p_hit = pygame.sprite.spritecollideany(player, powerup_sprites)
        if p_hit:
            if p_hit.type == "Nitro":
                player.powerup = "Nitro"
                player.powerup_time = pygame.time.get_ticks() + 10000 
            elif p_hit.type == "Shield":
                player.shield = True
                player.powerup = "Shield"
            elif p_hit.type == "Repair":
                enemy.spawn()
                oil.spawn()
            p_hit.kill()

        if pygame.sprite.spritecollideany(player, hazard_sprites):
            player.sliding = True
            player.slide_time = pygame.time.get_ticks() + 1000
            
        if pygame.sprite.spritecollideany(player, coin_sprites):
            coins += coin.value
            coin.respawn() 
            if coins >= next_level:
                level += 1
                coins -= 50
                enemy.speed += 1
                oil.speed += 0.5

        if pygame.sprite.spritecollideany(player, enemy_sprites):
            if player.shield:
                player.shield = False
                player.powerup = None
                enemy.spawn()
            else:
                sound_crash.play()
                final_score = (coins * 100) + distance
                save_score(final_score)
                return "GAMEOVER", final_score

        screen.blit(coin_font.render(f"Coins: {coins}", True, "black"), (WIDTH - 150, 45))
        screen.blit(coin_font.render(f"Dist: {distance}m", True, "black"), (WIDTH - 150, 10))
        
        if player.powerup:
            if player.powerup == "Nitro":
                rem = max(0, ((player.powerup_time - pygame.time.get_ticks()) // 1000))
                txt = f"Active: {player.powerup} : {rem}s"
                screen.blit(ui_font.render(txt, True, "blue"), (10, 10))
            else:
                txt = f"Active: {player.powerup}"
                screen.blit(ui_font.render(txt, True, "blue"), (10, 10))
            
        pygame.display.flip() 
        clock.tick(60)

def game_over_screen(score):
    while True:
        screen.fill("red")
        txt = font.render("GAME OVER", True, "white")
        score_txt = coin_font.render(f"Final Score: {score}", True, "white")
        back_txt = ui_font.render("Press SPACE to Menu", True, "white")
        
        screen.blit(txt, (WIDTH//2 - 150, 200))
        screen.blit(score_txt, (WIDTH//2 - 100, 300))
        screen.blit(back_txt, (WIDTH//2 - 100, 400))
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                return "QUIT"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return "MENU"

state = "MENU"
current_final_score = 0

while state != "QUIT":
    if state == "MENU":
        state = main_menu()
    elif state == "SCORES":
        state = leaderboard_screen()
    elif state == "GAME":
        result = game_loop()
        if result == "QUIT": 
            state = "QUIT"
        else:
            state, current_final_score = result
    elif state == "GAMEOVER":
        state = game_over_screen(current_final_score)

pygame.quit()