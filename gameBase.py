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
    pos = [200,100]
    balls += [Ball(images[random.randint(0,0)], speed, pos)]
    
for i in range(1):
    images = ["Ball/ball.png"]
    speed = [4,4]
    pos = [100,50]
    balls += [Ball(images[random.randint(0,0)], speed, pos)]


rkt= racket("Racket/racket.png", 7, [width/2, height-20])
rkt2= racket("Racket/racket.png", 7, [width/2, 20])




bgColor = r,g,b = 250, 250, 250

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
    
        
    
    
    rkt.update(size)
    rkt2.update(size)
    
    for block in level:
        block.update()
    
    for ball in balls:
        ball.update(size)
        ball.collide(rkt)
        ball.collide(rkt2)
        for block in level:
            ball.collide(block)
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
    #print clock.get_fps()

