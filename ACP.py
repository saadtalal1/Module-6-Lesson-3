import pygame
pygame.init()
window=pygame.display.set_mode((500,500))
red=(225,0,0)
green=(0,225,0)
blue=(0,0,225)
yellow=(225,225,0)
white=(225,225,225)
current_colour=(white)
x, y=30, 30
sprite_width, sprite_height=60, 60
x = min(max(0, x), 500 - 60)
y = min(max(0, y), 500 - 60)
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

    x = min(max(0, x), 500 - 60)
    y = min(max(0, y), 500 - 60)
    
    

    if x == 0: current_color = blue
    elif x == 500 - sprite_width: current_color = yellow
    elif y == 0: current_color = red
    elif y == 500 - sprite_height:
            current_color = green
    else:
            current_color = white

    window.fill((0, 0, 0))
    pygame.draw.rect(window, current_color,
                         (x, y, sprite_width, sprite_height))
    pygame.draw.rect(window, (225,225,0),(400,300,60,60))
    pygame.display.flip()

pygame.quit()



