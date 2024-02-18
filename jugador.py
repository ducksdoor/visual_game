import pygame
import random
import os

BLACK = (0, 0, 0)
WIDTH, HEIGHT = 1000, 600
MAX_X = WIDTH * 2 // 3

# Lista de nombres de archivos de imágenes
lista_imagenes = ["imagen/personajes/heroe1rubio.png", "imagen/personajes/heroe2rubio.png", "imagen/personajes/heroe3rubio.png", 
                    "imagen/personajes/heroe4rubio.png", "imagen/personajes/heroe5rubio.png", "imagen/personajes/heroe6rubio.png", 
                    "imagen/personajes/heroe7rubio.png", "imagen/personajes/heroe8rubio.png", "imagen/personajes/heroe9rubio.png", 
                    "imagen/personajes/heroe10rubio.png", "imagen/personajes/heroina1.png", "imagen/personajes/heroina2.png", 
                    "imagen/personajes/heroina3.png", "imagen/personajes/heroina4.png", "imagen/personajes/heroina5.png", 
                    "imagen/personajes/heroina6.png", "imagen/personajes/heroina7.png", "imagen/personajes/heroina8.png", 
                    "imagen/personajes/heroina9.png", "imagen/personajes/heroina10.png"]

class Jugador:
    def __init__(self, x, y, size=50, speed=5):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.color = BLACK
        self.vida = 5
        self.mision = 1


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

    def cambiar_imagen(self):
        imagen_aleatoria = random.choice(lista_imagenes)
        # Cargar la imagen desde la carpeta "imagenes" usando el nombre aleatorio
        self.image = pygame.image.load(imagen_aleatoria).convert_alpha()  # No es necesario usar os.path.join
        