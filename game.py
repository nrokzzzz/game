import pygame
import random
import  math
pygame.init()
#living

live = 3

# Load assets (ensure file paths are correct)
background = pygame.image.load('freepik-undefined-20241122033528EETP.png')
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Monster")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)
playerImg = pygame.image.load('arcade-game.png')
enemyImg = pygame.image.load('ghost.png')
bulletImg = pygame.image.load('bullet.png')
# Initial positions
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0
#score
score_value = 0

enemyX = random.randint(0, 736)
enemyY = -64
enemyY_change = 0.8 # Enemy's downward speed

bulletX = playerX+30
bulletY = playerY
bulletY_change=-2
bullet_state = "ready"
#font give


make = False


font = pygame.font.Font(None,50)
exit_font = pygame.font.Font(None,100)
#exit
def exit():
    game_exit = exit_font.render("GAME OVER",True,(73,245,91))
    screen.blit(game_exit,(200,250))
# Draw player and enemy
def show_live(live):
    living = font.render("Life :"+str(live),True,(255,0,0))
    screen.blit(living,(700,10))
def show_score():
    score = font.render("Score :"+ str(score_value),True,(255,255,255))
    screen.blit(score,(10,10))
def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))
def bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x+16,y-30))
def collision(enemyX,enemyY,bulletX,bulletY):
    check = math.sqrt((math.pow((enemyX-bulletX),2))+(math.pow((enemyY-bulletY),2)))
    if check < 27 :
        return True
    else:
        return False
# Game loop
running = True
one = True
while running:
    # Draw the background
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 1.3
            if event.key == pygame.K_UP:
                playerY_change = -1.3
            if event.key == pygame.K_DOWN:
                playerY_change = 1.3
            if event.key  == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX=playerX

                bullet(bulletX,bulletY)
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN,pygame.K_SPACE):
                playerX_change = 0
                playerY_change = 0

    # Update player position
    playerX += playerX_change
    playerY += playerY_change

    # Boundaries for the player
    playerX = max(0, min(playerX, 736))
    playerY = max(0, min(playerY, 536))
    #complete exit
    if make :
        exit()
        continue

    # Update enemy position
    enemyY += enemyY_change
    if enemyY > 600:  # Reset enemy if it goes off the screen
        enemyY = -64
        enemyX = random.randint(0, 736)

    # Draw player and enemy
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    if bulletY<=0:
        bulletY = playerY
        bulletX = playerX
        bullet_state = "ready"
    if bullet_state is "fire":
        bullet(bulletX,bulletY)
        bulletY+=bulletY_change
    if collision(enemyX,enemyY,bulletX,bulletY):
        enemyX = random.randint(0, 736)
        enemyY = -64
        bulletY = playerY
        bulletX = playerX
        bullet_state = "ready"
        score_value =score_value+ 1
        print(score_value)
    # Update the display
    if live == 0:
         exit()
         make=True
    if enemyY >=580:
        live -=1
        #print(live)
    show_score()
 #   show_live(live)
    pygame.display.update()
