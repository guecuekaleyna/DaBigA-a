
import random

import pygame

from table import Table

pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("bg_music.ogg")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1) # -1 = unendlich wiederholen


#Highscore
def load_highscore():
    try:
        with open("highscore.txt", "r") as f:
            return int(f.read())
    except:
        return 0

def save_highscore(score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))

# Fenstergröße und Screen-Setup
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Falling Floor")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)

# Table-Setup
table = Table(rows=5, columns=5, width=width, height=height, color=pygame.Color('green'))
table.split_the_table()
table.randomize_tiles()

# Timer & Phase-Management
phase = 'countdown'
countdown_time = 10
phase_start_time = pygame.time.get_ticks()
phase_duration = 5000  # 5 Sekunden pro Phase
difficulity = 1.0
score = 0
highscore = load_highscore()

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
                    score += 1
                elif clicked_tile.color == pygame.Color('yellow'):
                    score -= 1
                elif clicked_tile.color == pygame.Color('red'):
                    print('Game Over!')
                    running = False

    #Countdown Phase
    if phase == 'countdown':
        seconds = (pygame.time.get_ticks() - phase_start_time) / 1000
        remaining = max(0, countdown_time - int(seconds))
        if remaining <= 0:
            phase = 'yellow'
            phase_start_time = pygame.time.get_ticks()

    # Phase-Management
    current_time = pygame.time.get_ticks()
    if phase != 'countdown':
        if current_time - phase_start_time > phase_duration:
            if phase == 'yellow':
                table.turn_yellow_to_red()
                phase = 'red'
            elif phase == 'red':
                table.reset_red_tiles()
                table.randomize_tiles()
                difficulty *= 1.01
                phase_duration = max(1000, int(phase_duration * 0.99))
                score += 5
                phase = 'yellow'
            phase_start_time = current_time

    #Highscore speichern
        if score > highscore:
            highscore = score
            save_highscore(highscore)

    # Drawing
    screen.fill((0, 0, 0))
    table.draw(screen)


    #Textanzeige oben links
    score_text = font.render(f"Score: {score}  Highscore: {highscore}", True, pygame.Color('white'))
    screen.blit(score_text, (20, 20))

    #Countdown anzeigen (falls aktiv)
    if phase == 'countdown':
        countdown_text = font.render(f"Start in: {remaining}", True, pygame.Color('white'))
        screen.blit(countdown_text, (width // 2 - 80, height // 2 - 30))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
#2