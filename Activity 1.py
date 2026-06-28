import pygame
import random
pygame.init()
window=pygame.display.set_mode((800,600))
colors=[(225,0,0),(0,225,0),(0,0,225),(0,0,0),(225,225,0),(0,225,225)]
width=50
height=50
x=50
y=50
x = min(max(0, x), 800 - 50)
y = min(max(0, y), 600 - 50)
bg_color=(0,0,0)
Sp_color=(225,225,225)
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    pressed=pygame.key.get_pressed()

    if pressed [pygame.K_LEFT]: x=3
    if pressed [pygame.K_RIGHT]: x += 3
    if pressed [pygame.K_UP]: y = 3
    if pressed [pygame.K_DOWN]: y += 3



    x = min(max(0, x), 800 - 50)
    y = min(max(0, y), 600 - 50)
    window.fill((bg_color))
    if y==0:
        bg_color=random.choice(colors)
    elif x==0:
        bg_color=random.choice(colors)
    elif x==750:
        bg_color=random.choice(colors)
    elif y==550:
        bg_color=random.choice(colors)
    
        

    pygame.draw.rect(window,Sp_color,pygame.Rect(x,y,width,height),0)
    pygame.display.flip()