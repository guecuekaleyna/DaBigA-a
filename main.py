import pygame
import random

from Background import Background
from table import Table
from Tile import Tile

pygame.init()

width, height = 600, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("Black Background")

background = Background((0,0,0))
table = Table(5,5, 5, 5)
table.split_the_table()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            running = True


    background.draw(screen)
    table.draw(screen)
    pygame.display.flip()

pygame.quit()
