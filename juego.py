import pygame
import sys
import random
from Character import Character
import coneccion 

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
player_skin = RED
enemy_skin = BLUE
color_text = BLACK


# Función de texto de puntaje en pantalla
def draw_text(surface, text, size, color, x, y):
    font = pygame.font.SysFont("serif", size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)


# Actualizacion de paantalla y dimension
pygame.display.set_caption("Colisión")
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS = 60

# Instanciar los personajes
character_1 = Character(SCREEN_WIDTH / 3, SCREEN_HEIGHT - 80) 
enemy_1 = Character((random.randint(0, SCREEN_WIDTH - 50)), 0)

lives = 3
score = 0
game_over = False

# Menu principal
while not game_over:
    clock.tick(FPS)
    
    if score >= 0 and score < 800 or score >= 2000 and score < 5000 or score >= 10000:
        window.fill(BLACK)
        player_skin = WHITE
        enemy_skin = BLUE
        color_text = WHITE
        

    if score >= 800 and score < 2000 or score >= 5000 and score < 10000:
        window.fill(WHITE)
        player_skin = BLACK
        enemy_skin = RED
        color_text = BLACK

    # Jugador
    character_1.draw(window, player_skin)
    character_1.move(SCREEN_WIDTH)

    # Enemigos
    enemy_1.draw(window, enemy_skin)
    enemy_1.enemyMove(SCREEN_WIDTH ,SCREEN_HEIGHT)

    if enemy_1.rect.y >= SCREEN_HEIGHT:
        score += 100 

    
    # Colision
    if character_1.colision(enemy_1.rect.x, enemy_1.rect.y) and lives > 0:
        
        enemy_1.resetMove(SCREEN_WIDTH)
        lives -= 1
        
        if lives <= 0:
            game_over = True
    
    # Puntaje
    draw_text(window, str(score), 25, color_text, SCREEN_WIDTH / 2, 10)
    
    draw_text(window, f"vidas: {lives} ", 25, player_skin, (SCREEN_WIDTH - 50) , SCREEN_HEIGHT - 50)
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit() 

    pygame.display.update()

pygame.quit()

coneccion.Insert("NULL", score)

