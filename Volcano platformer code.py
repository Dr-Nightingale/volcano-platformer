#importing pygame module
import pygame

#initialising pygame module
pygame.init()

#setting game window size
screen_width=800
screen_height=500

#setting the game window variable
window=pygame.display.set_mode((screen_width, screen_height))

#making a bool value to check if the game is running
running=True

#setting colour presets
background_red=(169,62,62)
block_red=(47,23,23)

#setting player positions and dimensions (block for now)
block_size=30
block_x=80
block_y=470
block=pygame.Rect([block_x,block_y,block_size,block_size])

#setting platform positions and dimensions
platform_size_x=155
platform_size_y=20
platform_x=200
platform_y=480
platform=pygame.Rect([platform_x,platform_y,platform_size_x,platform_size_y])
#starting the main game loop
while running:

    #checking for event in queue
    for event in pygame.event.get():

        #setting running bool to false if event type is quit
        if event.type==pygame.QUIT:
            running=False

    #setting background colour
    window.fill(background_red)

    #giving player movement with arrow keys
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        block_x-=0.25
    
    if keys[pygame.K_RIGHT]:
        block_x+=0.25

    #putting player (block) in window
    pygame.draw.rect(window,block_red,[block_x,block_y,block_size,block_size])

    #putting platforms in window
    pygame.draw.rect(window,block_red,[platform_x,platform_y,platform_size_x,platform_size_y])

    #stop player from going through platform
    if block_x<=platform_x<=block_x+100:
        block_x=platform_x
    #updating the window
    pygame.display.flip()