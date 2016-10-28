import pygame, sys
import os
from pygame.locals import *

# set up pygame
pygame.init()
clock = pygame.time.Clock()

# set up colour variables
black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)

# set up the window
window_width = 900
window_height = 800
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Convicted Testing')

# load image and define position
class convictedtesting(object):
    def __init__(self):
        self.image = pygame.image.load('runningman.png')
        self.x = 0
        self.y = 550

    # set up keyboard actions
    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 5
        #if key[pygame.K_DOWN]:
            #self.y += dist
        if key[pygame.K_LEFT]:
            self.x -= dist
        #if key[pygame.K_UP]:
            #self.y -= dist
        if key[pygame.K_RIGHT]:
            self.x += dist

    # draw image to surface
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

# set up playerpos variable
playerpos = convictedtesting()
convictedgame = True

#run game loop
while convictedgame:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        convictedgame = False

    # draw image to window, fill window white
    playerpos.handle_keys()
    playerpos.draw(window)
    pygame.display.update()
    window.fill(white)
    wall = pygame.draw.rect(window, grey, [500, 350, 100, 500])
    # Tring to set up collision with wall
    #if wall.rect.colliderect(self.image):
        #playerpos = playerpos - 1
    clock.tick(30)

pygame.quit()
quit()