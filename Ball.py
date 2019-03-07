import pygame, sys, math, random


class Ball():
    def __init__(self, image, speed=[5,5], startPos=[0,0]):
        self.images= [
                      pygame.image.load("Ball/ball.png"),
                      pygame.image.load("Ball/ballA.png"),
                      pygame.image.load("Ball/ballB.png"),
                      pygame.image.load("Ball/ballAni1.png"),
                      pygame.image.load("Ball/ballAni3.png"),
                      pygame.image.load("Ball/ballAni4.png"),
                      pygame.image.load("Ball/ballAni5.png"),
                      pygame.image.load("Ball/ballAni6.png"),
                      pygame.image.load("Ball/ballAni7.png"),
                      pygame.image.load("Ball/ballAni8.png"),
                      pygame.image.load("Ball/ballAni9.png"),
                      pygame.image.load("Ball/ballAni10.png"),
                      pygame.image.load("Ball/ballAni11.png"),
                                        
                                        ]
                                        
        self.image= self.images[0]
        self.rect = self.image.get_rect(center = startPos)
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        #self.rect = self.rect.move(startPos)
        self.radius = (self.rect.width/2 + self.rect.height/2)/2
        self.didBounceX = False
        self.didBounceY = False
        
        self.living = True
        self.dying = False
        self.frame = 0 
        self.frameMax = len(self.images) -1 
        self.frameTimer = 0
        self.frameTimerMax = 60/6/len(self.images)
        
        self.startPos = startPos
        self.startSpeed = speed
        
        self.owner = 0
        
    def getDist(self, pt):
        x1 = self.rect.centerx
        y1 = self.rect.centery
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
            
    
    
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def bounceWall(self, size):
        width = size[0]
        height = size[1]
        if self.rect.left < 0 or self.rect.right > width:
            if not self.didBounceX:
                self.speedx = -self.speedx
                self.didBounceX = True
        if self.rect.top < 0 or self.rect.bottom > height:
            if not self.didBounceY:
                self.speedy = -self.speedy
                self.didBounceY = True
                self.dying = True
                self.speedx = 0
                self.speedy = 0
                self.owner = 0

    def update(self, size):
        self.didBounceX = False
        self.didBounceY = False
        self.move()
        self.bounceWall(size)
        if self.owner == 0:
            self.image = self.images[0]
        if self.owner == 1:
            self.image = self.images[1]
        if self.owner == 2:
            self.image = self.images[2]
        if self.dying == True:
            if self.frameTimer < self.frameTimerMax :
                self.frameTimer += 1
            else:
                self.frameTimer = 0
                self.frame += 1
                if self.frame > self.frameMax:
                    self.living = False
                    self.dying = False
                    self.frame = 0

                    spawnList = [300,650]
                    if self.owner == 0:
                        self.rect.center = [random.randint(200,1000),random.choice(spawnList)]
                    if self.owner == 1:
                        self.rect.center = [random.randint(200,1000),300]
                    if self.owner == 2:
                        self.rect.center = [random.randint(200,1000),650]

                    self.speedx = self.startSpeed[0]
                    self.speedy = self.startSpeed[1]
                self.image = self.images[self.frame]
    
            
    def rktcollide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.top < other.rect.bottom:
                    if self.rect.bottom > other.rect.top:
                            if not self.didBounceX:
                                if self.speedx > 1: #right
                                    if self.rect.centerx < other.rect.centerx:
                                        self.speedx = -self.speedx
                                        self.didBounceX = True
                                if self.speedx < 1: #left
                                    if self.rect.centerx > other.rect.centerx:
                                        self.speedx = -self.speedx
                                        self.didBounceX = True
                                        
                            if not self.didBounceY:
                                if self.speedy > 1: #down
                                    if self.rect.centery < other.rect.centery:
                                        self.speedy = -self.speedy
                                        self.didBounceY = True
                                if self.speedy < 1: #up
                                    if self.rect.centery > other.rect.centery:
                                        self.speedy  = -self.speedy
                                        self.didBounceY = True

                                return True
        return False

    def blockcollide(self, other):
        if not other.dying:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.top < other.rect.bottom:
                        if self.rect.bottom > other.rect.top:
                            if self.radius+other.radius > self.getDist(other.rect.center):
                                if not self.didBounceX:
                                    if self.speedx > 1: #right
                                        if self.rect.centerx < other.rect.centerx:
                                            self.speedx = -self.speedx
                                            self.didBounceX = True
                                    if self.speedx < 1: #left
                                        if self.rect.centerx > other.rect.centerx:
                                            self.speedx = -self.speedx
                                            self.didBounceX = True
                                            
                                if not self.didBounceY:
                                    if self.speedy > 1: #down
                                        if self.rect.centery < other.rect.centery:
                                            self.speedy = -self.speedy
                                            self.didBounceY = True
                                    if self.speedy < 1: #up
                                        if self.rect.centery > other.rect.centery:
                                            self.speedy  = -self.speedy
                                            self.didBounceY = True

                                    return True
            return False
    
