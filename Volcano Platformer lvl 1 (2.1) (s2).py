#importing pygame module
import pygame
from pygame.locals import*

#initialising pygame module
pygame.init()

#setting up physics
vec=pygame.math.Vector2
ACC=(0.25)
FRICT= (-0.10)
#setting game window size
screen_width=800
screen_height=500

#setting player size
player_size_x=10
player_size_y=10

#setting platform size
platform_x=110
platform_y=10
#setting colour presets
background_red=(169,62,62)
player_red=(47,23,23)
#all the platforms will look the same later but for now I need to be able to tell them apart easily
platform_red=(255,0,0)
platform_blue=(0,0,255)
platform_green=(0,255,0)
platform_grey=(128,128,128)

#setting the game window variable
window=pygame.display.set_mode((screen_width, screen_height))
title=pygame.display.set_caption("Volcano Platformer")



#defining the player sprite
class Player(pygame.sprite.Sprite):

    '''defines the appearance and dimensions of the player and uses those values 
    to form a corresponding surface and rectangle'''
    def __init__ (self):
        super().__init__()
        self.surf=pygame.Surface((player_size_x,player_size_y))
        self.surf.fill((player_red))
        self.rect=self.surf.get_rect()

        self.pos=vec((775,40))
        self.vel=vec(0,0)
        self.acc=vec(0,0.125)

    '''defines which keys move the player rectangle in what way, as
    well as affecting this movement using the established physics'''
    #defining player movement
    def move(self):
        self.acc=vec(0,0.125)

        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x= -ACC
        if keys[pygame.K_RIGHT]:
            self.acc.x= ACC

        self.acc.x+=self.vel.x * FRICT
        self.vel+=self.acc
        self.pos+=self.vel+0.5 * self.acc
        self.rect.midbottom=self.pos
    
    '''allows the player rectangle to jump if it is touching a platform/the floor
    by subtracting it's vertical velocity'''
    #defining player jumping
    def jump(self):
        touch=pygame.sprite.spritecollide(self,platforms,False)
        if touch:
            self.vel.y= -4

    '''stops the player's vertical movement from increasing if they are 
    touching a platform, as well as stopping the horizontal movement from 
    increasing/decreasing if they have reached the edges of the window'''     
    #making it so the player doesn't clip through platforms or the walls
    def update(self):
        touch=pygame.sprite.spritecollide(plyr,platforms,False)
        if plyr.vel.y>0:
            if touch:
                self.pos.y=touch[0].rect.top +1
                self.vel.y=0
        if plyr.pos.x>screen_width:
            plyr.pos.x=screen_width
        if plyr.pos.x<0:
            plyr.pos.x=0

    
    
#defining the platform sprite
class platform(pygame.sprite.Sprite):

    '''takes in the values and dimensions of a given platform and uses those values 
    to form a corresponding surface and rectangle'''
    def __init__ (self,x,y,colour):
        super().__init__()
        self.surf=pygame.Surface((platform_x,platform_y))
        self.surf.fill((colour))
        self.rect=self.surf.get_rect(center=(x,y))
        self.rect.x=x
        self.rect.y=y
        self.pos=vec(x,y)


        
#defining everything else
class sprite(pygame.sprite.Sprite):

    '''takes in the values and dimensions of a given sprite and uses those values 
    to form a corresponding surface and rectangle'''
    def __init__ (self,sprite_x,sprite_y,x,y,colour):
        super().__init__()
        self.surf=pygame.surface.Surface((sprite_x,sprite_y))
        self.surf.fill((colour))
        self.pos=(x,y)
        self.rect=self.surf.get_rect(center=(x,y))
        

#creating platforms and assigning classes
plyr=Player()

platform_values=[(145, 440, platform_blue),
    (295, 390, platform_green),
    (165, 335, platform_grey),
    (60, 280, platform_red),
    (210, 230, platform_blue),
    (385, 180, platform_green),
    (500, -50, platform_grey),
    (750, 40, platform_red),
    (640, 80, platform_blue),
    (500, 120, platform_green),
    (625,-10,platform_grey)]

platform_list=[]
for x,y,colour in platform_values:
    platform_list.append(platform(x=x,y=y,colour=colour))


pltfrm11=platform(625,-10,platform_grey)
floor=platform(400,485,player_red)
trophy=sprite(20,25,500,110,player_red)


#defining floor
floor.surf=pygame.Surface((screen_width,30))
floor.surf.fill((player_red))
floor.rect=floor.surf.get_rect(center=(400,485))



#putting the sprites together into groups
sprites=pygame.sprite.Group()
sprites.add(plyr)
sprites.add(floor)
sprites.add()

platforms=pygame.sprite.Group()
platforms.add(*platform_list)
platforms.add(floor)

trophies=pygame.sprite.Group()
trophies.add()

#setting the framerate
fps=230
fpsclock=pygame.time.Clock()

gone_up=False
gone_down=False

def platform_move(gone_up,gone_down):
    '''checking if the player's y value is less than 0 (above the screen) or more than 500 (below the screen)
    and sending all platforms up or down by 500 if so'''

    #making sure the code doesn't repeat every frame and only executes once

    if gone_up==False:
        if plyr.pos.y<=0:
            for plat in platforms:
                plat.rect.y += 5
            gone_up=True
        
        

    if gone_down==False:
        if plyr.pos.y>=500:
            for plat in platforms:
                plat.rect.y -=10
            gone_down=True
        
    
    return (gone_up,gone_down)
    

            
             


    
        
        
        
    

        
    



#making a bool value to check if the game is running
running=True

#starting the main game loop
while running:

    
    #checking for event in queue
    for event in pygame.event.get():

        #setting running bool to false if event type is quit
        if event.type==pygame.QUIT:
            running=False
        #checking if the player wants to jump when they press a key
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                plyr.jump()


    #setting background colour
    window.fill(background_red)

    #placing sprites in window
    for entity in sprites:
        window.blit(entity.surf,entity.rect)
    for entity in platforms:
        window.blit(entity.surf,entity.rect)

    plyr.move()
    plyr.update()
    platform_move(gone_up,gone_down)


    pygame.display.flip()
    fpsclock.tick(fps)