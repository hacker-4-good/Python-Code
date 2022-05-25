import pygame
import random

#intialise the pygame
pygame.init()

#create the screen 
screen = pygame.display.set_mode((800,600))

#title and icons
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0

#enemy
enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 0

def player(x,y):
    screen.blit(playerImg, (x,y))

def enemy(x,y):
    screen.blit(enemyImg, (x,y))

#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #if keystroke is pressed check whether it is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    # RGB = red, blue, green
    playerX += playerX_change
    if playerX<=0:
        playerX = 0
    elif playerX>=736:
        playerX = 736
    screen.fill((0,0,0))
    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()