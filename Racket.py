import pygame, sys, math
from Ball import *


class racket(Ball):
    def __init__(self,image, speed = 5, startPos=[0,0]):
        Ball.__init__(self, image, [0,0], startPos)
        self.maxSpeed = speed
        self.image = pygame.image.load ("Racket/racket.png")
        
        
    def go(self, direction):
        if direction == "left":
            self.speedx = -self.maxSpeed
            
        if direction == "right":
            self.speedx = self.maxSpeed
            
        
            
            
    def stop(self, direction):
        if direction == "left":
            self.speedx = 0
        if direction == "right":
            self.speedx = 0
        
        
            
    def setPos(self, pos):
        self.rect.center = pos
        
            
    def move(self):
        # ~ if self.goal[0]-self.maxSpeed <= self.rect.centerx <= self.goal[0]+self.maxSpeed:
            # ~ self.speedx = 0
        # ~ if self.goal[1]-self.maxSpeed <= self.rect.centery <= self.goal[1]+self.maxSpeed:
            # ~ self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)

            
    def pbcollide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.top < other.rect.bottom:
                    if self.rect.bottom > other.rect.top:
                        if self.radius + other.radius > self.getDist(other.rect.center):
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


