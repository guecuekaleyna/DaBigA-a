import pygame
from Tile import Tile



#colors for main game
green = pygame.Color('green')
yellow = pygame.Color('yellow')
red = pygame.Color('red')

#colors for timer, highscore
blue = pygame.Color('blue')
white = pygame.Color('white')

WIDTH = 600
HEIGHT = 600
SCREEN = (WIDTH, HEIGHT)


class Table:
    def __init__(self, rows, columns, width, height):
        '''
        :param rows:
        :param columns:
        :param width:
        :param height:
        '''
        self.tiles = []
        self.rows = rows
        self.columns = columns
        self.width = width
        self.height = height

    def split_the_table(self):
        '''
        :return: splits the table into rows and columns of tiles
        '''
        #table = Table(5, 5, WIDTH, HEIGHT)
        tile_width = SCREEN[0] / self.columns
        tile_height = SCREEN[1] / self.rows
        for row in range(self.rows):
            row_list = []
            for col in range(self.columns):
                x = col * tile_width
                y = row * tile_height
                tile = Tile(x, y, tile_width, tile_height, color=green)
                row_list.append(tile)
            self.tiles.append(row_list)

    def draw(self, screen):
        '''
        :param screen:
        :return: drawn rows and columns ofn tiles
        '''
        for row in self.tiles:
            for tile in row:
                tile.draw(screen)

