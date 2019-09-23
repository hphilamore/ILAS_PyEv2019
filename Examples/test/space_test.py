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
mix.music.load("../../Sounds/battleThemeB.mp3") # load music
mix.music.set_volume(0.3) # set volume
mix.music.play(-1, 0.0) # play music on repeat

# 2. Variables
x = 0
y = 1
monster_exists = True

# 2.1 colours
black = (0,0,0)
white = (255, 255, 255)
red =   (255, 0, 0)
green = (0, 255, 0)
blue =  (0, 0, 255)

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
if random.randrange(0,2) == 0:
    monster_vel[y] *= -1
    
# 2.4 List to store shots 
shots = []
    

# 3. Launch a game window
window = pygame.display.set_mode((win_width, win_height))
# 3.1 Import images
background = pygame.image.load("../../img/space.jpg").convert()
b_size = background.get_rect().size
print('b_size=', b_size)

# 3.2 Import sounds
zap = mix.Sound("../../Sounds/zap8a.ogg")

saucer = pygame.image.load("../../img/saucer.png")
s_size = saucer.get_rect().size

monster = pygame.image.load("../../img/monster.png")
m_size = monster.get_rect().size

fire = pygame.image.load("../../img/fire.png")
f_size = fire.get_rect().size

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
            
    if pressed[pygame.K_LEFT] & pressed[pygame.K_RIGHT]: 
            saucer_vel[x] = 0
    elif pressed[pygame.K_LEFT]: 
            saucer_vel[x] = -8
    elif pressed[pygame.K_RIGHT]: 
            saucer_vel[x] = 8
    else: 
            saucer_vel[x] = 0
            
    # 5.3 Mouse position  
    mouse_pos = pygame.mouse.get_pos()
    
    # 5.4 Mouse click
    if event.type==pygame.MOUSEBUTTONDOWN:
        mouse_click = True
    else:
        mouse_click = False
        
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
    
    # 6.5 Fire a shot
    if mouse_click:

        # 6.5.1 play sound effect
        zap.play()   
    
    
        # 6.5.2 add shot to the list of shots
        shot_pos = [saucer_pos[x] + s_size[x]/2 - f_size[x]/2, 
                    saucer_pos[y] + s_size[y]/2 - f_size[y]/2]
    
        shots.append([angle, shot_pos])
        
    # 6.6 Iterate over all shots, giving each one a number
    for n, shot in enumerate(shots):
        print(n)
        speed = 20
        shot_vel = [math.cos(shot[0]) *speed, 
                    -math.sin(shot[0])*speed] # y direction down=positive
   
        # 6.6.1 Update fireball position
        shot[1][x] += shot_vel[x]
        shot[1][y] += shot_vel[y]
        
        # 6.6.2 If the fireball leaves the screen, remove it from the list of shots
        shot_len = max(f_size[x],f_size[y])
        if (shot[1][x] > b_size[x] + shot_len or 
            shot[1][x] < - shot_len or 
            shot[1][y] > b_size[y] + shot_len or 
            shot[1][y] < - shot_len):
            shots.pop(n)
            
        # 6.6.3. Monster hit, turn off monster
        if ((monster_pos[x]  <  shot[1][x]  <  monster_pos[x] + m_size[x])
            and 
            (monster_pos[y]  <  shot[1][y]  <  monster_pos[y] + m_size[y])):
            monster_exists = False
 
    # 7. Draw 
    # 7.1 Draw background
    # window.fill(blue)
    window.blit(background, [0, 0])
    # window.fill(blue)
    
    # 7.2 Draw features
    # window.blit(saucer, saucer_pos)
    window.blit(saucer_r, saucer_pos)
    #window.blit(monster, monster_pos)
    if monster_exists:
        window.blit(monster, monster_pos)
    for shot in shots:
        shot_r = pygame.transform.rotate(fire, math.degrees(shot[0]) - 90)
        window.blit(shot_r, shot[1])
    
    # 7.3 Draw text on screen
    font_size = 26
    #font = pygame.font.SysFont(None, font_size) # default font
    font = pygame.font.SysFont('helveticaneuedeskinterface', font_size)
    space_green = (0,250,154)
    text = font.render("Space Game!", True, space_green)
    window.blit(text,         # text to print
            (800/2, 550))     # x, y position of text

    # 8. Update display
    pygame.display.update()
    
    # 9. Frame rate
    clock = pygame.time.Clock().tick(60)