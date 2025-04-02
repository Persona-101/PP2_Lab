import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

SPEED = 5
SCORE = 0
COINS = 0
LEVEL = 1   #adding new variable for level

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("racer_files/AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Racer")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("racer_files/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("racer_files/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(5, 0)

#New class for coins
class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("racer_files/Coin.png") 
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
        self.weight = random.randint(1, 2) #adding the random weight to a coin

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

P1 = Player()
E1 = Enemy()
C1 = Coins()

enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()  #adding the new sprite group for coins
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))

    new_level = (COINS // 10) + 1   #If 10 coins collected level increases by 1
    if new_level > LEVEL:  
        LEVEL = new_level
        SPEED += 2    #The speed of enemy increases by 2 with each new level

    new_level_line = font_small.render(f"Level: {new_level}", True, BLACK)
    new_level_rect = new_level_line.get_rect(center = (200, 30))

    score_line = font_small.render(f"Score: {SCORE}", True, BLACK)
    score_rect = score_line.get_rect(center = (50, 30))

    coin_line = font_small.render(f"Coins: {COINS}", True, BLACK)
    coin_rect = coin_line.get_rect(center = (350, 30))

    DISPLAYSURF.blit(score_line, score_rect)
    DISPLAYSURF.blit(coin_line, coin_rect)
    DISPLAYSURF.blit(new_level_line, new_level_rect)

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    coin_collision = pygame.sprite.spritecollideany(P1, coins)
    if coin_collision:   
        COINS += coin_collision.weight   #If player and coin collide increase the coin count by the weight of a coin
        coin_collision.kill()   #remove the coin from screen

    if len(coins) == 0:   #If the coin count on screen is zero
        new_coin = Coins()   #create new coin 
        coins.add(new_coin)  #add to the coins sprite group
        all_sprites.add(new_coin)  #add to the all_sprites sprite group

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('racer_files/crash.wav').play()
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)
