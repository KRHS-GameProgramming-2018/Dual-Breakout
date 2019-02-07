import pygame, sys, math, time, random, time
from Ball import *
from Racket import *
from Score import *
from LevelLoad import *
from Block import *
from BlackBlock import *
pygame.init()

dbgTime = True

balls = []

clock = pygame.time.Clock()

width = 1200
height = 950
size = width, height









screen = pygame.display.set_mode(size)

level1 = loadLevel ("Levels/1.lvl")
level2 = loadLevel ("Levels/2.lvl")
level3 = loadLevel ("Levels/3.lvl")




start = time.clock()

mode = "start"

while True: 
    menuimage = pygame.image.load ("Screens/MainMenu.png")
    menurect = menuimage.get_rect()
    startimage = pygame.image.load ("Screens/backroundStartScreen.png")
    startrect = startimage.get_rect()
    
    ###########START####
    
    while mode == "start":
        for event in pygame.event.get():
            #print event.type
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mode = "menu"
        
        screen.blit(startimage, startrect)
        pygame.display.flip()
        clock.tick(60)
 
 ###########MENU#########
 
    
    while mode == "menu":
        for event in pygame.event.get():
            #print event.type
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    mode = "easy"
                if event.key == pygame.K_m:
                    mode = "medium"
                if event.key == pygame.K_h:
                    mode = "hard"
                
        
        screen.blit(menuimage, menurect)
        pygame.display.flip()
        clock.tick(60)
    
    
    
    for i in range(1):
        images = ["Ball/ball.png"]
        speed = [5,5]
        pos = [random.randint(300,1000),300]
        balls += [Ball(images[0], speed, pos)]

    for i in range(1):
        images = ["Ball/ball.png"]
        speed = [5,-5]
        pos = [random.randint(300,1000),650]
        balls += [Ball(images[0], speed, pos)]


    rkt= racket("Racket/racket.png", 15, [width/2, height-10])
    rktScore = Score(0, [50, height-25])
    rkt2= racket("Racket/racket.png", 15, [width/2, 10])
    rkt2Score = Score(0, [width-50, 25])
    
    bgimage = pygame.image.load("screens/backround1.png")
    bgrect = bgimage.get_rect()
    easyimage = pygame.image.load ("screens/backroundEasy.png")
    easyrect = easyimage.get_rect()
    
    

    
    ###########MEDIUM######
    
    
    while mode == "medium":
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
                            if event.type == pygame.QUIT: sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_t:
                                    paused = False
                                    
                if event.key == pygame.K_ESCAPE:
                    pygame.quit() 
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
        
        for block in level2:
            block.update()
            
        if dbgTime: print "\t Time after  update:", time.clock() - start  
        
        for ball in balls:
            ball.update(size)
            if ball.rktcollide(rkt):
                print "racket 1"
                ball.owner = 1
            if ball.rktcollide(rkt2):
                print "racket 2"
                ball.owner = 2
            for block in level2:
                if ball.blockcollide(block):
                    if ball.owner == 1: 
                        rkt.score +=1
                    elif ball.owner == 2:
                        rkt2.score +=1
                block.pbcollide(ball)
            if ball.rect.top <0 :
                if rkt2.score >= 3:
                    rkt2.score -= 1
            if ball.rect.bottom > height :
                if rkt.score >= 3:
                    rkt.score -= 1
                
        if dbgTime: print "\t Time after  collide:", time.clock() - start  
            
            
        for block in level2:
            if not block.living:
                level2.remove(block)
        
    
        screen.blit(bgimage, bgrect)
        if dbgTime: print "\t\t Time background  Draw:", time.clock() - start  
        screen.blit(rktScore.image, rktScore.rect)
        screen.blit(rkt2Score.image, rkt2Score.rect)
        if dbgTime: print "\t\t Time score  Draw:", time.clock() - start  
        for ball in balls:
            screen.blit(ball.image, ball.rect)
            print "\t\t Time balls  Draw:", time.clock() - start  
        screen.blit(rkt.image, rkt.rect)
        screen.blit(rkt2.image, rkt2.rect)
        if dbgTime: print "\t\t Time paddles  Draw:", time.clock() - start  
        for block in level2:
            screen.blit(block.image, block.rect)
        if dbgTime: print "\t\t Time blocks  Draw:", time.clock() - start  
        pygame.display.flip()
        clock.tick(60)
        if dbgTime: print "\t Time after  Draw:", time.clock() - start  
        
        
    ################EASY##########    
        
        
    while mode == "easy":
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
                            if event.type == pygame.QUIT: sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_t:
                                    paused = False
                                    
                if event.key == pygame.K_ESCAPE:
                    pygame.quit() 
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
        
        for block in level1:
            block.update()
            
        if dbgTime: print "\t Time after  update:", time.clock() - start  
        
        for ball in balls:
            ball.update(size)
            if ball.rktcollide(rkt):
                print "racket 1"
                ball.owner = 1
            if ball.rktcollide(rkt2):
                print "racket 2"
                ball.owner = 2
            for block in level1:
                if ball.blockcollide(block):
                    if ball.owner == 1: 
                        rkt.score +=1
                    elif ball.owner == 2:
                        rkt2.score +=1
                block.pbcollide(ball)
            if ball.rect.top <0 :
                if rkt2.score >= 3:
                    rkt2.score -= 1
            if ball.rect.bottom > height :
                if rkt.score >= 3:
                    rkt.score -= 1
                
        if dbgTime: print "\t Time after  collide:", time.clock() - start  
            
            
        for block in level1:
            if not block.living:
                level1.remove(block)
        
    
        screen.blit(easyimage, easyrect)
        if dbgTime: print "\t\t Time background  Draw:", time.clock() - start  
        screen.blit(rktScore.image, rktScore.rect)
        screen.blit(rkt2Score.image, rkt2Score.rect)
        if dbgTime: print "\t\t Time score  Draw:", time.clock() - start  
        for ball in balls:
            screen.blit(ball.image, ball.rect)
            print "\t\t Time balls  Draw:", time.clock() - start  
        screen.blit(rkt.image, rkt.rect)
        screen.blit(rkt2.image, rkt2.rect)
        if dbgTime: print "\t\t Time paddles  Draw:", time.clock() - start  
        for block in level1:
            screen.blit(block.image, block.rect)
        if dbgTime: print "\t\t Time blocks  Draw:", time.clock() - start  
        pygame.display.flip()
        clock.tick(60)
        if dbgTime: print "\t Time after  Draw:", time.clock() - start
 
 
 
 ###########HARD########
        
        
    while mode == "hard":
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
                            if event.type == pygame.QUIT: sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_t:
                                    paused = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit = True
                    
                                    
                if event.key == pygame.K_q:
                    pygame.quit() 
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
        
        for block in level3:
            block.update()
            
            
        if dbgTime: print "\t Time after  update:", time.clock() - start  
        
        for ball in balls:
            ball.update(size)
            if ball.rktcollide(rkt):
                print "racket 1"
                ball.owner = 1
            if ball.rktcollide(rkt2):
                print "racket 2"
                ball.owner = 2
            for block in level3:
                if ball.blockcollide(block):
                    if ball.owner == 1: 
                        rkt.score +=1
                    elif ball.owner == 2:
                        rkt2.score +=1
                block.pbcollide(ball)
            if ball.rect.top <0 :
                if rkt2.score >= 3:
                    rkt2.score -= 1
            if ball.rect.bottom > height :
                if rkt.score >= 3:
                    rkt.score -=1
                
        if dbgTime: print "\t Time after  collide:", time.clock() - start  
            
            
        for block in level3:
            if not block.living:
                level3.remove(block)
        
    
        screen.blit(bgimage, bgrect)
        if dbgTime: print "\t\t Time background  Draw:", time.clock() - start  
        screen.blit(rktScore.image, rktScore.rect)
        screen.blit(rkt2Score.image, rkt2Score.rect)
        if dbgTime: print "\t\t Time score  Draw:", time.clock() - start  
        for ball in balls:
            screen.blit(ball.image, ball.rect)
            print "\t\t Time balls  Draw:", time.clock() - start  
        screen.blit(rkt.image, rkt.rect)
        screen.blit(rkt2.image, rkt2.rect)
        if dbgTime: print "\t\t Time paddles  Draw:", time.clock() - start  
        for block in level3:
            screen.blit(block.image, block.rect)
        if dbgTime: print "\t\t Time blocks  Draw:", time.clock() - start  
        pygame.display.flip()
        clock.tick(60)
        if dbgTime: print "\t Time after  Draw:", time.clock() - start
