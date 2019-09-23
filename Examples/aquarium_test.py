#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 23:33:55 2019

@author: hemma
"""

import pygame
import sys

# 1. Initailise the pygame library
pygame.init()

# 2. Variables
black = (0,0,0)
white = (255, 255, 255)
red =   (255, 0, 0)
green = (0, 255, 0)
blue =  (0, 0, 255)
# circle variables
circ_vel = [5, 1]
circ_pos = [100, 50]  
radius = 20  

# rectangle variables
rect_vel = [-2, -3]
rect_pos = [30, 300]  
rect_height = 80
rect_width = 60 

position = [circ_pos, rect_pos]
velocity = [circ_vel, rect_vel]  
horizontal = [[radius, radius], [rect_width, 0]]
vertical = [[radius, radius], [rect_height, 0]] 

# 3. Launch a game window
window = pygame.display.set_mode((600, 400))

# 4. Set up the main game loop
while True:
    
    # 5. Event Processing
    event = pygame.event.poll()
    
    if event.type == pygame.QUIT:        
        pygame.quit()
        sys.exit()  
        
#    elif event.type == pygame.MOUSEBUTTONDOWN:
#                print("User pressed a mouse button")
        
    # 6. Calculations
    
    # 6.1 Reverse direction of travel if edge is reached
    for vel, pos, vert, horiz in zip(velocity, position, vertical, horizontal):
        if pos[0] > (600-horiz[0]) or pos[0] < vert[1]:
            vel[0] *= -1
        if pos[1] > (400-vert[0]) or pos[1] < horiz[1]:
            vel[1] *= -1

        # 6.2 Update shape position
        pos[0] += vel[0]  
        pos[1] += vel[1]
    
    # window.fill((255, 255, 255))
    window.fill(black)
    # 7.1 Draw Shapes
    pygame.draw.circle(window, green, (circ_pos[0], circ_pos[1]), radius)
    pygame.draw.rect(window, white, pygame.Rect(rect_pos[0], rect_pos[1], rect_width, rect_height))
     


    # 8. Update display
    pygame.display.update()
    
    
    # 9. Frame rate
    clock = pygame.time.Clock().tick(60)