import pygame, sys, math

class Block():
    def __init__(self,  pos=[0,0]):
        self.image = pygame.image.load("Blocks/wall1.png")
        self.rect = self.image.get_rect(center=pos)
        self.radius = (self.rect.width/2 + self.rect.height/2)/2

