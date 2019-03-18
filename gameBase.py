import pygame, sys, math, time, random, time, webbrowser
from Ball import *
from Racket import *
from Score import *
from LevelLoad import *
from Block import *
from BlackBlock import *
from Button import *

pygame.init()

dbgTime = False

balls = []

clock = pygame.time.Clock()

width = 1200
height = 950
size = width, height


screen = pygame.display.set_mode(size)

start = time.clock()


mode = "start"

while True: 
    
    startimages = [ pygame.image.load ("Screens/backroundStartScreen.png"),
                    pygame.image.load ("Screens/backroundStartScreen2.png"),
                    pygame.image.load ("Screens/backroundStartScreen3.png")]
    currentImage = 0
    lastImage = len(startimages)-1
    startimage = startimages [currentImage]
    startrect = startimage.get_rect()
    
    aniTimer = 0
    aniTimerMax = 60/7
    
    menuimages = [ pygame.image.load ("Screens/MainMenu.png"),
                    pygame.image.load ("Screens/MainMenu2.png"),
                    pygame.image.load ("Screens/MainMenu3.png")]
    menuimage = menuimages[currentImage]
    menurect = menuimage.get_rect()
    lastImage = len(menuimages)-1
    
    easyButton = Button("easy", [width/2, 420])
    mediumButton = Button("medium", [width/2, 530])
    hardButton = Button("hard", [width/2, 640])
    quitButton = Button("quit", [1126, 708])
    noButton = Button("no", [900, 650])
    yesButton = Button("yes", [300, 650])
    quitwinButton = Button("wquit", [900, 625])
    menuButton = Button("menu", [300, 625])
    gButton = Button("g", [530, 265])
    pewButton = Button("pew", [1170, 205])
    
    ###########START####
    
    while mode == "start":
        for event in pygame.event.get():
            #print event.type
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mode = "menu"
        
        if aniTimer < aniTimerMax:
            aniTimer += 1
        else:
            aniTimer = 0
            if currentImage < lastImage:
                currentImage += 1
            else:
                currentImage = 0
            startimage = startimages [currentImage]
        
        screen.blit(startimage, startrect)
        pygame.display.flip()
        clock.tick(60)
 
 ###########MENU#########
 
    
    while mode == "menu":
        for event in pygame.event.get():
            #print event.type
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                if event.buttons[0] == 0:
                    easyButton.checkHover(event.pos)
                    mediumButton.checkHover(event.pos)
                    hardButton.checkHover(event.pos)
                    quitButton.checkHover(event.pos)
                    gButton.checkHover(event.pos)
                    pewButton.checkHover(event.pos)
                else:
                    easyButton.checkClick(event.pos)
                    mediumButton.checkClick(event.pos)
                    hardButton.checkClick(event.pos)
                    quitButton.checkClick(event.pos)
                    gButton.checkClick(event.pos)
                    pewButton.checkClick(event.pos)
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                print event.button
                if event.button == 1:
                    easyButton.checkClick(event.pos)
                    mediumButton.checkClick(event.pos)
                    hardButton.checkClick(event.pos)
                    quitButton.checkClick(event.pos)
                    gButton.checkClick(event.pos)
                    pewButton.checkClick(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                if easyButton.collidePt(event.pos):
                    level = loadLevel ("Levels/1.lvl")
                    bgimage = pygame.image.load("Screens/backroundEasy.png")
                    bgrect = bgimage.get_rect()
                    mode = "countdown"
                if mediumButton.collidePt(event.pos):
                    level = loadLevel ("Levels/2.lvl")
                    bgimage = pygame.image.load("Screens/backround1.png")
                    bgrect = bgimage.get_rect()
                    mode = "countdown"
                if hardButton.collidePt(event.pos):
                    level = loadLevel ("Levels/3.lvl")
                    bgimage = pygame.image.load("Screens/backround1.png")
                    bgrect = bgimage.get_rect()
                    mode = "countdown"
                    
                if quitButton.collidePt(event.pos):
                    mode = "ays"
                    
                if gButton.collidePt(event.pos):
                    bgimage = pygame.image.load("Screens/easterEgg.png")
                    bgrect = bgimage.get_rect()
                    mode = "g"
                    
                if pewButton.collidePt(event.pos):
                    bgimage = pygame.image.load("Screens/easterEgg.png")
                    bgrect = bgimage.get_rect()
                    mode = "pew"
                    
        if aniTimer < aniTimerMax:
            aniTimer += 1
        else:
            aniTimer = 0
            if currentImage < lastImage:
                currentImage += 1
            else:
                currentImage = 0
            menuimage = menuimages [currentImage]
        
        screen.blit(menuimage, menurect)
        screen.blit(easyButton.image, easyButton.rect)
        screen.blit(mediumButton.image, mediumButton.rect)
        screen.blit(hardButton.image, hardButton.rect)
        screen.blit(quitButton.image, quitButton.rect)
        screen.blit(gButton.image, gButton.rect)
        screen.blit(pewButton.image, pewButton.rect)
        
        
        pygame.display.flip()
        clock.tick(60)
    
    
    
    balls = []
    
    speed = [5,5]
    pos = [random.randint(300,1000),300]
    balls += [Ball("Ball/ball.png", speed, pos)]

    speed = [5,-5]
    pos = [random.randint(300,1000),650]
    balls += [Ball("Ball/ball.png", speed, pos)]


    rkt= racket("Racket/racket.png", 15, [width/2, height-10])
    rktScore = Score(0, [50, height-25])
    rkt2= racket("Racket/racket.png", 15, [width/2, 10])
    rkt2Score = Score(0, [width-50, 25])

#######################COUNTDOWN#####

    countimages = [ pygame.image.load ("Screens/Countdown1.png"),
                    pygame.image.load ("Screens/Countdown2.png"),
                    pygame.image.load ("Screens/Countdown3.png")]
    countimage = countimages[currentImage]
    countrect = countimage.get_rect()
    lastImage = len(countimages)-1
    
    currentImageNum = 0
    
    numimages = [ pygame.image.load ("Screens/3.png"),
                  pygame.image.load ("Screens/2.png"),
                  pygame.image.load ("Screens/1.png"),
                  pygame.image.load ("Screens/1.png")]
    numimage = numimages[currentImageNum]
    numrect = numimage.get_rect(center = [width/2, height/2])
    lastImageNum = len(numimages)-1
    
    aniTimerNum = 0
    aniTimerNumMax = 60/1

    while mode == "countdown":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        
        
        if aniTimer < aniTimerMax:
            aniTimer += 1
        else:
            aniTimer = 0
            if currentImage < lastImage:
                currentImage += 1
            else:
                currentImage = 0
            countimage = countimages [currentImage]
            
        if aniTimerNum < aniTimerNumMax:
            aniTimerNum += 1
        else:
            aniTimerNum = 0
            if currentImageNum < lastImageNum:
                currentImageNum += 1
            else:
                currentImage = 0
            numimage = numimages [currentImageNum]
            
        if numimage == numimages[3]:
            mode = "game"
            
            
        
        
        screen.blit(countimage, countrect)
        screen.blit(numimage, numrect)
        pygame.display.flip()
        clock.tick(60)






    ###########GAME######
    
    
    while mode == "game":
        if dbgTime: print "\nLoopTine:", time.clock() - start
        start = time.clock()
        for event in pygame.event.get():
            #print event.type
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    paused = True
                    while paused:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                 sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_t:
                                    paused = False
                                    
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_LEFT:
                    rkt.go("left")
                if event.key == pygame.K_a:
                    rkt2.go("left")
                if event.key == pygame.K_RIGHT:                 
                    rkt.go("right")
                if event.key == pygame.K_d:
                    rkt2.go("right") 

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    rkt.stop("left")
                if event.key == pygame.K_a:
                    rkt2.stop("left")
                if event.key == pygame.K_RIGHT:                 
                    rkt.stop("right")
                if event.key == pygame.K_d:
                    rkt2.stop("right") 
        if dbgTime: print "\t Time after event:", time.clock() - start  
        
        
    


        #print ("Score: Player 1 - " + str(rkt.score) + " Player 2 - " + str(rkt2.score))
        rkt.update(size)
        rkt2.update(size)
        
        rktScore.update(rkt.score)
        rkt2Score.update(rkt2.score)
        
        for block in level:
            block.update()
            
        for blackblock in level:
            blackblock.update()
            
        if dbgTime: print "\t Time after  update:", time.clock() - start  
        
        for ball in balls:
            ball.update(size)
            if ball.rktcollide(rkt):
                print "racket 1"
                ball.owner = 1
            if ball.rktcollide(rkt2):
                print "racket 2"
                ball.owner = 2
            for block in level:
                block.pbcollide(ball)
                if ball.blockcollide(block):
                    if block.hp <= 0:
                        print "hit"
                        if ball.owner == 1:
                            rkt.score += block.score
                        elif ball.owner == 2:
                            rkt2.score += block.score
                
            
                
        if dbgTime: print "\t Time after  collide:", time.clock() - start  
            
             
        for block in level:
            if not block.living:
                level.remove(block)

    
        

        if rkt.score > rkt2.score:
            if len(level) < (rkt.score - rkt2.score):
                mode = "p1win"
                
        if rkt2.score > rkt.score:
            if len(level) < (rkt2.score - rkt.score):
                mode = "p2win"


        screen.blit(bgimage, bgrect)
        if dbgTime: print "\t\t Time background  Draw:", time.clock() - start  
        screen.blit(rktScore.image, rktScore.rect)
        screen.blit(rkt2Score.image, rkt2Score.rect)
        if dbgTime: print "\t\t Time score  Draw:", time.clock() - start  
        for ball in balls:
            screen.blit(ball.image, ball.rect)
            if dbgTime: print "\t\t Time balls  Draw:", time.clock() - start  
        screen.blit(rkt.image, rkt.rect)
        screen.blit(rkt2.image, rkt2.rect)
        if dbgTime: print "\t\t Time paddles  Draw:", time.clock() - start  
        for block in level:
            screen.blit(block.image, block.rect)
        if dbgTime: print "\t\t Time blocks  Draw:", time.clock() - start  
        pygame.display.flip()
        clock.tick(60)
        if dbgTime: print "\t Time after  Draw:", time.clock() - start  

################END################
 
    endimage = pygame.image.load ("Screens/EndSplashScreen.png")
    endrect = endimage.get_rect()
    while mode == "end":
        for event in pygame.event.get():
            #print event.type
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mode = "start"
        
        screen.blit(endimage, endrect)
        pygame.display.flip()
        clock.tick(60)
        
        
        
#########AREYOUSURE######



    sureimage = pygame.image.load ("Screens/areYouSure.png")
    surerect = sureimage.get_rect()
    while mode == "ays":
        for event in pygame.event.get():
            #print event.type
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                if event.buttons[0] == 0:
                    yesButton.checkHover(event.pos)
                    noButton.checkHover(event.pos)
                else:
                    yesButton.checkClick(event.pos)
                    noButton.checkClick(event.pos)
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                print event.button
                if event.button == 1:
                    yesButton.checkClick(event.pos)
                    noButton.checkClick(event.pos)   
                         
            if event.type == pygame.MOUSEBUTTONUP:
                if yesButton.collidePt(event.pos):
                    mode = "quit"
                    
                if noButton.collidePt(event.pos):
                    mode = "menu"
                        
                        
        screen.blit(sureimage, surerect)
        screen.blit(yesButton.image, yesButton.rect)
        screen.blit(noButton.image, noButton.rect)
        pygame.display.flip()
        clock.tick(60)
        
##########QUIT########


    while mode == "quit":
        sys.exit()


########Player 1 Wins######

    endimages = [ pygame.image.load ("Screens/p1Win.png"),
                   pygame.image.load ("Screens/p1Win2.png"),
                   pygame.image.load ("Screens/p1Win3.png")]
    endimage = endimages[currentImage]
    endrect = endimage.get_rect()
    lastImage = len(endimages)-1
    while mode == "p1win":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                if event.buttons[0] == 0:
                    quitwinButton.checkHover(event.pos)
                    menuButton.checkHover(event.pos)
                else:
                    quitwinButton.checkClick(event.pos)
                    menuButton.checkClick(event.pos)
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                print event.button
                if event.button == 1:
                    quitwinButton.checkClick(event.pos)
                    menuButton.checkClick(event.pos)   
                         
            if event.type == pygame.MOUSEBUTTONUP:
                if quitwinButton.collidePt(event.pos):
                    mode = "quit"
                    
                if menuButton.collidePt(event.pos):
                    mode = "menu"
                        
        if aniTimer < aniTimerMax:
            aniTimer += 1
        else:
            aniTimer = 0
            if currentImage < lastImage:
                currentImage += 1
            else:
                currentImage = 0
            endimage = endimages [currentImage]
        
            
        screen.blit(endimage, endrect)
        screen.blit(quitwinButton.image, quitwinButton.rect)
        screen.blit(menuButton.image, menuButton.rect)
        pygame.display.flip()
        clock.tick(60)
        
        
#########Player 2 Wins########

    endimages = [ pygame.image.load ("Screens/p2Win.png"),
                   pygame.image.load ("Screens/p2Win2.png"),
                   pygame.image.load ("Screens/p2Win3.png")]
    endimage = endimages[currentImage]
    endrect = endimage.get_rect()
    lastImage = len(endimages)-1
    while mode == "p2win":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                if event.buttons[0] == 0:
                    quitwinButton.checkHover(event.pos)
                    menuButton.checkHover(event.pos)
                else:
                    quitwinButton.checkClick(event.pos)
                    menuButton.checkClick(event.pos)
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                print event.button
                if event.button == 1:
                    quitwinButton.checkClick(event.pos)
                    menuButton.checkClick(event.pos)   
                         
            if event.type == pygame.MOUSEBUTTONUP:
                if quitwinButton.collidePt(event.pos):
                    mode = "quit"
                    
                if menuButton.collidePt(event.pos):
                    mode = "menu"
                        
        if aniTimer < aniTimerMax:
            aniTimer += 1
        else:
            aniTimer = 0
            if currentImage < lastImage:
                currentImage += 1
            else:
                currentImage = 0
            endimage = endimages [currentImage]
            
        screen.blit(endimage, endrect)
        screen.blit(quitwinButton.image, quitwinButton.rect)
        screen.blit(menuButton.image, menuButton.rect)
        pygame.display.flip()
        clock.tick(60)

#######EASTEREGG1#######
    eggimage = pygame.image.load ("Screens/easterEgg.png")
    eggrect = eggimage.get_rect()
    while mode == "pew":
        screen.blit (bgimage, bgrect)
        pygame.display.flip()
        pygame.time.delay(1300)
        webbrowser.open('https://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw')
        sys.exit()
        
    while mode == "g":
        pygame.time.delay(300)
        webbrowser.open('https://www.google.com/search?q=atari+breakout&safe=strict&rlz=1C1CHBF_enUS806US806&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjY_4bvjf_gAhWunuAKHYKuAysQ_AUIDigB&biw=1858&bih=1009')
        sys.exit()
        
    

