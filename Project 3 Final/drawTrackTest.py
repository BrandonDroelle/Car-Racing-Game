import pygame
pygame.init()

SCR_WID, SCR_HEI = 1920, 1024

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
TEAL = (0,128,128)
PURPLE = (100,0,156)
LIGHTGRAY = (55, 55, 55)
DARKGRAY = (155, 155, 155)

class car():
    def __init__(self, sprites, x, y, width, height, upKey, downKey, leftKey, rightKey, basicFont):
        self.sprites = sprites
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.upKey = upKey
        self.downKey = downKey
        self.leftKey = leftKey
        self.rightKey = rightKey

        self.speed = 20
        self.timeFont = basicFont

    #controls to drive the car
    def driving(self):
        keys = pygame.key.get_pressed()
        if keys[self.upKey]:
            self.y -= self.speed
            print("pressing up key")
        elif keys[self.downKey]:
            self.y += self.speed
            print("pressing down key")
        elif keys[self.leftKey]:
            self.x -= self.speed
            print("pressing left key")
        elif keys[self.rightKey]:
            self.x += self.speed
            print("pressing right key")
            
    #draws the car
    def draw(self, win):
        spriteRect = pygame.Rect(self.x, self.y, self.width, self.height)
        win.blit(self.sprites[2], spriteRect)

class track():
    def __init__(self, name):
        self.name = name
        
    def drawTrack(self, win):
        #print track
        #start line outside
        self.drawTile(win, 'startline1.jpg', 7, 1)

        #start line inside
        self.drawTile(win, 'startline2.jpg', 7, 2)

        #straight track outside
        self.drawTile(win, 'trackStraight1.jpg', 8, 1)
        self.drawTile(win, 'trackStraight1.jpg', 9, 1)
        self.drawTile(win, 'trackStraight1.jpg', 10, 1)
        self.drawTile(win, 'trackStraight1.jpg', 11, 1)
        self.drawTile(win, 'trackStraight1.jpg', 12, 1)
        self.drawTile(win, 'track4.png', 13, 2)
        self.drawTile(win, 'track4.png', 13, 3)
        self.drawTile(win, 'track4.png', 13, 4)
        self.drawTile(win, 'track4.png', 13, 5)
        self.drawTile(win, 'trackStraight2.jpg', 12, 6)
        self.drawTile(win, 'trackStraight2.jpg', 11, 6)
        self.drawTile(win, 'trackStraight2.jpg', 10, 6)
        self.drawTile(win, 'trackStraight2.jpg', 9, 6)
        self.drawTile(win, 'trackStraight2.jpg', 8, 6)
        self.drawTile(win, 'trackStraight2.jpg', 7, 6)
        self.drawTile(win, 'trackStraight2.jpg', 6, 6)
        self.drawTile(win, 'trackStraight2.jpg', 5, 6)
        self.drawTile(win, 'trackStraight2.jpg', 4, 6)
        self.drawTile(win, 'trackStraight2.jpg', 3, 6)
        self.drawTile(win, 'trackStraight2.jpg', 2, 6)
        self.drawTile(win, 'track3.png', 1, 5)
        self.drawTile(win, 'track3.png', 1, 4)
        self.drawTile(win, 'track3.png', 1, 3)
        self.drawTile(win, 'track3.png', 1, 2)
        self.drawTile(win, 'trackStraight1.jpg', 2, 1)
        self.drawTile(win, 'trackStraight1.jpg', 3, 1)
        self.drawTile(win, 'trackStraight1.jpg', 4, 1)
        self.drawTile(win, 'trackStraight1.jpg', 5, 1)
        self.drawTile(win, 'trackStraight1.jpg', 6, 1)

        #straight track inside
        self.drawTile(win, 'trackStraight2.jpg', 8, 2)
        self.drawTile(win, 'trackStraight2.jpg', 9, 2)
        self.drawTile(win, 'trackStraight2.jpg', 10, 2)
        self.drawTile(win, 'trackStraight2.jpg', 11, 2)
        self.drawTile(win, 'track3.png', 12, 3)
        self.drawTile(win, 'track3.png', 12, 4)
        self.drawTile(win, 'trackStraight1.jpg', 11, 5)
        self.drawTile(win, 'trackStraight1.jpg', 10, 5)
        self.drawTile(win, 'trackStraight1.jpg', 9, 5)
        self.drawTile(win, 'trackStraight1.jpg', 8, 5)
        self.drawTile(win, 'trackStraight1.jpg', 7, 5)
        self.drawTile(win, 'trackStraight1.jpg', 6, 5)
        self.drawTile(win, 'trackStraight1.jpg', 5, 5)
        self.drawTile(win, 'trackStraight1.jpg', 4, 5)
        self.drawTile(win, 'trackStraight1.jpg', 3, 5)
        self.drawTile(win, 'track4.png', 2, 4)
        self.drawTile(win, 'track4.png', 2, 3)
        self.drawTile(win, 'trackStraight2.jpg', 3, 2)
        self.drawTile(win, 'trackStraight2.jpg', 4, 2)
        self.drawTile(win, 'trackStraight2.jpg', 5, 2)
        self.drawTile(win, 'trackStraight2.jpg', 6, 2)

        #curve inside
        self.drawTile(win, 'curveInsideTopRight.jpg', 12, 2)
        self.drawTile(win, 'track5.png', 12, 5)
        self.drawTile(win, 'track6.png', 2, 5)
        self.drawTile(win, 'curveInsideTopLeft.jpg', 2, 2)

        #curve outside
        self.drawTile(win, 'curveOutsideBotLeft.jpg', 13, 1)
        self.drawTile(win, 'track8.png', 13, 6)
        self.drawTile(win, 'track7.png', 1, 6)
        self.drawTile(win, 'curveOutsideBotRight.jpg', 1, 1)

    def drawBackground(self, win):
        #print grass tile on each coordinate to make a background
        for x in range(15):
            for y in range(8):
                self.drawTile(win, 'track0.png', x, y)
        
    def drawTile(self, win, imageName, x, y):
        #tile size
        tileLen = 128
        tileWid = 128
        #tile coordinates
        xCords = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        yCords = [0,0,0,0,0,0,0,0]

        for i in range(15):
            xCords[i] = (SCR_WID - (128 * (i + 1)))

        for i in range(8):
            yCords[i] = (SCR_HEI - (128 * (i + 1)))
        
        #draw tile
        tileImage = pygame.image.load(imageName)
        tileRect = pygame.Rect((xCords[x]), (yCords[y]), tileLen, tileWid)
        win.blit(tileImage, tileRect)

class simpleTrackHardCoded():
    def __init__(self):
        self.trackImage = pygame.image.load('customTrack.png')
        self.sprite = pygame.Rect( 0, 0, SCR_WID, SCR_HEI)

    def draw(self, win):
        win.blit(self.trackImage, self.sprite)
        
class simpleTrack():
    def __init__ (self, imageName):
        self.imageName = imageName

    def draw(self, win):
        trackImage = pygame.image.load(self.imageName)
        sprite = pygame.Rect( 0, 0, SCR_WID, SCR_HEI)
        win.blit(trackImage, sprite)

def drawSimpleTrack(win):
    #print background image
    trackImage = pygame.image.load('customTrack.png')
    sprite = pygame.Rect( 0, 0, SCR_WID, SCR_HEI)
    win.blit(trackImage, sprite)
    #win.fill(GREEN)

def main():
    win = pygame.display.set_mode((SCR_WID, SCR_HEI))
    basicFont = pygame.font.SysFont(None,128)

    #get car sprites
    smallBlueCarSprites = [pygame.image.load('car_blue_small_1_up.png'),
                           pygame.image.load('car_blue_small_1_down.png'),
                           pygame.image.load('car_blue_small_1_left.png'),
                           pygame.image.load('car_blue_small_1_right.png')]

    #create players car
    player1 = car(smallBlueCarSprites, 500, 500, 40, 70, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, basicFont)

    #create complex track object
    trackObject = track("track1")

    #draws image from class method with a hard coded image
    simpleTrack2 = simpleTrackHardCoded()

    #create simple track object
    simpleTrackObject = simpleTrack('customTrack.png')
    
    #create track image
    trackImage = pygame.image.load('customTrack.png')
    sprite = pygame.Rect( 0, 0, SCR_WID, SCR_HEI)
    
    clock = pygame.time.Clock()
    FPS = 60
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print ("Game exited by user")
                exit()
                
        #draws images from class methods
        #trackObject.drawBackground(win)
        #trackObject.drawTrack(win)

        #draws image from class method with a hard coded image
        #simpleTrack2.draw(win)

        #draws image from class method
        #simpleTrackObject.draw(win)
                
        #draws image from a function
        #drawSimpleTrack(win)
                
        #draws image in main
        win.blit(trackImage, sprite)
        
        player1.driving()
        player1.draw(win)
        pygame.display.update()
        clock.tick(FPS)

main()

