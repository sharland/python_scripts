#! /usr/bin/env python3

# bat_ball.py: simple pygame demo

# import the pygame library
import pygame, random
# this saves us from typing in full paths to the pygame modules.
from pygame.locals import *
# initialise the game engine
pygame.init()

# initialise variables
FPS = 100               # Frames Per Second
size = 300, 300         # size of pygame window
title = "Bat and Ball"  # window title
bat_gap = 50            # gap between bat and bottom of window
speed = [1, 1]          # speed of ball
ball_size = 40, 40      # size of ball surface
ball_rad = 20           # radius of ball
bat_size = 64, 12       # size of bat

# define colours
raspberry = [135,  38,  87]
black     = [  0,   0,   0]
white     = [255, 255, 255]
blue      = [  0,   0, 255]
green     = [  0, 255,   0]
red       = [255,   0,   0]
yellow    = [255, 255,   0]

# set up the graphic window 
width, height = size
screen = pygame.display.set_mode(size)
screenrect = screen.get_rect()

# give the window a title
pygame.display.set_caption(title)

# This makes the normal mouse pointer invisible in graphics window
pygame.mouse.set_visible(False)

# make surfaces for bat and ball
# bat
bat_surf = pygame.Surface(bat_size)
bat_surf.fill(green)        
batrect = bat_surf.get_rect()
# ball
ball_surf = pygame.Surface((ball_size))
ball_surf.set_colorkey(black)
ballrect = ball_surf.get_rect()
ball = pygame.draw.circle(ball_surf, blue,[ballrect.centerx, ballrect.centery], ball_rad)

# puts the bat center of screen, near the bottom
batrect.center = (screenrect.centerx, (screenrect.bottom - bat_gap))

# make a text object
font = pygame.font.Font(None, 36)
text = font.render("Game Over.", True, (red))
textRect = text.get_rect()
textRect.centerx = screenrect.centerx
textRect.centery = screenrect.centery

# loop until the user clicks the close button
done=False

# create a timer to control how often the screen updates
clock = pygame.time.Clock()

# main game loop
while done==False:
    # fill the screen with a colour
    screen.fill(yellow)

    # event handling
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=True 

    # moves bat in accordance with the mouse position
    position = pygame.mouse.get_pos()
    batrect.centerx = position[0]

    # move the ball
    ballrect.left += speed[0]
    ballrect.top += speed[1]

    # collision detection
    if ballrect.left <= (batrect.right) and ballrect.right >= (batrect.left):
        if ballrect.bottom == batrect.top:
            speed[1] = -speed[1]

    #check if the ball is going off screen
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0:
        speed[1] = -speed[1]

    # print "Game Over" if the ball leaves screen
    if ballrect.top > screenrect.bottom:
        screen.blit(text, textRect)

    # blit the images to the screen
    screen.blit(bat_surf, batrect)
    screen.blit(ball_surf, ballrect)

    # set the loop to fps cycles per second
    clock.tick(FPS)

    #  update the display
    pygame.display.flip()

# close pygame
pygame.quit()
