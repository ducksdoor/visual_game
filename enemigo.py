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

    def mover_enemigo(self):
        # Actualizar la posición en X del enemigo
        self.x -= self.speed

        # Si el enemigo sale de la pantalla por la izquierda, reiniciar su posición en X
        if self.x < 0 - self.size:
            self.x = 800


#esta un poco rota
    def mover_aleatorio(self):
        # Generar una dirección aleatoria
        dx = -1  # Mover de derecha a izquierda
        dy = random.uniform(-1, 1)

        # Calcular la distancia total y el movimiento por frame
        distancia_total = 100
        movimiento_por_frame = distancia_total / self.speed

        # Mover el enemigo en la dirección aleatoria
        self.x += movimiento_por_frame * dx
        self.y += movimiento_por_frame * dy

        # Cambiar de dirección aleatoria
        self.direccion = random.randint(0, 3)




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