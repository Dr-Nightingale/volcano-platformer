#importing modules
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
screen_height=800

#setting player size
player_size_x=10
player_size_y=10

#setting platform size
platform_x=110
platform_y=10
#setting colour presets
background_red=(169,62,62)
background_blue=(68,121,207)
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

        self.pos=vec((20,25))
        self.vel=vec(0,0)
        self.acc=vec(0,0.125)

    '''defines which keys move the player rectangle in what way, as
    well as affecting this movement using the established physics'''
    #defining player movement
    def move(self):
        self.acc=vec(0,0.125)

        keys=pygame.key.get_pressed()
        if level_number == 1 or level_number == 2:
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
        if level_number==0:
            touch=pygame.sprite.spritecollide(plyr,platforms_1,False)
        if level_number == 1:
            touch=pygame.sprite.spritecollide(plyr,platforms_1,False)
        if level_number == 2:
            touch=pygame.sprite.spritecollide(plyr,platforms_2,False)
        if level_number == 3 or level_number >= 3:
            touch=pygame.sprite.spritecollide(plyr,platforms_1,False)
        
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

platform_values1=[
    (145, 740, platform_red),
    (295, 690, platform_red),
    (165, 635, platform_red),
    (60, 580, platform_red),
    (210, 530, platform_red),
    (385, 480, platform_red),
    (450, 250, platform_red),
    (750, 340, platform_red),
    (640, 380, platform_red),
    (500, 420, platform_red),
    (625, 290, platform_red),
    (275, 210, platform_red),
    (375, 150, platform_red),
    (480, 75, platform_red),
    (350, 25, platform_red),
    (175, -15, platform_red),
    (50, -50, platform_red),
    (150, -125, platform_red),
    (350, -175, platform_red),
    (425, -250, platform_red),
    (650, -275, platform_red)]

platform_values2=[
    (200, 500, platform_blue),
    (400, 450, platform_blue),
    (755,375,platform_blue),
    (650,425,platform_blue),
    (450,400,platform_blue),
    (300,425,platform_blue),
    (105,440,platform_blue),
    (245,550,platform_blue),
    (475,575,platform_blue),
    (625,625,platform_blue),
    (500,675,platform_blue),
    (650,725,platform_blue),
    (75,675,platform_blue),
    (140,625,platform_blue),
    (360,700,platform_blue),
    (340,625,platform_blue),
    (200, 300, platform_blue),
    (400, 50, platform_blue),
    (755,175,platform_blue),
    (450,125,platform_blue),
    (450,200,platform_blue),
    (300,125,platform_blue),
    (105,240,platform_blue),
    (245,150,platform_blue),
    (475,275,platform_blue),
    (625,325,platform_blue),
    (500,475,platform_blue),
    (650,125,platform_blue),
    (75,75,platform_blue),
    (140,25,platform_blue),
    (360,50,platform_blue),
    (340,25,platform_blue),
    (475,25,platform_blue),
    (625,-15,platform_blue),
    (500,-75,platform_blue),
    (650,-180,platform_blue),
    (75,-75,platform_blue),
    (140,-125,platform_blue),
    (360,-50,platform_blue),
    (340,-190,platform_blue),
    (200,-60,platform_blue),
    (550,-240,platform_blue)]

platform_list1=[]
for x,y,colour in platform_values1:
    platform_list1.append(platform(x=x,y=y,colour=colour))
platform_list2=[]
for x,y,colour in platform_values2:
    platform_list2.append(platform(x=x,y=y,colour=colour))

floor=platform(screen_width,485,player_red)
trophy_1=sprite(20,25,700,-290,player_red)
trophy_2=sprite(20,25,600,-245,player_red)
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
platforms.add(*platform_list1)
platforms.add(*platform_list2)
platforms.add(floor)

platforms_1=pygame.sprite.Group()
platforms_1.add(*platform_list1)
platforms_1.add(floor)

platforms_2=pygame.sprite.Group()
platforms_2.add(*platform_list2)
platforms_2.add(floor)

trophies=pygame.sprite.Group()
trophies.add(trophy_1)
trophies.add(trophy_2)

trophies_1=pygame.sprite.Group()
trophies_1.add(trophy_1)

trophies_2=pygame.sprite.Group()
trophies_2.add(trophy_2)
 
 
line_number=(1)
level_number=(0)





def draw_screen(level_number,line_number):
    '''taking in the level number and drawing the corresponding objects/screen'''
    print(plyr.pos)
    if level_number == 0:
        for entity in platforms:
            window.blit(entity.surf,entity.rect)
        for entity in sprites:
            window.blit(entity.surf,entity.rect)
        
        window.fill(background_red)

        font=pygame.font.SysFont('freesansbold.ttf', 32)
        small_font=pygame.font.SysFont('freesansbold.ttf', 28)
        text_1="Welcome to Untitled Volcano Platformer!"
        text_2="press shift to begin"
        text_3="Use the left arrow button to move left and the right arrow button to move right"
        text_4="Use the up button to jump"
        text_5="You can hold left or right while jumping to move horizontally through the air"
        text_6="press space to progress dialogue"
        window.blit(font.render(text_1,True,text_colour),(175,230))
        window.blit(font.render(text_2,True,text_colour),(300, 340))
        window.blit(small_font.render(text_3,True,text_colour),(35, 500))
        window.blit(small_font.render(text_4,True,text_colour),(280, 535))
        window.blit(small_font.render(text_5,True,text_colour),(45, 620))
        window.blit(small_font.render(text_6,True,text_colour),(245, 565))

        

        keys=pygame.key.get_pressed()
        if keys[K_LSHIFT]:
            level_number += 1

        touch_win=pygame.sprite.spritecollide(plyr,trophies_1,False)
        
            
    if level_number==1:
        touch_win=pygame.sprite.spritecollide(plyr,trophies_1,False)
    if level_number==2:
        touch_win=pygame.sprite.spritecollide(plyr,trophies_2,False)
    if level_number== 3 or level_number >=3:
        touch_win=pygame.sprite.spritecollide(plyr,trophies_1,False)
    
    if touch_win:
        level_number +=1
        line_number = 1
        plyr.pos.y = 900
        plyr.pos.x = 25

    if level_number==1:
    #placing sprites in window based on the level number if applicable
        window.fill(background_red)

        for entity in trophies_1:
            window.blit(entity.surf,entity.rect)
        for entity in platforms_1:
            window.blit(entity.surf,entity.rect)
        for entity in sprites:
            window.blit(entity.surf,entity.rect)

    if level_number==2:
        window.fill(background_blue)
        for entity in trophies_2:
            window.blit(entity.surf,entity.rect)
        for entity in platforms_2:
            window.blit(entity.surf,entity.rect)
        for entity in sprites:
            window.blit(entity.surf,entity.rect)

    if level_number == 3 or level_number >= 3:
        window.fill(platform_grey)

        font=pygame.font.SysFont('freesansbold.ttf', 32)
        text_upper="Game Win!"
        text_lower="press space to play again"
        window.blit(font.render(text_upper,True,platform_blue),(300,250))
        window.blit(font.render(text_lower,True,platform_blue),(250, 300))
    
    return level_number, line_number

def play_again(level_number,line_number):
    if level_number == 3 or level_number >= 3:
        keys=pygame.key.get_pressed()
        if keys[K_SPACE]:
            level_number = 1
            line_number = 1
    return level_number,line_number

def narration(line_number,level_number):
    '''looks at the line and level numbers and places the corresponding text line on screen'''
    
    #defining the font and text position
    font=pygame.font.SysFont('freesansbold.ttf', 32)
    text_x=(30)

    #rendering text based on what the level number is
    if level_number == 0:
        text1=""
        text2=""
        text3=""
        text4=""

    if level_number == 1:

        #rendering text based on what the line number is
        if line_number==1:
            text1="thank you, Maui, truly! Although I must confess,"
            text2="I am not the easiest mountain to scale, I know you will succeed!"
            text3=""
            text4=""

        if line_number==2:
            text1=""
            text2=""
            text3=""
            text4=""

        if line_number==3:
            text1="Maui, my boy, do you remember when- ah, no you wouldn’t have been"  
            text2="born yet... were you ever taught the story of how the kiwi lost its" 
            text3="wings? Quite a funny story actually.."
            text4=""

        if line_number==4:
            text1="you see the bugs had been causing such a ruckus for the trees at the"
            text2="time, munching at their bark and getting them sick, and so one day"
            text3="Tāne Mahuta asks all the birds if any of them would agree to lose"
            text4="their wings and live on the ground, to eat all the bugs!"
            
        if line_number==5:
            text1="I remember the tui said he was too scared of the dark to do it, hah!"
            text2="And the pūkeko, oh no, he didn’t want to get his feet dirty! "
            text3="Even the pīpīwharauroa said no, said he was too busy building his nest!"
            text4=""
            
        if line_number==6:
            text1="Eventually the kiwi stuck his beak up and said he’d do it,which I’ll"
            text2="tell you, was a huge relief for everyone else. And then... what was it"
            text3="Tāne said? Oh yes, and then Tāne told the kiwi that he would be"
            text4="rewarded with love and fame for his sacrifice, and THEN"
        
        if line_number == 7:
            text1="he turns -and this is when it gets good- he turns to the other birds"
            text2="and starts dishing out punishments to everyone that refused!"
            text3="He gives the tui that white plume as a sign of his cowardice,"
            text4=" he banishes the pūkeko to live in the swamps for his vanity,"
        
        if line_number == 8:
            text1="and then he cursed the pīpīwharauroa to never build a nest again!"
            text2="Said he could only lay eggs in other bird’s nests! Anyway-"
            text3="where was I going with this? Ah forget it, Keep up the good work Maui!"
            text4=""

        if line_number == 9 or line_number >= 9:
            text1=""
            text2=""
            text3=""
            text4=""

    if level_number == 2:
        if line_number == 1:
            text1="You’re getting very close, Maui! Don’t give up now!"
            text2=""
            text3=""
            text4=""

        if line_number == 2:
            text1=""
            text2=""
            text3=""
            text4=""

        if line_number == 3:
            text1="Maui, my boy, how's the temperature down there? are you feeling"
            text2="alright? Well, you’d better be! I don’t mean to brag but my magma-"
            text3="and it IS magma, it’s only lava if it’s outside, you won’t believe how"
            text4="many people don’t know that- can get to well over a thousand degrees!"

        if line_number == 4:
            text1="You wouldn’t know it by my glorious coat of snow, but it’s true!"
            text2="Speaking of bragging… did you know that out of all the volcanoes"
            text3="on this island I am the tallest? Second tallest, actually, little"
            text4="Ruapehu has me beat by 279 metres."
        
        if line_number == 5:
            text1="But him and his brother Ngauruhoe are always erupting this way and"
            text2="that, trying to show off! They get it from their father, I suppose."
            text3="Not that Tongariro does more than blow smoke nowadays. Ahi!”"
            text4=""
        if line_number == 6 or line_number >= 6:
            text1=""
            text2=""
            text3=""
            text4=""

    if level_number == 3 or level_number >= 3:
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

#defining player position variables
gone_up=False
gone_down=False

#making it look like the screen is moving up and down based on the player's position
def platform_move():
    '''checking if the player's y value is less than 355 or more than 800 (below the screen)
    and sending all platforms up or down by 5 if so'''
    
    if plyr.pos.y<=330:
        for plat in platforms:
            plat.rect.y += 5
        for trophy in trophies:
            trophy.rect.y+=5
    
    if plyr.pos.y>=800:
        for plat in platforms:
            plat.rect.y -=5
        for trophy in trophies:
            trophy.rect.y-=5
            

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
    

    #calling various functions each gameloop
    level_number,line_number=draw_screen(level_number,line_number)
    plyr.move()
    plyr.update()
    platform_move()
    narration(line_number,level_number)
    level_number,line_number=play_again(level_number,line_number)
    



    #updating the screen
    pygame.display.flip()
    fpsclock.tick(fps)