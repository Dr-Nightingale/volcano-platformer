#importing modules
import pygame
from pygame.locals import*
import asyncio

#initialising pygame module
pygame.init()


#setting up physics
vec=pygame.math.Vector2
ACC=(0.25)
FRICT= (-0.10)
#setting game window size
screen_width=800
screen_height=800

#setting player size
player_size_x=10
player_size_y=10

#setting platform size
platform_x=110
platform_y=10
#setting colour presets
background_red=(169,62,62)
player_red=(47,23,23)
narrator_colour=(28,3,3)
text_colour=(140,5,3)
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

        self.pos=vec((700,300))
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

platform_values=[
    (145, 740, platform_blue),
    (295, 690, platform_green),
    (165, 635, platform_grey),
    (60, 580, platform_red),
    (210, 530, platform_blue),
    (385, 480, platform_green),
    (450, 250, platform_grey),
    (750, 340, platform_red),
    (640, 380, platform_blue),
    (500, 420, platform_green),
    (625,290, platform_grey),
    (275,210, platform_red),
    (375,150, platform_blue)]

platform_list=[]
for x,y,colour in platform_values:
    platform_list.append(platform(x=x,y=y,colour=colour))

floor=platform(screen_width,485,player_red)
trophy=sprite(20,25,500,110,player_red)
narrator=sprite(screen_width,350,400,50,narrator_colour)


#defining floor
floor.surf=pygame.Surface((screen_width,30))
floor.surf.fill((player_red))
floor.rect=floor.surf.get_rect(center=(400,785))



#putting the sprites together into groups
sprites=pygame.sprite.Group()
sprites.add(plyr)
sprites.add(floor)
sprites.add(narrator)


platforms=pygame.sprite.Group()
platforms.add(*platform_list)
platforms.add(floor)

trophies=pygame.sprite.Group()
trophies.add(trophy)


line_number=(0)
level_number=(0)

def narration(line_number,level_number):
    '''looks at the line and level numbers and places the corresponding text line on screen'''
    
    #defining the font and text position
    font=pygame.font.SysFont('freesansbold.ttf', 32)
    text_x=(30)

    #rendering text based on what the level number is
    if level_number==0:

        #rendering text based on what the line number is
        if line_number==0:
            text1="thank you, Maui, truly! Although I must confess,"
            text2="I am not the easiest mountain to scale, I know you will succeed!"
            text3=""
            text4=""

        if line_number==1:
            text1=""
            text2=""
            text3=""
            text4=""
        if line_number==2:
            text1="Maui, my boy, do you remember when- ah, no you wouldn’t have been"  
            text2="born yet... were you ever taught the story of how the kiwi lost its" 
            text3="wings? Quite a funny story actually.."
            text4=""

        if line_number==3:
            text1="you see the bugs had been causing such a ruckus for the trees at the"
            text2="time, munching at their bark and getting them sick, and so one day"
            text3="Tāne Mahuta asks all the birds if any of them would agree to lose"
            text4="their wings and live on the ground, to eat all the bugs!"
            
        if line_number==4:
            text1="I remember the tui said he was too scared of the dark to do it, hah!"
            text2="And the pūkeko, oh no, he didn’t want to get his feet dirty! "
            text3="Even the pīpīwharauroa said no, said he was too busy building his nest!"
            text4=""
            
        if line_number==5:
            text1="Eventually the kiwi stuck his beak up and said he’d do it,which I’ll"
            text2="tell you, was a huge relief for everyone else. And then... what was it"
            text3="Tāne said? Oh yes, and then Tāne told the kiwi that he would be"
            text4="rewarded with love and fame for his sacrifice, and THEN"
        
        if line_number == 6:
            text1="he turns -and this is when it gets good- he turns to the other birds"
            text2="and starts dishing out punishments to everyone that refused!"
            text3="He gives the tui that white plume as a sign of his cowardice,"
            text4=" he banishes the pūkeko to live in the swamps for his vanity,"
        
        if line_number == 7:
            text1="and then he cursed the pīpīwharauroa to never build a nest again!"
            text2="Said he could only lay eggs in other bird’s nests! Anyway-"
            text3="where was I going with this? Ah forget it, Keep up the good work Maui!"
            text4=""

        if line_number >= 8:
            text1=""
            text2=""
            text3=""
            text4=""

    if level_number >= 2:
        if line_number>= 0:
            text1=""
            text2=""
            text3=""
            text4=""

    window.blit(font.render(text1,True,text_colour),(text_x,40))
    window.blit(font.render(text2,True,text_colour),(text_x,80))   
    window.blit(font.render(text3,True,text_colour),(text_x,120))
    window.blit(font.render(text4,True,text_colour),(text_x,160))


#setting the framerate
fps=230
fpsclock=pygame.time.Clock()

gone_up=False
gone_down=False

#making it look like the screen is moving up and down based on the player's position
def platform_move(gone_up,gone_down):
    '''checking if the player's y value is less than 355 or more than 800 (below the screen)
    and sending all platforms up or down by 5 if so'''

    if gone_up==False:
        if plyr.pos.y<=355:
            for plat in platforms:
                plat.rect.y += 5
            trophy.rect.y+=5
            gone_up=True  

    if gone_down==False:
        if plyr.pos.y>=800:
            for plat in platforms:
                plat.rect.y -=5
            trophy.rect.y-=5
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
        #checking if the player wants to jump or progress the narrator when they press a key
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                plyr.jump()
            if event.key==pygame.K_SPACE:
                line_number+=1

    #setting background colour
    window.fill(background_red)

    #placing sprites in window
    for entity in trophies:
        window.blit(entity.surf,entity.rect)
    for entity in platforms:
        window.blit(entity.surf,entity.rect)
    for entity in sprites:
        window.blit(entity.surf,entity.rect)
    

    #calling various functions each gameloop
    plyr.move()
    plyr.update()
    platform_move(gone_up,gone_down)
    narration(line_number,level_number)

    #updating the screen
    pygame.display.flip()
    fpsclock.tick(fps)