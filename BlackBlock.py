import pygame, sys, math, random

class Block():
    def __init__(self,  pos=[0,0]):
        self.images = [pygame.image.load("Blocks/Black/black1.png"),
                       pygame.image.load("Blocks/Black/black2.png"),
                       pygame.image.load("Blocks/Black/black3.png"),
                       pygame.image.load("Blocks/Black/blackAni1.png"),
                       pygame.image.load("Blocks/Black/blackAni2.png"),
                       pygame.image.load("Blocks/Black/blackAni3.png"),
                       pygame.image.load("Blocks/Black/black1.png"),
                       ]
        self.image = self.images[random.choice(blockList)]               
        self.rect = self.image.get_rect(center=pos)
        self.radius = (self.rect.width/2 + self.rect.height/2)/2
        self.hp = 3
        
        self.living = True
        self.dying = True
        self.frame = 0 
        self.frameMax = len(self.images) -1 
        self.frameTimer = 0
        self.frameTimerMax = 60/4/len(self.images)
        
    def pbcollide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.top < other.rect.bottom:
                    if self.rect.bottom > other.rect.top:
                        if self.radius+other.radius > self.getDist(other.rect.center):
                            self.hp -= 1
                            self.frame +=1
                            print "ouch"
              
    def getDist(self, pt):
        x1 = self.rect.centerx
        y1 = self.rect.centery
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
    
    def update(self):
        if self.hp <= 0:
            if self.dying:
                if self.frameTimer < self.frameTimerMax :
                    self.frameTimer += 1
                else:
                    self.frameTimer = 0
                    self.frame += 1
                    if self.frame > self.frameMax:
                        self.living = False
                        self.dying = False
                        self.frame = 0
                        #self.rect.center = self.startPos
                        #self.speedx = self.startSpeed[0]
                        #daself.speedy = self.startSpeed[1]
                    self.image = self.images[self.frame]

