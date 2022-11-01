#Made by Brandon Droelle
#ITCS 1950 MCC
#December 202

import pygame
import time
pygame.init()

SCR_WID, SCR_HEI = 1920, 1024

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (250, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
TEAL = (0,128,128)
PURPLE = (100,0,156)
LIGHTGRAY = (55, 55, 55)
DARKGRAY = (155, 155, 155)

#creates and displays menus
class menu():
    def __init__(self, textFont):
        self.textFont = textFont
        
        self.buttons = []
        self.spriteImages = []
        self.spriteRecs = []

    def drawBackground(self, win, color):
        win.fill(color)
        
    def drawTextBox(self, win, x, y, l, w, boxColor, textColor, text):
        titleBox = pygame.Rect(x, y, l, w)
        pygame.draw.rect(win, boxColor, titleBox)
        text = self.textFont.render(text, True, textColor)
        win.blit(text, titleBox)

    def createButton(self, color, x, y, width, height, text=''):
        self.button1 = button(color, x, y, width, height, text)
        self.buttons.append(self.button1)

    def drawButtons(self, win, textColor, outlineColor):
        for x in range(len(self.buttons)):
            self.buttons[x].draw(win, textColor, outlineColor)

    def createSprite(self, imageName, x, y, length, width):
        spriteImage = pygame.image.load(imageName)
        spriteRec = pygame.Rect(x, y, length, width)
        self.spriteImages.append(spriteImage)
        self.spriteRecs.append(spriteRec)

    def drawSprites(self, win):
        for x in range(len(self.spriteImages)):
            win.blit(self.spriteImages[x], self.spriteRecs[x])

#this class creates button objects
class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    #draws button onto screen
    def draw(self,win,textColor,outline=None):
        if outline:
            #creates a secound rectangle 4px larger to make an outline
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
        #draws button
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        #draws button text
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (textColor))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    #Pos is the mouse position or a tuple of (x,y) coordinates
    def isOver(self, pos):
        #tests if mouse x is between button x and button width
        if pos[0] > self.x and pos[0] < self.x + self.width:
            #tests if mouse y is between button y and button height
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

#This class creates car objects
class car():
    def __init__(self, name, sprites, x, y, width, height, upKey, downKey, leftKey, rightKey, basicFont):
        self.name = name
        self.sprites = sprites
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.upKey = upKey
        self.downKey = downKey
        self.leftKey = leftKey
        self.rightKey = rightKey

        self.hitbox = (self.x, self.y, self.width, self.height)
        self.frame = 2
        self.speed = 20
        self.maxSpeed = 20
        self.currentTime = 0.0
        self.bestTime = 0.0
        self.currentLap = 0
        self.timeFont = basicFont

    #displays the lap time
    def time(self, win):
        #display current lap time
        outputString = ("{0}{1:.3f}".format("Time:", self.currentTime))
        lapTimeBlit = self.timeFont.render(outputString, 1, BLACK)
        win.blit(lapTimeBlit, (100, 30))

        #display best lap time
        outputString = ("{0}{1:.3f}".format("Best Lap:", self.bestTime))
        bestTimeBlit = self.timeFont.render(outputString, 1, RED)
        win.blit(bestTimeBlit, (1200, 30))

    def lap(self, win, x, y):
        #displays the players current lap
        outputString = self.name + ("{0}{1}".format(" Lap:", self.currentLap))
        lapBlit = self.timeFont.render(outputString, 1, BLACK)
        win.blit(lapBlit, (x, y))

    def win(self, win):
        #displays a message saying the player won, then waits before going back to main
        winBox = pygame.Rect(600, 500, 500, 100)
        pygame.draw.rect(win, BLACK, winBox)
        outputString = ("{}{}".format(self.name, " WINS!"))
        text = self.timeFont.render(outputString, True, WHITE)
        win.blit(text, (650, 500))
        pygame.display.update()
        time.sleep(3)

    #controls to drive the car
    def driving(self):
        keys = pygame.key.get_pressed()
        if keys[self.upKey]:
            self.y -= self.speed
            self.frame = 0
        elif keys[self.downKey]:
            self.y += self.speed
            self.frame = 1
        elif keys[self.leftKey]:
            self.x -= self.speed
            self.frame = 2
        elif keys[self.rightKey]:
            self.x += self.speed
            self.frame = 3

        #sets screen boundary
        if self.y <= 0:
            self.y = 0
        elif self.y >= SCR_HEI-self.height:
            self.y = SCR_HEI-self.height - 1
        if self.x <= 0:
            self.x = 0
        elif self.x >= SCR_WID-self.width:
            self.x = SCR_WID-self.width - 1
            
    #draws the car
    def draw(self, win):
        spriteRect = pygame.Rect(self.x, self.y, self.width, self.height)
        win.blit(self.sprites[self.frame], spriteRect)
        self.hitbox = (self.x, self.y, self.width, self.height)
        #draws hitbox
        #pygame.draw.rect(win, RED, self.hitbox, 2)

#drawTrackClass
class simpleTrack():
    def __init__(self):
        #loads track image
        self.trackImage = pygame.image.load('customTrack.png')
        self.sprite = pygame.Rect( 0, 0, SCR_WID, SCR_HEI)

    def draw(self, win):
        #draws track
        win.blit(self.trackImage, self.sprite)

#creates and displays the startlight
class startLight():
    def __init__(self):
        self.lightImages = [pygame.image.load('light0.png'),
                    pygame.image.load('light1.png'),
                    pygame.image.load('light2.png'),
                    pygame.image.load('light3.png'),
                    pygame.image.load('light4.png')]
        
        self.beep1 = pygame.mixer.Sound("beep1.wav")
        self.beep2 = pygame.mixer.Sound("beep2.wav")

    #draws lights onto screen
    def draw(self, win):
        self.length = (len(self.lightImages)-1)
        for i in range(self.length):
            spriteRec = pygame.Rect(750, 500, 320, 96)
            win.blit(self.lightImages[i], spriteRec)
            pygame.display.update()
            #cycles through the lights
            if i > 0 or i < 4:
                self.beep1.play()
            elif i == 4:
                self.beep2.play()
            time.sleep(1)
        spriteRec = pygame.Rect(750, 500, 320, 96)
        win.blit(self.lightImages[4], spriteRec)
        pygame.display.update()
        return True

#creates the checkpoints to count laps
class checkPoint():
    def __init__ (self, x, y, length, width, color):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.color = color

        self.hitbox = (self.x, self.y, self.length, self.width)

    def draw(self, win):
        #creates checkpoint
        cp = pygame.Rect(self.x, self.y, self.length, self.width)
        #draws checkpoint
        #pygame.draw.rect(win, self.color, cp)
        #creates checkpoint hit box
        self.hitbox = (self.x, self.y, self.length, self.width)
        #draws hit boxes
        #pygame.draw.rect(win, RED, self.hitbox, 2)

#creates the main menu
def drawMainMenu(win, textFont, choice):

    #Create main menu objects
    mainMenu = menu(textFont)
    mainMenu.createButton(BLACK, 75, 225, 300, 100, 'Time Trial')
    mainMenu.createButton(BLACK, SCR_WID-375, 225, 300, 100, '2 Player')
    mainMenu.createButton(BLACK, 75, SCR_HEI-175, 300, 100, 'How To Play')
    mainMenu.createButton(BLACK, SCR_WID-375, SCR_HEI-175, 300, 100, 'Credits')
    mainMenu.createSprite('checkeredFlag.png', (SCR_WID/2) - 250, (SCR_HEI/2) - 150, 100, 100)

    #run menu loop
    run = True
    while run:
        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            
            if event.type == pygame.QUIT:
                print ("Game exited by user")
                exit()
            mainMenu.drawBackground(win, RED)
            mainMenu.drawTextBox(win, 600, 30,
                               530, 90, BLACK, WHITE, "M1 RACING")     
            mainMenu.drawButtons(win, WHITE, DARKGRAY)
            mainMenu.drawSprites(win)
            
            #checks if mouse gets clicked, and if it over a button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mainMenu.buttons[0].isOver(pos):
                    choice[0] = "carSelectMenu"
                    choice[1] = "timeTrial"
                    run = False
                if mainMenu.buttons[1].isOver(pos):
                    choice[0] = "carSelectMenu"
                    choice[1] = "twoPlayer"
                    run = False
                if mainMenu.buttons[2].isOver(pos):
                    choice[0] = "howToPlayMenu"
                    run = False
                if mainMenu.buttons[3].isOver(pos):
                    choice[0] = "creditsMenu"
                    run = False

    #returns the players choice
    return choice
                        
#creates the car select menu
def drawCarSelectMenu(win, textFont, choice):     

    p1Select = True
    selectText = "P1 Selecting"

    #create menu objects
    carSelectMenu = menu(textFont)
    carSelectMenu.createButton(BLACK, 100, 250, 200, 67, 'Car One')
    carSelectMenu.createButton(BLACK, 100, 500, 200, 67, 'Car Two')
    carSelectMenu.createButton(BLACK, 100, 750, 200, 67, 'Car Three')
    carSelectMenu.createSprite('car_blue_1.png', 500, 250, 100, 100)
    carSelectMenu.createSprite('car_green_2.png', 500, 500, 100, 100)
    carSelectMenu.createSprite('car_red_3.png', 500, 750, 100, 100)
    
    #draw background
    carSelectMenu.drawBackground(win, RED)

    #displays which player is selecting
    carSelectMenu.drawTextBox(win, 1000, 500,
                           600, 100, BLACK, WHITE, selectText)

    #draw title
    carSelectMenu.drawTextBox(win, 440, 25,
                           800, 100, BLACK, WHITE, "Car Selection")

    #run menu loop
    run = True
    while run:
        pygame.display.update()
        
        #displays which player is selecting
        carSelectMenu.drawTextBox(win, 1000, 500,
                           600, 100, BLACK, WHITE, selectText)
        #draw buttons
        carSelectMenu.drawButtons(win, WHITE, DARKGRAY)
        carSelectMenu.drawSprites(win)

        #get car sprites
        blueCarSprites = [pygame.image.load('car_blue_small_1_up.png'),
                               pygame.image.load('car_blue_small_1_down.png'),
                               pygame.image.load('car_blue_small_1_left.png'),
                               pygame.image.load('car_blue_small_1_right.png')]
        greenCarSprites = [pygame.image.load('car_green_small_2_up.png'),
                               pygame.image.load('car_green_small_2_down.png'),
                               pygame.image.load('car_green_small_2_left.png'),
                               pygame.image.load('car_green_small_2_right.png')]
        redCarSprites = [pygame.image.load('car_red_small_3_up.png'),
                               pygame.image.load('car_red_small_3_down.png'),
                               pygame.image.load('car_red_small_3_left.png'),
                               pygame.image.load('car_red_small_3_right.png')]

        #create cars
        blueCar1 = car("P1", blueCarSprites, 910, 875, 40, 70, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, textFont)
        greenCar1 = car("P1", greenCarSprites, 910, 875, 40, 70, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, textFont)
        redCar1 = car("P1", redCarSprites, 910, 875, 40, 70, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, textFont)
        blueCar2 = car("P2", blueCarSprites, 1000, 800, 40, 70, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, textFont)
        greenCar2 = car("P2", greenCarSprites, 1000, 800, 40, 70, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, textFont)
        redCar2 = car("P2", redCarSprites, 1000, 800, 40, 70, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, textFont)

        for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                
                if event.type == pygame.QUIT:
                    print ("Game exited by user")
                    exit()

                #checks if mouse gets clicked, and if it over a button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #selects the car for P1 based on the button slected
                    if choice[1] == "timeTrial":
                        if carSelectMenu.buttons[0].isOver(pos):
                            choice[2] = blueCar1
                            run = False
                        if carSelectMenu.buttons[1].isOver(pos):
                            choice[2] = greenCar1
                            run = False
                        if carSelectMenu.buttons[2].isOver(pos):
                            choice[2] = redCar1
                            run = False
                        choice[3] = blueCar2

                    if choice[1] == "twoPlayer":
                        #selects the car for P1 based on the button slected
                        if p1Select:
                            if carSelectMenu.buttons[0].isOver(pos):
                                choice[2] = blueCar1
                                p1Select = False
                                selectText = "P2 Selecting"
                            if carSelectMenu.buttons[1].isOver(pos):
                                choice[2] = greenCar1
                                p1Select = False
                                selectText = "P2 Selecting"
                            if carSelectMenu.buttons[2].isOver(pos):
                                choice[2] = redCar1
                                p1Select = False
                                selectText = "P2 Selecting"
                        #selects the car for P2 based on the button slected
                        else:
                            if carSelectMenu.buttons[0].isOver(pos):
                                choice[3] = blueCar2
                                run = False
                            if carSelectMenu.buttons[1].isOver(pos):
                                choice[3] = greenCar2
                                run = False
                            if carSelectMenu.buttons[2].isOver(pos):
                                choice[3] = redCar2
                                run = False

    #returns players choice
    choice[0] = "startGame"
    return choice

#creates the how to play menu
def drawHowToPlayMenu(win, textFont, choice):

    howToPlayMenu = menu(textFont)
    
    #draw background
    howToPlayMenu.drawBackground(win, RED)

    #draw title
    howToPlayMenu.drawTextBox(win, 640, 32,
                            640, 96, BLACK, WHITE, "How To Play")

    #draw instructions
    instructionBox = pygame.Rect(128, 256, 1536, 600)
    nl = "\n"
    line1 = ("{}".format("Time Trial: Race against the clock to"))
    line1b = ("{}".format("set the fastest lap."))
    line2 = ("{}".format("Two Player: Race against a friend in"))
    line2b = ("{}".format("a 10 lap race."))
    line3 = ("{}".format("P1 Controls: Arrow Keys"))
    line4 = ("{}".format("P2 Controls: WASD"))
    line5 = ("{}".format("Hit Esc to go back to the main menu"))
    line1Blit = textFont.render(line1, 1, WHITE)
    line1bBlit = textFont.render(line1b, 1, WHITE)
    line2Blit = textFont.render(line2, 1, WHITE)
    line2bBlit = textFont.render(line2b, 1, WHITE)
    line3Blit = textFont.render(line3, 1, WHITE)
    line4Blit = textFont.render(line4, 1, WHITE)
    line5Blit = textFont.render(line5, 1, WHITE)
    
    pygame.draw.rect(win, BLACK, instructionBox)

    win.blit(line1Blit, (128, 256))
    win.blit(line1bBlit, (128, 336))
    win.blit(line2Blit, (128, 416))
    win.blit(line2bBlit, (128, 496))
    win.blit(line3Blit, (128, 576))
    win.blit(line4Blit, (128, 656))
    win.blit(line5Blit, (128, 736))
    
    #run menu loop
    run = True
    while run:
        pygame.display.update()

        for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                
                if event.type == pygame.QUIT:
                    print ("Game exited by user")
                    exit()

                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    choice[0] = "mainMenu"
                    run = False
                        
    #returns players choice               
    return choice

#creates the credits menu
def drawCreditsMenu(win, textFont, choice):

    creditsMenu = menu(textFont)
    
    #draw background
    creditsMenu.drawBackground(win, RED)

    #draw title
    creditsMenu.drawTextBox(win, 640, 32,
                            350, 96, BLACK, WHITE, "Credits")

    #draw instructions
    creditsBox = pygame.Rect(128, 384, 1536, 500)
    line1 = ("{}".format("Made by Brandon Droelle"))
    line2 = ("{}".format("ITCS 1950 Project 3 MCC"))
    line3 = ("{}".format("December 2020"))

    line1Blit = textFont.render(line1, 1, WHITE)
    line2Blit = textFont.render(line2, 1, WHITE)
    line3Blit = textFont.render(line3, 1, WHITE)
    
    pygame.draw.rect(win, BLACK, creditsBox)

    win.blit(line1Blit, (128, 384))
    win.blit(line2Blit, (128, 564))
    win.blit(line3Blit, (128, 724))
    
    #run menu loop
    run = True
    while run:
        pygame.display.update()

        for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                
                if event.type == pygame.QUIT:
                    print ("Game exited by user")
                    exit()

                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    choice[0] = "mainMenu"
                    run = False
                        
    #returns players choice               
    return choice

#sets up and runs time Trial game loop
def game(win, basicFont, choice):

    #create checkpoints
    startLine = checkPoint(850, 780, 3, 150, BLUE)
    sec1 = checkPoint(145, 545, 200, 3, BLUE)
    sec2 = checkPoint(850, 200, 3, 140, BLUE)
    sec3 = checkPoint(1500, 545, 250, 3, BLUE)
    checkpoints = [startLine, sec1, sec2, sec3]

    #initializes the music
    gameMusic = pygame.mixer.music.load("music.wav")

    #inital draw
    track = simpleTrack()
    track.draw(win)
    choice[2].draw(win)
    if choice[1] == "timeTrial":
        choice[2].time(win)
    if choice[1] == "twoPlayer":
        choice[3].draw(win)
        choice[2].lap(win, 100, 30)
        choice[3].lap(win, 1200, 30)
    startLine.draw(win)
    sec1.draw(win)
    sec2.draw(win)
    sec3.draw(win)

    #checkpoint checks
    #p1 checkpoints
    startLineCheck1 = False
    sec1Check1 = False
    sec2Check1 = False
    sec3Check1 = True
    #p2 checkpoints
    startLineCheck2 = False
    sec1Check2 = False
    sec2Check2 = False
    sec3Check2 = True

    #run timeTrial loop
    clock = pygame.time.Clock()
    frameRate = 60
    frameCount = 0
    run = True
    lights = startLight()
    run = lights.draw(win)

    #play music
    pygame.mixer.music.play(-1, 0.0)
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print ("Game exited by user")
                exit()

        #timer
        totalSeconds = frameCount / frameRate
        choice[2].currentTime = totalSeconds

        #for checkPoint in checkpoints:
        #startline
        #checks if car1 y is between the top and bottom of the checkpoint
        if choice[2].y + choice[2].height > checkpoints[0].hitbox[1] and choice[2].y - choice[2].height < checkpoints[0].hitbox[1] + checkpoints[0].hitbox[3]:
            #checks if car1 x is between the top and bottom of the checkpoint
            if choice[2].x + choice[2].width > checkpoints[0].hitbox[0] and choice[2].x - choice[2].width < checkpoints[0].hitbox[0] + checkpoints[0].hitbox[2]:
                #checks if last check point was hit before enabling this one
                if sec3Check1 == True:
                    sec3Check1 = False
                    startLineCheck1 = True
                    choice[2].currentLap = choice[2].currentLap + 1
                    #checks if lap time is greater, starts at lap 2 so time is not stuck at 0
                    if choice[2].currentLap == 2:
                        choice[2].bestTime = choice[2].currentTime
                    if choice[2].currentTime < choice[2].bestTime:
                        choice[2].bestTime = choice[2].currentTime
                frameCount = 0
        #checkpoint 1
        if choice[2].y + choice[2].height > checkpoints[1].hitbox[1] and choice[2].y - choice[2].height < checkpoints[1].hitbox[1] + checkpoints[1].hitbox[3]:
            if choice[2].x + choice[2].width > checkpoints[1].hitbox[0] and choice[2].x - choice[2].width < checkpoints[1].hitbox[0] + checkpoints[1].hitbox[2]:
                if startLineCheck1 == True:
                    startLineCheck1 = False
                    sec1Check1 = True
        #checkpoint 2
        if choice[2].y + choice[2].height > checkpoints[2].hitbox[1] and choice[2].y - choice[2].height < checkpoints[2].hitbox[1] + checkpoints[2].hitbox[3]:
            if choice[2].x + choice[2].width > checkpoints[2].hitbox[0] and choice[2].x - choice[2].width < checkpoints[2].hitbox[0] + checkpoints[2].hitbox[2]:
                if sec1Check1 == True:
                    sec1Check1 = False
                    sec2Check1 = True
        #checkpoint 3
        if choice[2].y + choice[2].height > checkpoints[3].hitbox[1] and choice[2].y - choice[2].height < checkpoints[3].hitbox[1] + checkpoints[3].hitbox[3]:
            if choice[2].x + choice[2].width > checkpoints[3].hitbox[0] and choice[2].x - choice[2].width < checkpoints[3].hitbox[0] + checkpoints[3].hitbox[2]:
                if sec2Check1 == True:
                    sec2Check1 = False
                    sec3Check1 = True

        #checks if car2 is between the top and bottom of the checkpoint
        if choice[3].y + choice[3].height > checkpoints[0].hitbox[1] and choice[3].y - choice[3].height < checkpoints[0].hitbox[1] + checkpoints[0].hitbox[3]:
            #checks if car2 x is between the top and bottom of the checkpoint
            if choice[3].x + choice[3].width > checkpoints[0].hitbox[0] and choice[3].x - choice[3].width < checkpoints[0].hitbox[0] + checkpoints[0].hitbox[2]:
                if sec3Check2 == True:
                    sec3Check2 = False
                    startLineCheck2 = True
                    choice[3].currentLap = choice[3].currentLap + 1
                    #checks if lap time is best, starts at lap 2 so time is not stuck at 0
                    if choice[3].currentLap == 2:
                        choice[3].bestTime = choice[3].currentTime
                    if choice[3].currentTime < choice[3].bestTime:
                        choice[3].bestTime = choice[3].currentTime
                frameCount = 0
        #checkpoint 1
        if choice[3].y + choice[3].height > checkpoints[1].hitbox[1] and choice[3].y - choice[3].height < checkpoints[1].hitbox[1] + checkpoints[1].hitbox[3]:
            if choice[3].x + choice[3].width > checkpoints[1].hitbox[0] and choice[3].x - choice[3].width < checkpoints[1].hitbox[0] + checkpoints[1].hitbox[2]:
                if startLineCheck2 == True:
                    startLineCheck2 = False
                    sec1Check2 = True
        #checkpoint 2
        if choice[3].y + choice[3].height > checkpoints[2].hitbox[1] and choice[3].y - choice[3].height < checkpoints[2].hitbox[1] + checkpoints[2].hitbox[3]:
            if choice[3].x + choice[3].width > checkpoints[2].hitbox[0] and choice[3].x - choice[3].width < checkpoints[2].hitbox[0] + checkpoints[2].hitbox[2]:
                if sec1Check2 == True:
                    sec1Check2 = False
                    sec2Check2 = True
        #checkpoint 3
        if choice[3].y + choice[3].height > checkpoints[3].hitbox[1] and choice[3].y - choice[3].height < checkpoints[3].hitbox[1] + checkpoints[3].hitbox[3]:
            if choice[3].x + choice[3].width > checkpoints[3].hitbox[0] and choice[3].x - choice[3].width < checkpoints[3].hitbox[0] + checkpoints[3].hitbox[2]:
                if sec2Check2 == True:
                    sec2Check2 = False
                    sec3Check2 = True

        #draw sprites
        track.draw(win)
        choice[2].driving()
        choice[2].draw(win)
        if choice[1] == "timeTrial":
            choice[2].time(win)
        #two player methods
        if choice[1] == "twoPlayer":
            choice[2].lap(win, 100, 30)
            choice[3].lap(win, 1200, 30)
            choice[3].driving()
            choice[3].draw(win)
            #checks if laps are greater than 10 to end the race
            if choice[2].currentLap > 10:
                pygame.mixer.music.stop()
                choice[0] = "mainMenu"
                choice[2].win(win)
                run = False
            if choice[3].currentLap > 10:
                pygame.mixer.music.stop()
                choice[0] = "mainMenu"
                choice[3].win(win)
                run = False
        startLine.draw(win)
        sec1.draw(win)
        sec2.draw(win)
        sec3.draw(win)

        frameCount += 1
        pygame.display.update()
        clock.tick(frameRate)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.mixer.music.stop()
            choice[0] = "mainMenu"
            run = False

def main():
    pygame.display.set_caption("M1 Racing")
    win = pygame.display.set_mode((SCR_WID, SCR_HEI))
    basicFont = pygame.font.SysFont(None,128)
    clock = pygame.time.Clock()
    FPS = 60

    #game loop
    choice = ["mainMenu", "gameMode", "P1car", "P2car"]
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print ("Game exited by user")
                exit()

        #this displays the main menu
        if choice[0] == "mainMenu":
            choice = drawMainMenu(win, basicFont, choice)

        #this displays the car selection menu
        if choice[0] == "carSelectMenu":
            choice = drawCarSelectMenu(win, basicFont, choice)

        #This displays the how to play menu
        if choice[0] == "howToPlayMenu":
            choice = drawHowToPlayMenu(win, basicFont, choice)

        #This displays the credits menu
        if choice[0] == "creditsMenu":
            choice = drawCreditsMenu(win, basicFont, choice)

        if choice[0] == "startGame":
            game(win, basicFont, choice)

    pygame.display.update()
    clock.tick(FPS)

main()
