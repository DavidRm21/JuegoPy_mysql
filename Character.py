import pygame 
import random

class Character:

    def __init__(self, x, y):
        global size
        self.rect = pygame.Rect((x, y, 50, 50))

    # Movimiento del personaje

    def move(self, screen_width):
        
        SPEED = 10
        dx = 0

        # Obtener la tecla presionada
        key = pygame.key.get_pressed()

        if key[pygame.K_a] or key[pygame.K_LEFT]:
            dx = -SPEED
            
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            dx = +SPEED

        # Colisión con la pantalla
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right

        # Actualizar la posición del jugador
        self.rect.x += dx

    
    # Movimiento del enemigo

    def enemyMove(self, width, heigth):
        i = 0
        if self.rect.y >= 0 and self.rect.y < heigth and i == 0:
            
            self.rect.bottom += 8
            
        else: 
            self.rect.x = random.randint(0, width - 50)
            self.rect.y = 0 
        
    
    def resetMove(self, width):

        self.rect.x = random.randint(0, width - 50)
        self.rect.y = 0

    def colision(self, enemyX, enemyY):

        if (enemyX >= self.rect.x and enemyX < (self.rect.x + 50)) or (self.rect.x >= enemyX and self.rect.x < (enemyX + 50)):

            if(enemyY >= self.rect.y and enemyY < (self.rect.y + 50)) or (self.rect.y >= enemyY and self.rect.y < (enemyY + 50)):

                return True
            
        return False

    # Dibujar el personaje
        
    def draw(self, surface, SKIN, ):
        pygame.draw.rect(surface, SKIN, self.rect)

    

