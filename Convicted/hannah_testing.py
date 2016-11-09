import pygame, sys
import os
from pygame.locals import *

# set up pygame
pygame.init()
clock = pygame.time.Clock()

# set up colour variables
black = (0, 0, 0)
white = (255, 255, 255)

# set up window
window_width = 900
window_height = 800
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Convicted')

# set up player
class player(object):
    def __init__(self):
        self.image = pygame.image.load('runningman.png')
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.x = 0
        self.y = 650
    # set up keyboard actions
    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 5
        # if key[pygame.K_DOWN]:
            # self.y += dist
        if key[pygame.K_LEFT]:
            self.x -= dist
        #if key[pygame.K_UP]:
            #self.y -= dist
        if key[pygame.K_RIGHT]:
            self.x += dist
        # keep player on screen
        if self.x < 0:
            self.x = 0
        if self.x > 670:
            self.x = 670
        if self.y < 0:
            self.y = 0
        if self.y > 670:
            self.y = 670
    # draw player to surface
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

# set up wall
class brickwall(object):
    def __init__(self):
        self.image = pygame.image.load('concretewall.png')
        self.x = 450
        self.y = 395
    # draw wall to surface
    def draw(self, surface):
            surface.blit(self.image, (self.x, self.y))

# set up bin
class bin(object):
    def __init__(self):
        self.image = pygame.image.load('bin_192px.png')
        self.x = 250
        self.y = 640
    # draw bin to surface
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

# set up playerpos and wallpos variables
playerpos = player()
wallpos = brickwall()
binpos = bin()

#run game loop
running = True
while running:
    pressed = pygame.key.get_pressed()
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False

    playerpos.handle_keys()
    playerpos.draw(window)
    pygame.display.update()
    window.fill(white)
    wallpos.draw(window)
    binpos.draw(window)
    clock.tick(40)

pygame.quit()
quit()