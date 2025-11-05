import pygame
import random
from Tile import Tile

class Table:
    def __init__(self, rows, columns, width, height, color):
        self.tiles = []
        self.rows = rows
        self.columns = columns
        self.width = width
        self.height = height
        self.color = color

    def split_the_table(self):
        tile_width = self.width / self.columns
        tile_height = self.height / self.rows
        for row in range(self.rows):
            row_list = []
            for col in range(self.columns):
                x = col * tile_width
                y = row * tile_height
                tile = Tile(x, y, tile_width, tile_height, self.color)
                row_list.append(tile)
            self.tiles.append(row_list)

    def get_tile_at(self, point):
        for row in self.tiles:
            for tile in row:
                if tile.contains_point(point):
                    return tile
        return None

    def turn_yellow_to_red(self):
        for row in self.tiles:
            for tile in row:
                if tile.color == pygame.Color('yellow'):
                    tile.change_color(pygame.Color('red'))

    def reset_red_tiles(self):
        for row in self.tiles:
            for tile in row:
                if tile.color == pygame.Color('red'):
                    tile.change_color(pygame.Color('green'))
#3
    def randomize_tiles(self):
        green_tiles = [tile for row in self.tiles for tile in row if tile.color == pygame.Color('green')]
        if not green_tiles:
            return
        num_yellow = max(1, int(len(green_tiles) * 0.2))
        yellow_tiles = random.sample(green_tiles, num_yellow)
        for tile in yellow_tiles:
            tile.change_color(pygame.Color('yellow'))

    def draw(self, screen):
        for row in self.tiles:
            for tile in row:
                tile.draw(screen)
