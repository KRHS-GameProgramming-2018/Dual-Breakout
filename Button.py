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
        if kind == "quit":
            self.basicImage = pygame.image.load("Buttons/quitBasic.png")
            self.hoverImage = pygame.image.load("Buttons/quitHover.png")
            self.clickImage = pygame.image.load("Buttons/quitClick.png")
        if kind == "yes":
            self.basicImage = pygame.image.load("Buttons/yesBasic.png")
            self.hoverImage = pygame.image.load("Buttons/yesHover.png")
            self.clickImage = pygame.image.load("Buttons/yesClick.png")
        if kind == "no":
            self.basicImage = pygame.image.load("Buttons/noBasic.png")
            self.hoverImage = pygame.image.load("Buttons/noHover.png")
            self.clickImage = pygame.image.load("Buttons/noClick.png")
        if kind == "menu":
            self.basicImage = pygame.image.load("Buttons/menuBasic.png")
            self.hoverImage = pygame.image.load("Buttons/menuHover.png")
            self.clickImage = pygame.image.load("Buttons/menuClick.png")
        if kind == "wquit":
            self.basicImage = pygame.image.load("Buttons/wquitBasic.png")
            self.hoverImage = pygame.image.load("Buttons/wquitHover.png")
            self.clickImage = pygame.image.load("Buttons/wquitClick.png")
        if kind == "g":
            self.basicImage = pygame.image.load("Buttons/gBasic.png")
            self.hoverImage = pygame.image.load("Buttons/gHover.png")
            self.clickImage = pygame.image.load("Buttons/gClick.png")
            
            
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

