#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
- A circle and rectangle move autonomously within the game window.
- The polygon can be moved using the arrow keys.
- If you press 'R', all the "fish" turn red, 
- If you press 'G', all the "fish" turn green until the key is released.
- Three cases can be run, depending on which section of code is uncommented:
    
    1. The square and rectangle move towards the mouse curser; 
    Their velocity is proportional to their distance from the mouse.
    
    2. The circle and rectangle are scared of the mouse curser.
    They move away from it. 
    
     3. If you right click on the rectangle it disappears
    
"""

import pygame 
import sys
import numpy as np
from pygame.math import Vector2
import math
import random

# 1. Initailise the pygame library
pygame.init()

x = 0
y = 1

flag = True
rectangle = True

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
circ_vel = [1, 1]
circ_pos = [100, 50] 
radius = 20  
circ_col = white

# rectangle variables
rect_vel = [2, 1]
rect_pos = [30, 30]  
rect_width = 60
rect_height = 80
rect_col = red

# polygon and line variables
poly_vel = [1, 2]
poly_pos = [[100, 100], [150, 150], [100, 150], [50, 125]] 
poly_col = green
line_col = black

position = [circ_pos, rect_pos] 
velocity = [circ_vel, rect_vel] 
horizontal = [[radius, radius], [rect_width, 0]] 
vertical = [[radius, radius], [rect_height, 0]]

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
    mouse_pos = pygame.mouse.get_pos()
    #print(mouse_pos)    
    
    # 5.4 Check for mouse press
    mouse_press = pygame.mouse.get_pressed()
    left_click = mouse_press[0]
    mid_click = mouse_press[1]
    right_click = mouse_press[2]



    # **** HOMEWORK : KEYBOARD PRESS ****
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
       

    # The up, down, left and right keys move the polygon.
    if pressed[pygame.K_UP]:
        poly_vel[y] = -3
    elif pressed[pygame.K_DOWN]:                     
        poly_vel[y] = 3
    else:
        poly_vel[y] = 0
        
    if pressed[pygame.K_LEFT]: 
        poly_vel[x] = -3
    elif pressed[pygame.K_RIGHT]: 
        poly_vel[x] = 3
    else:
        poly_vel[x] = 0
      
    
    
    # update the polygon position 
    for pos in poly_pos:   
        if not (
                # within window limits
                (pos[y] > 0 and pos[y] < win_height) or
                # velocity moves shape stuck at boundary in opposite direction
                (pos[y] >= win_height and poly_vel[y] < 0) or 
                (pos[y] <= 0 and poly_vel[y] > 0)
                ):
            break
    
    else:
        for pos in poly_pos: 
            pos[y] += poly_vel[y]
            
    for pos in poly_pos:   
        if not (
                # within window limits
                (pos[x] > 0 and pos[x] < win_width) or
                # velocity moves shape stuck at boundary in opposite direction
                (pos[x] >= win_width and poly_vel[x] < 0) or 
                (pos[x] <= 0 and poly_vel[x] > 0)
                ):
            print('break!')
            break

    else:
        for pos in poly_pos: 
            pos[x] += poly_vel[x]
 
    
    
    # If you left click a location, the circle swims to that location
    if left_click:
        left_clicked = True
        target_pos = mouse_pos
        velocity[0] = [3 * Vector2((target_pos[x] - circ_pos[x]), 
                                (target_pos[y] - circ_pos[y])).normalize()[0],
                       3 * Vector2((target_pos[x] - circ_pos[x]), 
                                (target_pos[y] - circ_pos[y])).normalize()[1]]
        
        
                    
    # update the circle and rectangle position
    for vel, pos, vert, horiz in zip(velocity, position, vertical, horizontal):
        print(circ_pos, rect_pos)          
        pos[x] += vel[x]  
        pos[y] += vel[y]
        
        # distance mouse to fish
        distx = mouse_pos[x] - pos[x]
        disty = mouse_pos[y] - pos[y] 
        dist = math.sqrt(distx**2 + disty**2)
        norm = Vector2(distx, disty).normalize()
        

# **** HOMEWORK : UNCOMMENT EITHER 1, 2, or 3 ****    

 # **** HOMEWORK : MOUSE POSITION ****    
# 1. The square and rectangle move towards the mouse curser; 
# Their velocity is proportional to their distance from the mouse.
##############################################################################   
#            vel[x] += norm[x]*0.2
#            vel[y] += norm[y]*0.2
##############################################################################        
# end of 1.



 # **** HOMEWORK : MOUSE POSITION ****    
# 2. The circle and rectangle are scared of the mouse curser.
# They move away from it.         
##############################################################################        
           
#        if math.fabs(dist) < 100:
#            flag = True
#            vel[x] = - norm[x] * (-0.08 * distx + 10)
#            vel[y] = - norm[y] * (-0.08 * disty + 10)
#        else:
#            if flag:
#                vel[x] = random.randrange(2,4)
#                if random.randrange(0,2) == 0:
#                    vel[x] *= -1
#                flag = False
#                else:   
#                    pass
##############################################################################
# end of 2. 
        
        
        # Leave uncommented : Collision with boundary, reverse direction
        if pos[x] > (win_width - horiz[0]) or pos[x] < horiz[1]:
            vel[x] *= -1
        if pos[y] > (win_height - vert[0]) or pos[y] < vert[1]:
            vel[y] *= -1
                
 
    
    
 # **** HOMEWORK : MOUSE CLICK ****
 # 3. If you right click on the rectangle it disappears 
##############################################################################               
    if (right_click and 
        (rect_pos[x] < mouse_pos[x] < rect_pos[x] + rect_width) and 
        (rect_pos[y] < mouse_pos[y] < rect_pos[y] + rect_height)):
        rectangle = False        
##############################################################################        
# end of 3.  
    
        
    
    
    
    
    
    # 5. Draw
    window.fill(blue)
    # 
    
    # 5.1 Draw Shapes
    # circle
    pygame.draw.circle(window, 
                       circ_col, 
                       (int(circ_pos[0]), int(circ_pos[1])), 
                       radius)
    
    # rectangle
    #pygame.draw.rect(window, white, pygame.Rect(30, 300, 60, 80))
    if rectangle:
        pygame.draw.rect(window, 
                         rect_col, 
                         pygame.Rect(rect_pos[0], 
                                     rect_pos[1], 
                                     rect_width, 
                                     rect_height, 
                                     width=10))
   
    # ploygon
    pygame.draw.polygon(window, poly_col, poly_pos)
    # multiple continuous lines
    pygame.draw.lines(window, line_col, True, poly_pos, 3)  
                
                     
    # 6. Update display
    pygame.display.update()
    
    # 7. Frame rate
    clock = pygame.time.Clock().tick(60)