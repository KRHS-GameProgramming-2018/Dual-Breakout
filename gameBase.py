import pygame, sys, math, time, random
from Ball import *
from Racket import *
from LevelLoad import *
from Block import *
pygame.init()

balls = []

clock = pygame.time.Clock()

width = 1600
height = 900
size = width, height

for i in range(1):
    images = ["Ball/ball.png"]
    speed = [4,4]
    pos = [random.randint(300,1000),250]
    balls += [Ball(images[0], speed, pos)]
    
for i in range(1):
    images = ["Ball/ball.png"]
    speed = [4,-4]
    pos = [random.randint(300,1000),550]
    balls += [Ball(images[0], speed, pos)]


rkt= racket("Racket/racket.png", 7, [width/2, height-10])
rkt2= racket("Racket/racket.png", 7, [width/2, 10])




bgColor = r,g,b = 50, 50, 50

screen = pygame.display.set_mode(size)

level= loadLevel("Levels/2.lvl")

while True:
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
    
        
    
    print ("Score: Player 1 - " + str(rkt.score) + " Player 2 - " + str(rkt2.score))
    rkt.update(size)
    rkt2.update(size)
    
    for block in level:
        block.update()
    
    for ball in balls:
        ball.update(size)
        if ball.collide(rkt):
            print "racket 1"
            ball.owner = 1
        if ball.collide(rkt2):
            print "racket 2"
            ball.owner = 2
        for block in level:
            if ball.collide(block):
                if ball.owner == 1: 
                    rkt.score +=1
                elif ball.owner == 2:
                    rkt2.score +=1
            block.pbcollide(ball)
        
        
    for block in level:
        if not block.living:
            level.remove(block)
    
    bgColor = r,g,b
    screen.fill(bgColor)
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    screen.blit(rkt.image, rkt.rect)
    screen.blit(rkt2.image, rkt2.rect)
    for block in level:
        screen.blit(block.image, block.rect)
    pygame.display.flip()
    clock.tick(60)
