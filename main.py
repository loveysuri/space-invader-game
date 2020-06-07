import pygame
import random
import math
from pygame import mixer
pygame.init()
disp=pygame.display.set_mode([800,600])
bullet = mixer.Sound("bullet.wav")
collision=mixer.Sound("collision.wav")
#for player
img1=pygame.image.load("spaceship(3).png")
px=20
py=480
px_change = 0
py_change = 0
#for enemy
img2=[]
ex=[]
ey=[]
ex_change=[]
ey_change=[]
for i in range(0,5):
    img2.append(pygame.image.load("monster.png"))
    ex.append(random.randint(50,750))
    ey.append(random.randint(30,150))
    ey_change.append(1)#-----------------------------------------------------------------
#for bullet
img3=pygame.image.load("bullet.png")
bx=0
by=480
by_change=0
state=0
#score
score_value=0
score_font=pygame.font.SysFont("comicsansms",35)
#background
backg=pygame.image.load("space.png")
mixer.music.load("background.mp3")
mixer.music.play(-1)
#game over
over_font=pygame.font.SysFont("comicsansms",70)
run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            px_change = -7
            py_change = 0
        elif event.key == pygame.K_RIGHT:
            px_change = 7
            py_change = 0
        elif event.key == pygame.K_SPACE:
            if state==0:
                bullet.play()
                bx=px
                state=1
                by_change=-30
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            px_change=0
            py_change=0
    px = px + px_change#changing co ordinates of player
    by=by+by_change#changing co ordinates of bullet
    if px>736:
        px=736
    if px<0:
        px=0
    disp.fill((0, 0, 0))
    disp.blit(backg, (0, 0))
    if state==1:
        disp.blit(img3,(bx+16,by))
        if by<=0:
            by=480
            state=0
    for i in range(0, 5):#----------------------------------------------------------------
        if ey[i]>=480:
            for j in range(0,5):
                ey[j]=20000
            game_over = over_font.render("GAME OVER", True, (255, 255, 0))
            disp.blit(game_over,(200,200))
            ey[i]=2000
        ey[i] = ey[i] + ey_change[i]
        distance = math.sqrt(((bx - ex[i]) ** 2) + ((by - ey[i]) ** 2))
        if distance < 27:
            collision.play( )
            ex[i]=random.randint(50,750)
            ey[i] = random.randint(20, 150)
            score_value+=1
        score = score_font.render("SCORE:" + str(score_value), True, (255, 255, 0))#-------------------------------------------------
        disp.blit(score, (10, 10))#--------------------------------------------
        disp.blit(img2[i], (ex[i], ey[i]))
    disp.blit(img1, (px,py))
    pygame.display.flip()
pygame.quit()