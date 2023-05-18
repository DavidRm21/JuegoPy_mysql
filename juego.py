import pygame
import sys
import random
from Character import Character

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
JUGADOR_SKIN = (255, 0, 0)
ENEMY_SKIN = (0, 0, 255)
BACKGROUND = (0, 0, 0)

#bg_image = pygame.image.load("assets/fondo23.jpg").convert_alpha()

def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    window.blit(scaled_bg, (0,0))

# Actualizacion de paantalla y dimension
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS = 60


# Menu
menu_options = ["Jugar", "Opciones", "Salir"]
selected_option = 0

# Instanciar los personajes
Character_1 = Character(SCREEN_WIDTH / 3, SCREEN_HEIGHT - 80) 
enemy_1 = Character((random.randint(0, SCREEN_WIDTH - 50)), 0)

lives = 3
score = 0
game_over = False

while not game_over:

    clock.tick(FPS)
    #draw_bg()
    window.fill(BACKGROUND)

    # Jugador
    Character_1.draw(window, JUGADOR_SKIN)
    Character_1.move(SCREEN_WIDTH)

    # Enemigos
    enemy_1.draw(window, ENEMY_SKIN)
    enemy_1.enemyMove(SCREEN_WIDTH ,SCREEN_HEIGHT)

    if enemy_1.rect.y == SCREEN_HEIGHT:
        score += 100   

    print(score)

    # Colision
    if Character_1.colision(enemy_1.rect.x, enemy_1.rect.y) and lives > 0:
        
        enemy_1.resetMove(SCREEN_WIDTH)
        lives -= 1
        
        if lives <= 0:
            game_over = True
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()

pygame.quit()