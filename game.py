import pygame
import random
import math 

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0

background = pygame.image.load("background.png")

enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(0,735)
enemyY = random.randint(50,150)
enemyX_change = 2
enemyY_change = 40

bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"

score = 0

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    screen.blit(enemyImg,(x,y))

def bullet_fire(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x+16,y+10))

def isCollison(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2)+math.pow(enemyY-bulletY,2))
    if distance<27:
        return True
    else:
        return False

running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -2
        if event.key == pygame.K_RIGHT:
            playerX_change = 2
        if event.key == pygame.K_TAB:
            if bullet_state is "ready":
                bulletX = playerX
                bullet_fire(bulletX,bulletY)

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

    playerX += playerX_change

    if playerX<=0:
        playerX = 0
    elif playerX>=736:
        playerX = 736

    enemyX += enemyX_change

    if enemyX<=0:
        enemyX_change = 2
        enemyY += enemyY_change
    elif enemyX>=736:
        enemyX_change = -2
        enemyY += enemyY_change

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        bullet_fire(bulletX,bulletY)
        bulletY -= bulletY_change
    
    collision = isCollison(enemyX,enemyY,bulletX,bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(0,735)
        enemyY = random.randint(50,150)

    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()