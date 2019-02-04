"""
Hello, I'm Kalvin Situmeang and this is my snake game
To play this game you'd need to install pygame using this link, https://www.pygame.org/download.shtml
I learned this code from https://www.youtube.com/watch?v=K5F-aGDIYaM&list=PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq
"""
import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blueish = (3,51,95) #1 Changed the backgroud color for intro and end game screen using w3schools.com
green = (28,239,42)

display_width = 800
display_height = 600 
        
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither')

clock = pygame.time.Clock()

block_size = 10

FPS = 30

direction = "right"

smallfont = pygame.font.SysFont("vintage", 25)
medfont = pygame.font.SysFont("vintage", 40)    #2. Changed the font using tkinterbook.com
largefont = pygame.font.SysFont("vintage", 80)
#font = pygame.font.SysFont(None, 25)

def pause():

    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                    
            gameDisplay.fill(red)
            message_to_screen("Paused",red, -100, size = "small")
            message_to_screen("Press ESC to continue or Q to Quit.", white, 25)
            pygame.display.update()
            clock.tick(5)

def score(score):
    text = smallfont.render("Score: "+ str(score), True, red)
    gameDisplay.blit(text, [0,0])


def randApple(): 
    randAppleX = round(random.randrange(0, display_width - block_size))
    randAppleY = round(random.randrange(0, display_height - block_size))

    return randAppleX, randAppleY


def game_intro():

    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: #3. Changed the start key from C to Space
                    intro = False 
                if event.key == pygame.K_q:
                    quit()
                    
        gameDisplay.fill(blueish)
        message_to_screen("Welcome to Slither",green,-100,"large")
        message_to_screen("The Objective of the game is to eat APPLES!",white,-30,)
        message_to_screen("The more APPLES you eat, the larger you get.",white,10,)
        message_to_screen("If you run into yourself or the walls, you die!! RIP OWO!",white,50,)
        message_to_screen("Press Space to play, P to pause, and Q to quit.",red,180,)


        pygame.display.update()
        clock.tick(15)  #fps                    

def snake(block_size,snakeList):  
	for segment in snakeList:
		lead_x, lead_y = segment
		pygame.draw.rect(gameDisplay, green, [lead_x, lead_y, block_size, block_size])

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color) 
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
        
    return textSurface, textSurface.get_rect()

def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (display_width /2), (display_height /2) + y_displace 
    gameDisplay.blit(textSurf, textRect)

def gameLoop():
    global direction
    direction = 'right'
    
    gameExit = False
    gameOver = False
  
    lead_x = display_width/2
    lead_y = display_height/2
  
    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1
    
    apple_x = round(random.randrange(0, display_width - block_size)/10.0)*10.0
    apple_y = round(random.randrange(0, display_height - block_size)/10.0)*10.0
  
    while not gameExit:
    
        while gameOver == True:
          gameDisplay.fill(blueish)
          message_to_screen("Game over!",red,y_displace=-30,size = "large")
          message_to_screen("Press Q to exit or Space to play again!",white,50,size = "medium") 
          message_to_screen("GOODLUCK! (OR LATER LOSER)", green,100, size = "small")  
          pygame.display.update()
      
          for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q: 
                        gameExit = True
                        gameOver = False
                        quit()
                    if event.key == pygame.K_c:
                        intro = False
                        gameLoop()
                        
                        
          
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            gameExit = True
            
        
          if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:    #4. Added A key using https://www.pygame.org/docs/ref/key.html.
                    direction = "left"
                    lead_x_change = -block_size 
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:  #5. Added D key using https://www.pygame.org/docs/ref/key.html.
                    direction = "right"
                    lead_x_change = block_size 
                    lead_y_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:    #6. Added W key using https://www.pygame.org/docs/ref/key.html.            
                    direction = "up" 
                    lead_x_change = 0
                    lead_y_change = -block_size
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:    #7. Added S key using https://www.pygame.org/docs/ref/key.html. 
                    direction = "down"
                    lead_x_change = 0
                    lead_y_change = block_size
                elif event.key == pygame.K_p:
                    pause()
          
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
    
        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(black)
        pygame.draw.rect(gameDisplay, red, [apple_x, apple_y, block_size, block_size])
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len (snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(block_size, snakeList)
        score(snakeLength-1) 
        pygame.display.update()
                    

        
        if lead_x == apple_x and lead_y == apple_y:
                apple_x = round(random.randrange(0, display_width - block_size)/10.0)*10.0
                apple_y = round(random.randrange(0, display_height - block_size)/10.0)*10.0
                snakeLength +=1
            
        clock.tick(FPS)

    running = True
    while running:
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
        
    pygame.quit()
    quit()
game_intro()
gameLoop()
