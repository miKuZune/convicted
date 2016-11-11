import pygame, sys
import os
from pygame.locals import *

# Set up pygame
pygame.init()
clock = pygame.time.Clock()

# Set up colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (169, 169, 169)

# Set up window
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 900
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Convicted')

# Set up Road
road = (0, 880, WINDOW_WIDTH, 40)

"""Set up player"""
class player(object):
    def __init__(self):
        self.sprite = pygame.image.load('runningman.png').convert()
        self.sprite = pygame.transform.scale(self.sprite, (150, 150))
        self.rect = self.sprite.get_rect()
        self.x = 0
        self.y = 740
    # set up keyboard actions
    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 5
        standing = True
        jumping = False
        if key[pygame.K_LEFT]:
            self.x -= dist
        if key[pygame.K_RIGHT]:
            self.x += dist
        if key[pygame.K_SPACE] and jumping == False:
            self.y += - 20
        # keep player on screen
        if self.x < 0:
            self.x = 0
        if self.x > 1050:
            self.x = 1050
        if self.y < 0:
            self.y = 0
        if self.y > 1050:
            self.y = 1050
    # draw player to surface
    def draw(self, surface):
        surface.blit(self.sprite, (self.x, self.y))

"""Set up wall"""
class brickwall(object):
    def __init__(self):
        self.sprite = pygame.image.load('concretewall_smaller.png').convert()
        self.sprite = pygame.transform.scale(self.sprite, (138, 273))
        self.rect = self.sprite.get_rect()
        self.x = 860
        self.y = 610
    # draw wall to surface
    def draw(self, surface):
            surface.blit(self.sprite, (self.x, self.y))

"""Set up bin"""
class bin(object):
    def __init__(self):
        self.image = pygame.image.load('bin_192px.png')
        self.x = 250
        self.y = 720
    # draw bin to surface
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

"""Set up bikerack"""
class bikerack(object):
    def __init__(self):
        self.image = pygame.image.load('BikeRack.png')
        self.image = pygame.transform.scale(self.image, (400, 400))
        self.x = 450
        self.y = 610
    # draw bikerack to surface
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

BrickWallRect = (138, 273, 0, 0)
pygame.draw.rect(window, BLACK, BrickWallRect)
PlayerRect = (150, 150, 0, 0)
Transparent = pygame.Surface((150, 150), pygame.SRCALPHA)
Transparent.fill((255,255,255,128))
pygame.draw.rect(window, BLACK, PlayerRect)
window.blit(Transparent, (0,0))

# set up playerpos and wallpos variables
playerpos = player()
wallpos = brickwall()
binpos = bin()
bikerackpos = bikerack()

#run game loop
running = True
while running:
    pressed = pygame.key.get_pressed()
    #if pygame.sprite.spritecollide(PlayerRect, BrickWallRect, True):
       # playerpos.x = 500
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False


    playerpos.handle_keys()
    pygame.draw.rect(window, GREY, road)
    playerpos.draw(window)
    pygame.display.update()
    window.fill(WHITE)
    wallpos.draw(window)
    binpos.draw(window)
    bikerackpos.draw(window)

    clock.tick(60)

pygame.quit()
quit()