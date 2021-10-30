import pygame;import time
import random

pygame.init()

display_width = 800
display_height = 600
canvas = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()
carImg = pygame.image.load('racecar.png')
carWidth = 72
carHeight = 83
white=(255,255,255)
black=(0,0,0)
#################
def car(x,y):
    canvas.blit(carImg, (x,y)) #This fuction overlaps carImg in canvas at (x,y)
#######################
def crash():
    display_message('You Crashed')
#################################################
def display_message(text):
    font = pygame.font.Font('freesansbold.ttf',115)
    textSurface = font.render(text,True,black)
    textRect = textSurface.get_rect()
    textRect.center = (display_width/2,display_height/2)
    canvas.blit(textSurface,textRect)
    pygame.display.update()
    time.sleep(1)
    car_loop()
####################################################
def objects(objectx,objecty,objectw,objecth,color):
        pygame.draw.rect(canvas,color,[objectx,objecty,objectw,objecth])


#####################################################
def object_dodge_display(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Dodge:{}".format(count),True,black)
    canvas.blit(text,[0,0])
    pygame.display.update()
################################################################################
def car_loop():
    x =  (display_width/2-carWidth)
    y = (display_height-carHeight)
    crashed = False
    x_change = 0
    y_change = 0
######################################################
    objectSpeed = 6
    objecty = 0
    objectw = random.randrange(80,120)
    objectx = random.randrange(0,display_width-objectw)
    objecth = 70
######################################################
    count = 0
######################################################
    while not crashed:
##while is whole game loop
        #car movement loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        x+=x_change
        y+=y_change
        canvas.fill(white)
###############################################################################
        car(x,y)
        objects(objectx,objecty,objectw,objecth,black)
        object_dodge_display(count)
###############################################################################
        objecty+=objectSpeed #object speed
###############################################################################

        if objecty > display_height:
            objecty = 0
            objectx = random.randrange(0,display_width-objectw)
            objectw = random.randrange(80,120)
            count +=1
            objectSpeed +=0.05#increasing each time



        if x > display_width-carWidth or x < 0 or y > display_height-carHeight or y < 0 :
            crash()

        if y < objecty+objecth: #Y-crossover
            if (x > objectx and x < objectx + objectw) or (x+carWidth < objectx + objectw and x+carWidth > objectx):# x-crossover
                crash()


        pygame.display.update()
        clock.tick(80)

car_loop()
pygame.quit()
quit()
