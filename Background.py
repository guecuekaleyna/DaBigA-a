import pygame

class Background:
    def __init__(self, color=(200, 0, 0)):
        self.color = color

    def draw(self, screen):
        screen.fill(self.color)
#1