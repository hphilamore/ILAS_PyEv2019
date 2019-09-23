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

# 1. Initailise the pygame library
pygame.init()


# 3. Launch a game window
window = pygame.display.set_mode((100, 100))


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