import pygame
import random
import math
import time

BLACK = (0, 0, 0)
WIDTH, HEIGHT = 1000, 600
MAX_X = WIDTH * 2 // 3
ROJO = (255, 0, 0)
# Clase Enemigo
class Enemigo:
    def __init__(self, x, y, size=20, speed=2):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.image = pygame.image.load('carpeta/enemigo.png').convert_alpha()
        self.projectile_image = pygame.image.load('carpeta/impacto_32_32.png').convert_alpha()
        self.projectiles = []  # Lista para almacenar los proyectiles disparados por el enemigo
        self.vida = 5
        self.direction = random.choice(['arriba', 'arriba+derecha', 'arriba+izquierda', 'abajo', 'abajo+derecha', 'abajo+izquierda', 'izquierda', 'derecha'])
        self.last_direction_change_time = 0
    def disparar(self, jugador):
        dx = jugador.rect.x - self.x
        dy = jugador.rect.y - self.y
        distancia = math.sqrt(dx ** 2 + dy ** 2)
        if distancia != 0:
            dx /= distancia
            dy /= distancia
            # Crear un nuevo proyectil con coordenadas y dirección
            disparo = {'x': self.x, 'y': self.y, 'dx': dx * 2, 'dy': dy * 2}  # Aqui se ajusta la velocidadd
            self.projectiles.append(disparo)



    def dibujar(self, surface):
        surface.blit(self.image, (self.x - self.image.get_width() // 2, self.y - self.image.get_height() // 2))
        for projectile in self.projectiles:
            surface.blit(self.projectile_image, (projectile['x'], projectile['y']))

        # Dibujar barra de vida debajo del enemigo
        vida_length = self.vida * 10  # Ancho de la barra de vida (10 px por punto de vida)
        pygame.draw.rect(surface, ROJO, (self.x - vida_length // 2, self.y + self.size + 5, vida_length, 5))

    def mover_enemigo(self, tiempo_actual):
        # Cambiar la dirección cada dos segundos
        if tiempo_actual - self.last_direction_change_time >= 2:
            self.direction = random.choice(['arriba', 'arriba+derecha', 'arriba+izquierda', 'abajo', 'abajo+derecha', 'abajo+izquierda', 'izquierda', 'derecha'])
            self.last_direction_change_time = tiempo_actual

        if self.direction == 'arriba':
            if self.y > 150:  # Asegurar que no esté demasiado cerca del borde superior
                self.y -= self.speed
            else:  # Cambiar de dirección si llega al borde
                self.direction = random.choice(['abajo', 'abajo+derecha', 'abajo+izquierda', 'izquierda', 'derecha'])
        elif self.direction == 'abajo':
            if self.y + self.size < HEIGHT - 150:  # Asegurar que no esté demasiado cerca del borde inferior
                self.y += self.speed
            else:  # Cambiar de dirección si llega al borde
                self.direction = random.choice(['arriba', 'arriba+derecha', 'arriba+izquierda', 'izquierda', 'derecha'])
        elif self.direction == 'izquierda':
            if self.x > 150:  # Asegurar que no esté demasiado cerca del borde izquierdo
                self.x -= self.speed
            else:  # Cambiar de dirección si llega al borde
                self.direction = random.choice(['arriba', 'arriba+derecha', 'abajo', 'abajo+derecha', 'izquierda'])
        elif self.direction == 'derecha':
            if self.x + self.size < MAX_X - 150:  # Asegurar que no esté demasiado cerca del borde derecho
                self.x += self.speed
            else:  # Cambiar de dirección si llega al borde
                self.direction = random.choice(['arriba', 'arriba+izquierda', 'abajo', 'abajo+izquierda', 'derecha'])
        elif self.direction == 'arriba+derecha':
            if self.y > 150 and self.x + self.size < MAX_X - 150:  # Asegurar que no esté demasiado cerca de los bordes
                self.y -= self.speed
                self.x += self.speed
            else:  # Cambiar de dirección si llega al borde
                self.direction = random.choice(['abajo', 'abajo+izquierda', 'izquierda'])
        elif self.direction == 'arriba+izquierda':
            if self.y > 150 and self.x > 150:  # Asegurar que no esté demasiado cerca de los bordes
                self.y -= self.speed
                self.x -= self.speed
            else:  # Cambiar de dirección si llega al borde
                self.direction = random.choice(['abajo', 'abajo+derecha', 'derecha'])
        elif self.direction == 'abajo+derecha':
            if self.y + self.size < HEIGHT - 150 and self.x + self.size < MAX_X - 150:  # Asegurar que no esté demasiado cerca de los bordes
                self.y += self.speed
                self.x += self.speed
            else:  # Cambiar de dirección si llega al borde
                self.direction = random.choice(['arriba', 'arriba+izquierda', 'izquierda'])
        elif self.direction == 'abajo+izquierda':
            if self.y + self.size < HEIGHT - 150 and self.x > 150:  # Asegurar que no esté demasiado cerca de los bordes
                self.y += self.speed
                self.x -= self.speed
            else:  # Cambiar de dirección si llega al borde
                self.direction = random.choice(['arriba', 'arriba+derecha', 'derecha'])

    def actualizar_proyectiles(self):
        # Mover y eliminar los proyectiles que salieron de la pantalla
        for projectile in self.projectiles[:]:
            projectile['x'] += projectile['dx']
            projectile['y'] += projectile['dy']
            if not (0 <= projectile['x'] <= WIDTH and 0 <= projectile['y'] <= HEIGHT):
                self.projectiles.remove(projectile)

    def recibir_danio(self):
        self.vida -= 1

"""        
        def Disparar un proyectil en dirección aleatoria
        projectile = {'x': self.x, 'y': self.y, 'dx': dx * 5, 'dy': dy * 5}  # Guardar la dirección del proyectil
        self.projectiles.append(projectile)"""