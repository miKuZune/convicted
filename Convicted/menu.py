import pygame, sys
import os
from pygame.locals import *

# Set up pygame
pygame.init()

# Set up colours
black = (0, 0, 0)
white = (255, 255, 255)

# Set up window
WINDOW_WIDTH = 1300
WINDOW_HEIGHT = 1000
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Main Menu')

# Set up background
background = pygame.image.load('Menu Design 1.5-1.png')
background = pygame.transform.scale(background,(WINDOW_WIDTH, WINDOW_HEIGHT))
window.blit(background, (0, 0))

playbutton = pygame.image.load('1 - Play.png')
loadbutton = pygame.image.load('2 - Load Game.png')
optionsbutton = pygame.image.load('3 - Options.png')
extrasbutton = pygame.image.load('4 - Extras.png')
exitbutton = pygame.image.load('5 - Exit.png')
window.blit(playbutton, (500, 350))
window.blit(loadbutton, (500, 400))
window.blit(optionsbutton, (500, 450))
window.blit(extrasbutton, (500, 500))
window.blit(exitbutton, (550, 550))

pygame.display.update()

running = True
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False

pygame.quit()
quit()