import pygame, sys, math

class Block():
    def __init__(self,  pos=[0,0]):
        self.images = [pygame.image.load("Blocks/wall11.png"),
                       
        self.rect = self.image.get_rect(center=pos)
        self.radius = (self.rect.width/2 + self.rect.height/2)/2
        self.hp = 1
        self.living = True
        
        self.dying = False
        
    def pbcollide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.top < other.rect.bottom:
                    if self.rect.bottom > other.rect.top:
                        self.hp -= 1
                        print "ouch"
    
    def update(self):
        if self.hp <= 0:
            self.dying = True
