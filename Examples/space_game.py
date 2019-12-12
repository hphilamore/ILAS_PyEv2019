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
import pygame.mixer as mix

# 1. Initailise the pygame library
pygame.init()
mix.init() # initialise music player

mix.music.load("../Sounds/battleThemeB.mp3") # load music
mix.music.set_volume(0.3) # set volume
mix.music.play(-1, 0.0) # play music on repeat

# 2. Variables
x = 0
y = 1

# 2.1 colours
black = (0,0,0)
white = (255, 255, 255)
red =   (255, 0, 0)
green = (0, 255, 0)
blue =  (0, 0, 255)
space_green = (0,250,154)

# 2.2 window
win_width = 800
win_height = 600

# 2.3 Position and velocity variables 
monster_pos =[200, 200]                   
saucer_pos = [200, 25]
saucer_vel = [0, 0]
monster_vel = [random.randrange(10,12), random.randrange(10,12)]
if random.randrange(0,2) == 0:
    monster_vel[x] *= -1
    

# 3. Launch a game window
window = pygame.display.set_mode((win_width, win_height))

# 3.1 Import images
background = pygame.image.load("../img/space.jpg").convert()
b_size = background.get_rect().size
print('b_size=', b_size)

# 3.1 Import images
saucer = pygame.image.load("../img/saucer.png")
s_size = saucer.get_rect().size

monster = pygame.image.load("../img/monster.png")
m_size = monster.get_rect().size

# 3.2 Import sounds
zap = mix.Sound("../Sounds/zap8a.ogg")



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
        
    # 5. Event Processing
    # 5.2 Check if any keys have been pressed 
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] & pressed[pygame.K_DOWN]: 
            saucer_vel[y] = 0
    elif pressed[pygame.K_UP]: 
            saucer_vel[y] = -8
    elif pressed[pygame.K_DOWN]: 
            saucer_vel[y] = 8
    else: 
            saucer_vel[y] = 0
            
    # 5.3 Mouse position  
    mouse_pos = pygame.mouse.get_pos()
        
    # 6. Calculations
    # 6.1 Reverse direction of travel if edge is reached        
    if monster_pos[x] > (win_width - m_size[x]) or monster_pos[x] < 0:
        monster_vel[x] *= -1
    if monster_pos[y] > (win_height - m_size[y]) or monster_pos[y] < 0:
        monster_vel[y] *= -1
    
    # 6.2 Update position
    monster_pos[x] += monster_vel[x]
    monster_pos[y] += monster_vel[y]
    saucer_pos[x] += saucer_vel[x]
    saucer_pos[y] += saucer_vel[y]
    
    # 6.3 Angle between mouse and saucer
    angle = math.atan2(-(mouse_pos[y] - (saucer_pos[y] + s_size[y]/2)),
                        (mouse_pos[x] - (saucer_pos[x] + s_size[x]/2)))
    
    # 6.4 Rotate the saucer
    saucer_r = pygame.transform.rotate(saucer, math.degrees(angle) - 90)
        
    
    # 7. Draw 
    # window.fill(blue)
    window.blit(background, [0, 0])    
    # 7.2 Draw features
    #window.blit(saucer, (100,100))
    # 7.2 Draw features
    #window.blit(saucer, saucer_pos)
    window.blit(saucer_r, saucer_pos)
    window.blit(monster, monster_pos)
    
    
    # 7.3 Draw text on screen
    font_size = 26
    #font = pygame.font.SysFont(None, font_size) # default font
    font = pygame.font.SysFont('helveticaneuedeskinterface', font_size)
    text = font.render("Space Game!", True, space_green)
    window.blit(text,         # text to print
               (250, 550))   # x, y position of text
    
    # 8. Update display
    pygame.display.update()
    
    # 9. Frame rate
    clock = pygame.time.Clock().tick(60)