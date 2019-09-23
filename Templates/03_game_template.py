"""
Created on Tue May  8 09:02:36 2018

@author: hemma

A template with the basic Pygame setup :
0. Import libraries
1. Initailise the pygame library
2. Variables
3. Launch a game window
4. Set up the main game loop
5. Event Processing
6. Calculations 
7. Draw 
8. Update display once per loop
9. Set frame rate

"""

# 0. Import libraries
import pygame 
import sys
import math
import random

# 1. Initailise the pygame library
pygame.init()

# 2. Variables
x = 0
y = 1

# 2.1 colours
black = (0,0,0)
white = (255, 255, 255)
red =   (255, 0, 0)
green = (0, 255, 0)
blue =  (0, 0, 255)

# 2.2 window
win_width = 600
win_height = 400


# 3. Launch a game window
window = pygame.display.set_mode((win_width, win_height))


# 4. Set up the main game loop
while True:
    
    # 5. Event Processing
    event = pygame.event.poll()
    # 5.1 Check if the user has quit the game
    if event.type == pygame.QUIT:        
        pygame.quit()
        sys.exit()  
#    elif event.type == pygame.MOUSEBUTTONDOWN:
#        print("User pressed a mouse button")
        
    # 6. Calculations
        
    # 7. Draw 
    window.fill(blue)

    # 8. Update display
    pygame.display.update()
    
    # 9. Frame rate
    clock = pygame.time.Clock().tick(60)