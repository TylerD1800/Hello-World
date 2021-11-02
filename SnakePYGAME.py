import pygame,sys,random,time
from pygame.locals import *

#Setup pygames#
pygame.init()


#Setup the window#
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode(
    (WINDOWWIDTH,WINDOWHEIGHT), 0, 32
    )
pygame.display.set_caption('Snake')
mainClock = pygame.time.Clock()

#Direction Variables#
U = 'up'
D = 'down'
L = 'left'
R = 'right'

#Set up the colors#
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,102)

#All the food code stuff#
FOODS = []
FOODSIZE = 10
FOODS.append(pygame.Rect(random.randint(FOODSIZE,WINDOWWIDTH-2*FOODSIZE),
        random.randint(FOODSIZE,WINDOWHEIGHT-2*FOODSIZE),FOODSIZE,FOODSIZE))

#Code for the game over screen#
font_style = pygame.font.SysFont(None, 50)
font_style1 = pygame.font.SysFont(None, 25)
score_font = pygame.font.SysFont('sfcompactroundedregularotf',25)

#function you call to dispplay the GAME OVER message#
def message(msg1,msg2,msg3,color):
    mesg1 = font_style.render(msg1,True,color)
    mesg2 = font_style1.render(msg2,True,color)
    mesg3 = font_style1.render(msg3,True,color)
    windowSurface.blit(mesg1,[WINDOWWIDTH/4, WINDOWHEIGHT/3])
    windowSurface.blit(mesg2,[WINDOWWIDTH/4+50, WINDOWHEIGHT/3+40])
    windowSurface.blit(mesg3,[WINDOWWIDTH/4+50, WINDOWHEIGHT/3+60])

#function that you can call to display the score to the screen#
def yourScore(score):
    msgScore = score_font.render('Score:' + str(score),True,YELLOW)
    windowSurface.blit(msgScore,[0,0])


#Define the snake class#
snakeSize = 10
class Snake:
    size = 10

    def __init__(self,rect,color,direc):
        self.rect = rect
        self.color = color
        self.direc = direc
#Draws the snake onto the screen#
def ourSnake(snakeSize,snakeList):
    for x in snakeList:
        pygame.draw.rect(windowSurface, WHITE,[x[0],x[1],snakeSize,snakeSize])



#We define the main game loop#
def main():
    
    gameClose = False   #value to check if the player has lost#
    player = Snake(pygame.Rect(WINDOWWIDTH/2,WINDOWHEIGHT/2,snakeSize,snakeSize),WHITE,U) #Build the players initial snake#
    SPEED = 10  #Speed of the snake#
    snakeLength = 1 #Initial length of the snake, to be incremented after contact with food#
    snakeList = []
        
    while True:
        #Creates a seperate loop that occurs after the game has been lost#
        while gameClose == True:
            windowSurface.fill(WHITE) 
            message('GAME OVER!','Press P to play','Press Q to quit',BLUE)
            pygame.display.update()
            #Defines which keys exit and which restarts the game#
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_p:
                        main()
        
        #Check for events#
        for event in pygame.event.get():
            #QUIT event type#
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            #Define wha the arrow and wasd keys do#
            if event.type == KEYDOWN:
                    if event.key == K_LEFT or event.key == K_a:
                        player.direc = L
                    if event.key == K_RIGHT or event.key == K_d:
                        player.direc = R
                    if event.key == K_UP or event.key == K_w:
                        player.direc = U  
                    if event.key == K_DOWN or event.key == K_s:
                        player.direc = D
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

        #Defines how the snake will move around the screen#
        #Also sets up bounds on the snake i.e. the edges of the screen#
        if player.direc == D and player.rect.bottom < WINDOWHEIGHT:
            player.rect.bottom += SPEED
        if player.direc == U and player.rect.top > 0:
            player.rect.top -= SPEED
        if player.direc == R and player.rect.right < WINDOWWIDTH:
            player.rect.right += SPEED
        if player.direc == L and player.rect.left > 0:
            player.rect.left -= SPEED

        #Draw the black background#
        windowSurface.fill(BLACK)

        #Draws foods onto the screen#
        for i in range(len(FOODS)):
            pygame.draw.rect(windowSurface,GREEN,FOODS[i])
            
        #Handles the collision of the sanke with the foods#
        #Removes the foods and appends a new food to the list the increments the snake length#
        for food in FOODS:
            if player.rect.colliderect(food):
                FOODS.remove(food)
                FOODS.append(pygame.Rect(random.randint(FOODSIZE,WINDOWWIDTH-2*FOODSIZE),
        random.randint(FOODSIZE,WINDOWHEIGHT-2*FOODSIZE),FOODSIZE,FOODSIZE))
                snakeLength += 1
        #Ends the game if the snake hits the boundaries of the screen#
        if (player.rect.bottom >= WINDOWHEIGHT or player.rect.top <= 0 or
            player.rect.left <= 0 or player.rect.right >= WINDOWWIDTH):
            gameClose = True

        #Prints the entire length of the snake#
        ####################################
        snakeHead = []
        snakeHead.append(player.rect.left)
        snakeHead.append(player.rect.top)
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLength:
            del snakeList[0]
        ourSnake(snakeSize, snakeList)
        ####################################

        #Causes a game over if the snake runs into itself#
        for x in snakeList[:-1]:
            if x == snakeHead:
                gameClose = True

        #Displays your score to the screen#
        yourScore(snakeLength - 1)
        
        pygame.display.update()
        mainClock.tick(10)
        
    pygame.quit()
    sys.exit()


main()
