import pygame, sys, math

class Block():
    def __init__(self,  pos=[0,0]):
        self.images = [pygame.image.load("Blocks/Orange/orange1.png"),
                                        ("Blocks/Orange/orange2.png"),
                                        ("Blocks/Orange/orange3.png"),
                                        ("Blocks/Orange/orange4.png"),
                                        ("Blocks/Red/red1.png"), 
                                        ("Blocks/Red/red2.png"),
                                        ("Blocks/Red/red3.png"),
                                        ("Blocks/Red/red4.png"),
                                        ("Blocks/Yellow/yellow1.png"),
                                        ("Blocks/Yellow/yellow2.png"),
                                        ("Blocks/Yellow/yellow3.png"),
                                        ("Blocks/Yellow/yellow4.png")
                       
                        
                         ]
        self.image = self.images[0]               
        self.rect = self.image.get_rect(center=pos)
        self.radius = (self.rect.width/2 + self.rect.height/2)/2
        self.hp = 1
        
        self.living = True
        self.dying = False
        self.frame = 0 
        self.frameMax = len(self.images) -1 
        self.frameTimer = 0
        self.frameTimerMax = 60/4/len(self.images)
        
    def pbcollide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.top < other.rect.bottom:
                    if self.rect.bottom > other.rect.top:
                        self.hp -= 1
                        print "ouch"
                        
    
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
                        self.rect.center = self.startPos
                        self.speedx = self.startSpeed[0]
                        self.speedy = self.startSpeed[1]
                    self.image = self.images[self.frame]
