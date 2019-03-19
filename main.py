import random
from time import time
from Classes.Block import Block
from Classes.ImageBackGround import *
from Classes.myCheckbox import *
from io import BytesIO
from base64 import b64decode
pygame.init()
main = Tk()
seedWindow = Toplevel()
controlsWindow = Toplevel()
image64 = "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAIAAAD8GO2jAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAYdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjEuNWRHWFIAAABOSURBVEhL7ZYhDgAgDAOreQb//yOQlARXtU6QXs7M9OzQwQCmwTN7OYeDN9sXWEWSBIQkASFJQEgSEJIEhCQBIUlASL4M1NIYsD+/RoANprRM50WVCWoAAAAASUVORK5CYII="
logo = BytesIO(b64decode(image64))
logo = pygame.image.load(logo)
pygame.display.set_caption("Cube Evasion")
pygame.display.set_icon(logo)
main.title("Cube Evasion: Settings")
seedWindow.title("Cube Evasion: Seed")
controlsWindow.title("Cube Evasion: Controls")

configs = { "up":pygame.K_UP, "down":pygame.K_DOWN,"left":pygame.K_LEFT,"right":pygame.K_RIGHT,"player2":pygame.K_p,"pause":pygame.K_r,"settings":pygame.K_BACKQUOTE,"2up":pygame.K_w,
            "2down":pygame.K_s,"2left":pygame.K_a,"2right":pygame.K_d}
configsKeys = ["up","down","left","right","player2","pause","settings","2up","2down","2left","2right"]
def confirmSeed():
    global eSeed
    global r
    global isRandSeed
    print(randseedCheck.getVar())
    isRandSeed =not( randseedCheck.getVar())
    r = int(eSeed.get())
    random.seed(int(eSeed.get()))
    seedWindow.withdraw()
def confirmControls():
    global listEntries
    global configs
    global configsKeys
    l = []
    for i in range(0,len(listEntries)):
        j = listEntries[i].get().lower()
        if j is not "":
            if j == "backquote":
                l.append(pygame.K_BACKQUOTE)
            elif j == "up":
                l.append(pygame.K_UP)
            elif j == "down":
                l.append(pygame.K_DOWN)
            elif j == "left":
                l.append(pygame.K_LEFT)
            elif j == "right":
                l.append(pygame.K_RIGHT)
            else:
                l.append(ord(j))
    for i in range(0,len(l)):
        pass
    print(l[0])
    configs["up"] = l[0]
    configs["down"] = l[1]
    configs["left"] = l[2]
    configs["right"] = l[3]
    configs["2up"] = l[4]
    configs["2down"] = l[5]
    configs["2left"] = l[6]
    configs["2right"] = l[7]
    configs["player2"] = l[8]
    configs["pause"] = l[9]
    configs["settings"] = l[10]
    controlsWindow.withdraw()
def confirmSettings():
    main.withdraw()
    main.quit()
    restart(r)
isRandSeed = True
# Setting main:
bFinishSettings = Button(main,text = "Finish", command = confirmSettings)
bToSeed = Button(main,text = "open seed window", command = seedWindow.deiconify)
bToControls = Button(main, text = "Open controls",command = controlsWindow.deiconify)
bToSeed.pack()
bToControls.pack()
bFinishSettings.pack()
# Setting controls window:
spacer1 = Label(controlsWindow)
spacer2 = Label(controlsWindow)
bConfirmControls = Button(controlsWindow,text = "Confirm",command = confirmControls)
eUp = Entry(controlsWindow)
eUp.insert(0,"up")
eDown = Entry(controlsWindow)
eDown.insert(0,"down")
eLeft = Entry(controlsWindow)
eLeft.insert(0,"left")
eRight = Entry(controlsWindow)
eRight.insert(0,"right")
e2Up = Entry(controlsWindow)
e2Up.insert(0,"w")
e2Down = Entry(controlsWindow)
e2Down.insert(0,"s")
e2Left = Entry(controlsWindow)
e2Left.insert(0,"a")
e2Right = Entry(controlsWindow)
e2Right.insert(0,"f")
eChangeP2 = Entry(controlsWindow)
eChangeP2.insert(0,"p")
ePause = Entry(controlsWindow)
ePause.insert(0,"r")
eSettings = Entry(controlsWindow)
eSettings.insert(0,"backquote")
listEntries = [eUp,eDown,eLeft,eRight,e2Up,e2Down,e2Left,e2Right,eChangeP2,ePause,eSettings]
lPlayer = Label(controlsWindow,text = "Player1: ")
lPlayer2 = Label(controlsWindow,text = "Player2: ")
lUp = Label(controlsWindow,text = "Up: ")
lDown = Label(controlsWindow,text = "Down: ")
lLeft = Label(controlsWindow,text = "Left: ")
lRight = Label(controlsWindow,text = "Right: ")
l2Up = Label(controlsWindow,text = "Up: ")
l2Down = Label(controlsWindow,text = "Down: ")
l2Left = Label(controlsWindow,text = "Left: ")
l2Right = Label(controlsWindow,text = "Right: ")
lChangeP2 = Label(controlsWindow,text = "Change players: ")
lPause = Label(controlsWindow,text = "Pause: ")
lSettings = Label(controlsWindow,text = "Settings: ")
lPlayer.grid(row = 0,column = 0)
lUp.grid(row = 1,column = 0)
lDown.grid(row = 2,column = 0)
lLeft.grid(row = 3,column = 0)
lRight.grid(row = 4,column = 0)
spacer1.grid(row = 5,column = 0)
lChangeP2.grid(row = 6,column = 0)
lPause.grid(row = 7,column = 0)
eUp.grid(row = 1,column = 1)
eDown.grid(row = 2,column = 1)
eLeft.grid(row = 3,column = 1)
eRight.grid(row = 4,column = 1)
eChangeP2.grid(row = 6,column = 1)
ePause.grid(row = 7,column = 1)
lPlayer2.grid(row = 0,column = 2)
l2Up.grid(row = 1,column = 2)
l2Down.grid(row = 2,column = 2)
l2Left.grid(row = 3,column = 2)
l2Right.grid(row = 4,column = 2)
spacer1.grid(row = 5,column = 0)
lSettings.grid(row = 6,column = 2)
e2Up.grid(row = 1,column = 3)
e2Down.grid(row = 2,column = 3)
e2Left.grid(row = 3,column = 3)
e2Right.grid(row = 4,column = 3)
eSettings.grid(row = 6,column = 3)
bConfirmControls.grid(column = 0,columnspan = 4,row = 8)
#Seed window:
label = Label(seedWindow,text = "Enter seed:")
eSeed = Entry(seedWindow)
randseedCheck = mycheckbox(seedWindow,"Randomize seed",True,False)
bSeed = Button(seedWindow,text = "confirm",command = confirmSeed)
label.pack()
eSeed.pack()
randseedCheck.pack()
bSeed.pack()
main.withdraw()
isDebug = True
transition = pygame.display.set_mode((400,400))
try:
    TransitionImage = pygame.image.load("TransitionLogo.png")
except:
    print("NO LOGO!")
else:
    TransitionImage = ImageBackground(TransitionImage,(0,0))
    TransitionImage.image = pygame.transform.scale(TransitionImage.image,(400,400))
    transition.fill([255, 255, 255])
    transition.blit(TransitionImage.image, TransitionImage.rect)
    pygame.display.flip()
    tt = time()
    while time() - tt < 3:
        pygame.event.get()

# Define some colors
# An idea for the randomizer, do it in batches and lkimit the number of blocks.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0,0,153)
GREEN = (0,255,0)
PLAYER_SPEED = 4
pPlayer_SPEED = 4
SCROLL_SPEED = 4
pSCROLL_SPEED = 4
r = random.randint(0,1000)
random.seed(r)

def makeCol(x,amountCols):
    newBlocks = []
    blockPlacements = []
    for j in range(0,amountCols):
        if j%2 == 0:
            ry = random.randint(0,10)
            rx = random.randint(x,x+amountCols)
            if ry != 0:
                blockPlacements.append((rx,ry))
    for i in range(0,len(blockPlacements)):
        newBlocks.append(Block(BLUE,screen,blockPlacements[i][0]*32,blockPlacements[i][1]*32))
    return newBlocks


def pause(screen):
    global SCROLL_SPEED
    global PLAYER_SPEED
    global pSCROLL_SPEED
    global pPlayer_SPEED
    global isPause
    global pauseTime
    pauseTime = time()
    isPause = not isPause
    if isPause:
        pSCROLL_SPEED = SCROLL_SPEED
        pPlayer_SPEED = PLAYER_SPEED
        PLAYER_SPEED = 0
        SCROLL_SPEED = 0
    if not isPause:
        PLAYER_SPEED = pPlayer_SPEED
        SCROLL_SPEED = pSCROLL_SPEED
        screen.fill(BLACK)
        downBlue.draw(screen)


def restart(seed = None):
    global player
    global player2
    global blocks
    global running
    global isDead
    global start
    global counter
    global r
    global SCROLL_SPEED
    global players
    global score
    global isPause
    global screen
    global isRandSeed
    if isPause:
        pause(screen)
    score = 0
    SCROLL_SPEED = 4
    if seed is not None:
        r = seed
    elif isRandSeed:
        r = random.randint(0,1000)
    random.seed(r)
    counter = 0
    start = time()
    screen = pygame.display.set_mode((800, TOTAL_H))
    screen.fill(BLACK)
    blocks = []
    players = []
    player = Block(RED, screen, 0, 32, 28, 28, True,players)
    if isPlayerTwo:
        player2 = Block(GREEN, screen, 0, 32, 28, 28, True,players)
        players.append(player2)
    players.append(player)
    running = True
    isDead = False
    upBlue.draw(screen)
    downBlue.draw(screen)

pauseTime = 0
failFont = pygame.font.SysFont('Arial', 52)
tFailed = failFont.render('GAME OVER!', True, (255, 0, 0))
TOTAL_H = 384
TOTAL_W = 2048
screen = pygame.display.set_mode((800, TOTAL_H))
players = []
player = Block(RED, screen, 0,32,28,28,True,players)
player2 = Block(GREEN,screen,0,32,28,28,True,players)
players.append(player)
isPlayerTwo = False
isPause = False
running = True
isDead = False
start = time()
time_since_change = 0
blocks = []
upBlue = Block(BLUE,screen, 0,0,TOTAL_W)
downBlue = Block(BLUE,screen, 0,TOTAL_H - 32,TOTAL_W)
upBlue.draw(screen)
downBlue.draw(screen)
timefont = pygame.font.SysFont('Consolas', 13)
tPause = failFont.render("PAUSE",True,RED)
counter = 0
score = 0


# Run loop:
while running:
    # Blitting "pause" if paused
    if isPause:
        screen.blit(tPause,(150,200))
        pygame.display.flip()
    # Getting pressed keys:
    keys = pygame.key.get_pressed()
    player.draw(screen)
    # Accelerating screen:
    if not isPause:
        SCROLL_SPEED += 0.001
    pygame.time.delay(16)
    if not isDead:
        # Making new blocks:
        if counter % 64 == 0:
            blocks.extend(makeCol(33,8))
        # Drawing upper borders:
        upBlue.draw(screen)
        # Changing text of Score and Time and blitting them:
        tScore = timefont.render("Score: " + str(round(score,0)), True, RED)
        tTime = timefont.render("seed: "+str(r) + ", Scroll Speed: "+ str(round(SCROLL_SPEED,3)) , True, (255, 0, 0))
        screen.blit(tTime,(10,10))
        screen.blit(tScore,(600,10))
        # Updating position of Blocks:
        for i in blocks:
            i.update(-SCROLL_SPEED,0)
            if i.x == -32:
                blocks.remove(i)
            # Checking for collisions
            for j in players:
                if (i.shape.colliderect(j.shape)  or upBlue.shape.colliderect(j.shape) or downBlue.shape.colliderect(j.shape)):
                    screen.blit(tFailed,(200,150))
                    isDead = True
        pygame.display.flip()
        # Opening seed if needed
        if keys[configs["settings"]]:
            isPause = True
            screen.blit(tPause,(200,150))
            pygame.display.flip()
            print("Opening main")
            main.deiconify()
            seedWindow.withdraw()
            controlsWindow.withdraw()
            main.mainloop()
        # Checking for pause and movement:
        if keys[configs["pause"]] and time()-pauseTime > 1:
            pause(screen)
        if keys[configs["up"]]:
            player.update(0,-PLAYER_SPEED)
        if keys[configs["down"]]:
            player.update(0,PLAYER_SPEED)
        if keys[configs["right"]]:
            player.update(PLAYER_SPEED,0)
        if keys[configs["left"]]:
            player.update(-PLAYER_SPEED,0)
        # Adding/ Removing Second player:
        if pygame.key.get_pressed()[configs["player2"]] and time() - time_since_change > 1 and (not isPause):
            time_since_change = time()
            if isPlayerTwo:
                isPlayerTwo = False
                # players.remove(player2)
                player2.kill()
            else:
                player2.x = 0
                player2.y = 32
                player2.updateShape()
                player2.draw(screen)
                isPlayerTwo = True
                players.append(player2)
        if isPlayerTwo and not isDead:
            # Checking for p2 movement:
            player2.draw(screen)
            if keys[configs["2up"]]:
                player2.update(0, -PLAYER_SPEED)
            if keys[configs["2down"]]:
                player2.update(0, PLAYER_SPEED)
            if keys[configs["2right"]]:
                player2.update(PLAYER_SPEED, 0)
            if keys[configs["2left"]]:
                player2.update(-PLAYER_SPEED, 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_SPACE] and not isPause:
        restart()
    if not isDead and not isPause:
        counter += 1
        score += len(blocks)

