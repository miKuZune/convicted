import pygame, sys
from pygame import *

pygame.init()

Width = 1200
Height = 900
charXpos = 400
charYPos = 400
charYDirection = 1
floorXPos = 100
floorYPos = 900
jumped = False

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

window = pygame.display.set_mode((Width, Height),0, 32)
font = pygame.font.SysFont(None,48)
text = font.render("    ",True, WHITE,BLUE)
text2 = font.render("                                                                                                                                                                                                                                                                    ",True,WHITE,RED)
floor = text2.get_rect()
character = text.get_rect()

while True:
    character.centerx = charXpos
    character.centery = charYPos
    floor.centerx = floorXPos
    floor.centery = floorYPos

    if charYPos<=865:
        charYPos += 1

    pressed = pygame.key.get_pressed()
    if pressed[K_RIGHT]:
        charXpos +=1
    if charXpos>=1200:
        charXpos -=1
    if charXpos<=0:
        charXpos +=1
    if pressed[K_LEFT]:
        charXpos -=1
    if pressed[K_d]:
        charXpos +=1
    if pressed[K_a]:
        charXpos -= 1
    if pressed[K_SPACE]:
        charYPos -= 10
    if charYPos <= 0:
        charYPos += 10

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()



    pygame.draw.rect(window,WHITE,character)
    pygame.draw.rect(window,WHITE,floor)
    window.fill(WHITE)
    window.blit(text2,floor)
    window.blit(text,character)
    pygame.display.flip()
    pygame.display.update()