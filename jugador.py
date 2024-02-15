import pygame
import random
import os

BLACK = (0, 0, 0)
WIDTH, HEIGHT = 1000, 600
MAX_X = WIDTH * 2 // 3

class Jugador:
    def __init__(self, x, y, size=50, speed=5):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.color = BLACK
        self.vida = 5
        self.mision = 1

        # Lista de nombres de archivos de imágenes
        lista_imagenes = ["carpeta/personajes/heroe1rubio.png", "carpeta/personajes/heroe2rubio.png", "carpeta/personajes/heroe3rubio.png", "carpeta/personajes/heroe4rubio.png", "carpeta/personajes/heroe5rubio.png", "carpeta/personajes/heroe6rubio.png", "carpeta/personajes/heroe7rubio.png", "carpeta/personajes/heroe8rubio.png", "carpeta/personajes/heroe9rubio.png", "carpeta/personajes/heroe10rubio.png"]

        # Cargar una imagen aleatoria de la lista
        imagen_aleatoria = random.choice(lista_imagenes)

        # Cargar la imagen desde la carpeta "imagenes" usando el nombre aleatorio
        self.image = pygame.image.load(imagen_aleatoria).convert_alpha()  # No es necesario usar os.path.join
        self.rect = self.image.get_rect()  # Obtener el rectángulo de la imagen
        self.rect.topleft = (x, y)  # Establecer la posición inicial

    def dibujar(self, surface):
        surface.blit(self.image, self.rect)  # Dibujar la imagen del personaje en la posición del rectángulo
        #pygame.draw.rect(surface, self.color, (self.x, self.y, self.size, self.size))

    def recibir_danio(self):
        self.vida -= 1
    def mover(self, keys):
        if keys[pygame.K_a] and self.rect.left > 0:  # Mover hacia la izquierda
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.right < MAX_X:  # Mover hacia la derecha
            self.rect.x += self.speed
        if keys[pygame.K_w] and self.rect.top > 0:  # Mover hacia arriba
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.bottom < HEIGHT:  # Mover hacia abajo
            self.rect.y += self.speed

    def cambiar_color(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def move_square_random(self):
        white_zone_width = WIDTH * 3 // 4 - self.size
        white_zone_height = HEIGHT - self.size

        x = random.randint(0, white_zone_width)
        y = random.randint(0, white_zone_height)

        while x + self.size > white_zone_width or y + self.size > white_zone_height:
            x = random.randint(0, white_zone_width)
            y = random.randint(0, white_zone_height)

        return x, y