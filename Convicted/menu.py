import pygame, sys
import os
from pygame.locals import *

# Set up pygame
pygame.init()

# Set up colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define button rects
playbuttonrect = (560, 355, 190, 30)
loadbuttonrect = (500, 410, 300, 30)
optionsbuttonrect = (540, 470, 250, 30)
extrasbuttonrect = (550, 520, 220, 40)
exitbuttonrect = (580, 570, 190, 40)

# Set up window
WINDOW_WIDTH = 1300
WINDOW_HEIGHT = 1000

# Set up background
background = pygame.image.load('Menu Design 1.5-1.png')
background = pygame.transform.scale(background,(WINDOW_WIDTH, WINDOW_HEIGHT))

# Load buttons and icons
playbutton = pygame.image.load('1 - Play.png')
loadbutton = pygame.image.load('2 - Load Game.png')
optionsbutton = pygame.image.load('3 - Options.png')
extrasbutton = pygame.image.load('4 - Extras.png')
exitbutton = pygame.image.load('5 - Exit.png')
icon = pygame.image.load('8bitDude.jpg')

# Blit window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
window.blit(background, (0, 0))

# Draw button rects

pygame.display.set_icon(icon)

# Blit menu to screen
pygame.display.set_caption('Main Menu')
window.blit(playbutton, (560, 320))
window.blit(loadbutton, (470, 380))
window.blit(optionsbutton, (520, 430))
window.blit(extrasbutton, (515, 480))
window.blit(exitbutton, (570, 530))
pygame.display.update()

running = True
while running:
    pygame.draw.rect(window, BLACK, playbuttonrect)
    pygame.draw.rect(window, BLACK, loadbuttonrect)
    pygame.draw.rect(window, BLACK, optionsbuttonrect)
    pygame.draw.rect(window, BLACK, extrasbuttonrect)
    pygame.draw.rect(window, BLACK, exitbuttonrect)
    mousePos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if click[0] == True:
        import main.py
    if pygame.mouse.get_pos(loadbuttonrect):
        print "Load"
    if pygame.mouse.get_pos(optionsbuttonrect):
        print "Options"
    if pygame.mouse.get_pos(extrasbuttonrect):
        print "Extras"
    if pygame.mouse.get_pos(exitbuttonrect):
        print "Exit"
    else:
        print "Error"
    #if pygame.mouse.get_pressed(loadbuttonrect):

    #if pygame.mouse.get_pressed(optionsbuttonrect):

    #if pygame.mouse.get_pressed(extrasbuttonrect):

    #if pygame.mouse.get_pressed(exitbuttonrect):

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False

pygame.quit()
quit()