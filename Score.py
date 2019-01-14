import pygame, sys, math, random

class Score():
    def __init__(self,  score=0, pos=[0,0]):
        self.score = score
        self.font = pygame.font.Font(None, 36)
        self.image = self.font.render(str(self.score), True, (255,255,255))
        self.rect = self.image.get_rect(center = pos)
        
    def update(self, newScore):
        self.score = newScore
        self.image = self.font.render(str(self.score), True, (255,255,255))
        self.rect = self.image.get_rect(center = self.rect.center)
