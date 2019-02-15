import pygame, sys, math

class Button():
    def __init__(self, kind, pos=[0,0]):
        if kind == "easy":
            self.basicImage = pygame.image.load("Buttons/easyBasic.png")
            self.hoverImage = pygame.image.load("Buttons/easyHover.png")
            self.clickImage = pygame.image.load("Buttons/easyClick.png")
        if kind == "medium":
            self.basicImage = pygame.image.load("Buttons/mediumBasic.png")
            self.hoverImage = pygame.image.load("Buttons/mediumHover.png")
            self.clickImage = pygame.image.load("Buttons/mediumClick.png")
        if kind == "hard":
            self.basicImage = pygame.image.load("Buttons/hardBasic.png")
            self.hoverImage = pygame.image.load("Buttons/hardHover.png")
            self.clickImage = pygame.image.load("Buttons/hardClick.png")
            
            
        self.image = self.basicImage
        self.rect = self.image.get_rect(center=pos)
        self.radius = (self.rect.width/2 + self.rect.height/2)/2
        
    def collidePt(self, pt):
        if self.rect.right > pt[0]:
            if self.rect.left < pt[0]:
                if self.rect.top < pt[1]:
                    if self.rect.bottom > pt[1]:
                        return True
        return False
        
    def checkHover(self, pt):
        if self.collidePt(pt):
            self.image = self.hoverImage
        else:
            self.image = self.basicImage
            
    def checkClick(self, pt):
        if self.collidePt(pt):
            self.image = self.clickImage
        else:
            self.image = self.basicImage

