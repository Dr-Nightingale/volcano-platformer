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

        self.pos=vec((25,485))
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
pltfrm1=platform(x=145,y=440,colour=platform_blue)
pltfrm2=platform(x=295,y=390,colour=platform_green)
pltfrm3=platform(x=165,y=335,colour=platform_grey)
pltfrm4=platform(x=60,y=280,colour=platform_red)
pltfrm5=platform(x=210,y=230,colour=platform_blue)
pltfrm6=platform(x=385,y=180,colour=platform_green)
pltfrm7=platform(x=575,y=275,colour=platform_grey)
pltfrm8=platform(x=750,y=40,colour=platform_red)
pltfrm9=platform(x=640,y=80,colour=platform_blue)
pltfrm10=platform(x=500,y=120,colour=platform_green)
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
sprites.add(trophy)

platforms=pygame.sprite.Group()
platforms.add(pltfrm1,pltfrm2,pltfrm3,pltfrm4,pltfrm5,pltfrm6,pltfrm7,pltfrm8,pltfrm9,pltfrm10)
platforms.add(floor)

trophies=pygame.sprite.Group()
trophies.add(trophy)

#setting the framerate
fps=230
fpsclock=pygame.time.Clock()


#setting up a win screen 
'''checks if the win condition is active, and if so, draws over the window to
show a win screen that prompts the player to press the space button. pressing the space
button changes the player's position back to the start of the level which makes 
the win condition unfulfilled and changes the screen back'''
def go_up():
    #checking if the player has fulfilled the win conditions
    
    if plyr.pos.y<=0:
        up=True
    else:
        up=False
    if up==True:
       for objects in platforms:
           y += 500

           


        
    return up



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

    #putting up the win screen if the win conditions are met
    go_up()

    pygame.display.flip()
    fpsclock.tick(fps)