import pygame


class Tile:
    def __init__(self, x, y, width, height, color):
        '''
        :param x: x position
        :param y: y position
        :param width: width of the tile
        :param height: height of the tile
        :param color: color of the tile
        '''
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def change_color(self, new_color):
        '''
        :param new_color: for later (change of color with random)
        :return: returns changed color
        '''
        self.color = new_color

    def draw(self, screen):
        '''
        :param screen: tile drawn on screen
        :param rect: rect of the tile
        :.draw.rect: gives contoured tiles back
        :return: drawn tile
        '''
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, rect, 0)
        pygame.draw.rect(screen, (0,0,0), rect, 1)