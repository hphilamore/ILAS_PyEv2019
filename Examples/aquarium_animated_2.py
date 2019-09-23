#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 09:02:36 2018

@author: hemma
"""

import pygame 
import sys
import numpy as np

# 1. Initailise the pygame library
pygame.init()

# 2. Variables
win_width = 600
win_height = 400

black = (0,0,0)
white = (255, 255, 255)
red =   (255, 0, 0)
green = (0, 255, 0)
blue =  (0, 0, 255)

# circle variables
#x_pos = 100
#y_pos = 50
circ_vel = [5, 1]
circ_pos = [100, 50] 
radius = 20  
circ_col = white

# rectangle variables
rect_vel = [2, 3]
rect_pos = [30, 30]  
rect_width = 60
rect_height = 80
rect_col = red

# polygon and line variables
poly_vel = [2, 3]
poly_pos = [[100, 100], [150, 150], [100, 150], [50, 125]] 
poly_col = green
line_col = black


position = [circ_pos, rect_pos, poly_pos] 
velocity = [circ_vel, rect_vel, poly_vel] 
horizontal = [[radius, radius], [rect_width, 0], [0, 0]] 
vertical = [[radius, radius], [rect_height, 0], [0, 0]]

print(position)
print(velocity)
print(horizontal)
print(vertical)

# 3. Launch a game window
window = pygame.display.set_mode((win_width, win_height))

# 4. Set up the main game loop
while True:
    event = pygame.event.poll()
    
    if event.type == pygame.QUIT:        
        pygame.quit()
        sys.exit()  
        
    # 5. Event processing
    event = pygame.event.poll()
    
    # 5.1 Check if the user has quit the game
    if event.type == pygame.QUIT:        
        pygame.quit()
        sys.exit()  
    
    # 5.2 Check if any keys have been pressed    
    pressed = pygame.key.get_pressed()
    
    # 5.3 Get the mouse position   
    pos = pygame.mouse.get_pos()
    print(pos)    
    
    # 5.4 Check for mouse press
    mouse_press = pygame.mouse.get_pressed()
    left_click = mouse_press[0]
    mid_click = mouse_press[1]
    right_click = mouse_press[2]


    # If you press 'R', all the "fish" turn red, 
    # if you press 'G', all the "fish" turn green until the key is released.
    if pressed[pygame.K_r]: 
        poly_col, circ_col, rect_col = red, red, red
    elif pressed[pygame.K_g]:                     
        poly_col, circ_col, rect_col = green, green, green
    else: 
        poly_col, circ_col, rect_col = green, white, red
        
    # If you press Q, you quit the game    
    if pressed[pygame.K_q]: 
        pygame.quit()
        sys.exit() 
        
    # 5. Draw
    window.fill(blue)
    # 
    
    # 5.1 Draw Shapes
    # circle
    pygame.draw.circle(window, circ_col, (circ_pos[0], circ_pos[1]), radius)
    
    # rectangle
    #pygame.draw.rect(window, white, pygame.Rect(30, 300, 60, 80))
    pygame.draw.rect(window, rect_col, pygame.Rect(rect_pos[0], rect_pos[1], rect_width, rect_height, width=10))

    
    # ploygon
    pygame.draw.polygon(window, poly_col, poly_pos)
    
    # multiple continuous lines
    pygame.draw.lines(window, line_col, True, poly_pos, 3)
    # arc
    # pygame.draw.arc(screen, color, (x,y,width,height), start_angle, stop_angle, thickness)
    # rect = (x_center, y_center, height, width) = coordinates of a rectangle that the arc would fit inside if it were drawn all the way around
    # if height and width are equal, then the rectangle is a square, and the arc will be a portion of a circle
    # start_angle and stop_angle are the angle on the unit circle in radians (not degrees) where the arc stops and starts
#    arc_centre = (100, 100)
#    (x, y) = arc_centre
#    radius = 50
#    startDeg = 0
#    endDeg = 90
#    thickness = 5
#    rect = (x-radius,y-radius,radius*4,radius*2)
#    startRad = np.radians(startDeg)
#    endRad = np.radians(endDeg)
#
#    pygame.draw.arc(window, 
#                    red, 
#                    rect,
#                    startRad,
#                    endRad,
#                    thickness)

    
    # ellipse
    #pygame.draw.ellipse(window, green, rect, 1)
#                                        ,
#                                        ,
#   # line
    #pygame.draw.line(window, white, (0, win_height/2), (win_width, win_height/2), 3)                                    
#    
    

    
    # anti-aliased line
    # aaline(Surface, color, startpos, endpos, blend=1)
    #pygame.draw.aaline(window, red, (400, 400), (500, 500), True)
    
#    # 5.2 Reverse direction of travel if edge is reached
#    if circ_pos[0] > (win_width-radius) or circ_pos[0] < radius:
#        circ_vel[0] *= -1
#    if circ_pos[1] > (win_height-radius) or circ_pos[1] < radius:
#        circ_vel[1] *= -1
#        
#    if rect_pos[0] > (600-width) or rect_pos[0] < 0:
#        rect_vel[0] *= -1
#    if rect_pos[1] > (400-height) or rect_pos[1] < 0:
#        rect_vel[1] *= -1
#  
#    
#    # 5.3 Update circle position
##    x_pos += 1
##    y_pos += 1
#    circ_pos[0] += circ_vel[0]  
#    circ_pos[1] += circ_vel[1] 
#    
#    rect_pos[0] += rect_vel[0]  
#    rect_pos[1] += rect_vel[1] 
    
    # 6.3 Update ball position
#    distx = pos[x]-ball_pos[x]
#    disty = pos[y]-ball_pos[y]
#    norm = Vector2(distx, disty).normalize()
#    
#    ball_pos[x] += norm[x]
#    ball_pos[y] += norm[y]
    
    
    
    for vel, pos, vert, horiz in zip(velocity, position, vertical, horizontal):
        
        
        
        print('pos', pos)
        print('vel', vel)
        
        
        if not isinstance(pos[0], list):
            pos = [pos]
        
        for p in pos:           
            p[0] += vel[0]  
            p[1] += vel[1]
            
        
                
            if p[0] > (win_width - horiz[0]) or p[0] < horiz[1]:
                vel[0] *= -1
            if p[1] > (win_height - vert[0]) or p[1] < vert[1]:
                vel[1] *= -1
#            
#            
#        # 5.3 Update shape position
#        pos[0] += vel[0]  
#        pos[1] += vel[1] 
    
    # 6. Update display
    pygame.display.update()
    
    # 7. Frame rate
    clock = pygame.time.Clock().tick(60)