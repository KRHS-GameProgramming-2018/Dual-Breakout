import pygame, sys, math, time, random, time
from Ball import *
from Racket import *
from Score import *
from LevelLoad import *
from Block import *
pygame.init()

balls = []

clock = pygame.time.Clock()


width = 1200
height = 950
size = width, height

for i in range(1):
    images = ["Ball/ball.png"]
    speed = [6,6]
    pos = [random.randint(300,1000),300]
    balls += [Ball(images[0], speed, pos)]

for i in range(1):
    images = ["Ball/ball.png"]
    speed = [6,-6]
    pos = [random.randint(300,1000),650]
    balls += [Ball(images[0], speed, pos)]


rkt= racket("Racket/racket.png", 15, [width/2, height-10])
rktScore = Score(0, [50, height-25])
rkt2= racket("Racket/racket.png", 15, [width/2, 10])
rkt2Score = Score(0, [width-50, 25])




bgColor = r,g,b = 50, 50, 50

bgimage = pygame.image.load("screens/backround1.png")
bgrect = bgimage.get_rect()

screen = pygame.display.set_mode(size)

level= loadLevel("Levels/2.lvl")

start = time.clock()

while True:
    print "\nLoopTine:", time.clock() - start
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
    print "\t Time after event:", time.clock() - start  
            
            
        
    

    #print ("Score: Player 1 - " + str(rkt.score) + " Player 2 - " + str(rkt2.score))
    rkt.update(size)
    rkt2.update(size)
    
    rktScore.update(rkt.score)
    rkt2Score.update(rkt2.score)
    
    for block in level:
        block.update()
        
    print "\t Time after  update:", time.clock() - start  
    
    for ball in balls:
        ball.update(size)
        if ball.rktcollide(rkt):
            print "racket 1"
            ball.owner = 1
        if ball.rktcollide(rkt2):
            print "racket 2"
            ball.owner = 2
        for block in level:
            if ball.blockcollide(block):
                if ball.owner == 1: 
                    rkt.score +=1
                elif ball.owner == 2:
                    rkt2.score +=1
            block.pbcollide(ball)
            
    print "\t Time after  collide:", time.clock() - start  
        
        
    for block in level:
        if not block.living:
            level.remove(block)
    
    bgColor = r,g,b
    screen.fill(bgColor)
    screen.blit(bgimage, bgrect)
    print "\t\t Time background  Draw:", time.clock() - start  
    screen.blit(rktScore.image, rktScore.rect)
    screen.blit(rkt2Score.image, rkt2Score.rect)
    print "\t\t Time score  Draw:", time.clock() - start  
    for ball in balls:
        screen.blit(ball.image, ball.rect)
        print "\t\t Time balls  Draw:", time.clock() - start  
    screen.blit(rkt.image, rkt.rect)
    screen.blit(rkt2.image, rkt2.rect)
    print "\t\t Time paddles  Draw:", time.clock() - start  
    for block in level:
        screen.blit(block.image, block.rect)
    print "\t\t Time blocks  Draw:", time.clock() - start  
    pygame.display.flip()
    clock.tick(60)
    print "\t Time after  Draw:", time.clock() - start  
        
