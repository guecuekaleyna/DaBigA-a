import pygame
from table import Table

pygame.init()

# Fenstergröße und Screen-Setup
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Falling Floor")
clock = pygame.time.Clock()

# Table-Setup
table = Table(rows=5, columns=5, width=width, height=height, color=pygame.Color('green'))
table.split_the_table()
table.randomize_tiles()

# Timer & Phase-Management
phase = 'yellow'
phase_start_time = pygame.time.get_ticks()
phase_duration = 5000  # 5 Sekunden pro Phase

running = True
while running:
    # Event-Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            clicked_tile = table.get_tile_at(pos)
            if clicked_tile:
                if clicked_tile.color == pygame.Color('green'):
                    print('Safe')
                elif clicked_tile.color == pygame.Color('yellow'):
                    print('Caution')
                else:
                    print('Game Over')

    # Phase-Management
    current_time = pygame.time.get_ticks()
    if current_time - phase_start_time > phase_duration:
        if phase == 'yellow':
            table.turn_yellow_to_red()
            phase = 'red'
        elif phase == 'red':
            table.reset_red_tiles()
            table.randomize_tiles()
            phase = 'yellow'
        phase_start_time = current_time

    # Drawing
    screen.fill((0, 0, 0))
    table.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
#2