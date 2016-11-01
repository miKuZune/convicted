import pygame, sys
from pygame import *

pygame.init()

#Height and width of the screen
Width = 1200
Height = 900

#Direction of the character. For x 1 is right and -1 is left, 0 is no movement.
charXDirection = 0
charYDirection = 1
#Sets the starting position for the character.
charXpos = 50
charYPos = 750
#Sets the starting position for the floor.
floorXPos = 100
floorYPos = 900
#Used to check if the character has jumped and therefore if they are able to jump.
jumped = False

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

window = pygame.display.set_mode((Width, Height),0, 32)
font = pygame.font.SysFont(None,48)
text = font.render("  ",True, WHITE,BLUE)
text2 = font.render("                                                                                                                                                                                                                                                                    ",True,WHITE,RED)
floor = text2.get_rect()
character = text.get_rect()
onFloor = False

while True:
    #Checks if the player is pressing any key. Listener.
    pressed = pygame.key.get_pressed()
    charYDirection += 0.1


    #Checks if the players position is less than the position of the floor. If it is then it brings the player back up one space.
    onFloor = character.colliderect(floor)

    if onFloor == True:
        charYDirection = 0
        jumped = False
    #Checks if the player is pressing the right or d arrow keys. If they are the character moves to the right.
    if pressed[K_RIGHT] or pressed[K_d]:
        if charXDirection <4.5:
            charXDirection += 0.1
    elif pressed[K_LEFT] or pressed[K_a]:
        if charXDirection >-4.5:
            charXDirection -=0.1
    elif pressed[K_DOWN] or pressed[K_s]:
        charXDirection
    else:
        charXDirection = 0

    if pressed[K_SPACE] and jumped == False:
        charYDirection = -4
        jumped = True

    #Position checkers to see if the player is at the boundry of the screen.
    if charYPos <= 0:
        charYPos =0
    if charXpos>=1200:
        charXpos =1200
    if charXpos<=0:
        charXpos =0


    charXpos = charXpos + charXDirection
    charYPos = charYPos + charYDirection
    character.centerx = charXpos
    character.centery = charYPos
    floor.centerx = floorXPos
    floor.centery = floorYPos

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if pressed[K_ESCAPE]:
        pygame.quit()
        sys.exit()



    pygame.draw.rect(window,WHITE,character)
    pygame.draw.rect(window,WHITE,floor)
    window.fill(WHITE)
    window.blit(text2,floor)
    window.blit(text,character)
    clock = pygame.time.Clock()
    clock.tick(500)
    pygame.display.flip()
    pygame.display.update()