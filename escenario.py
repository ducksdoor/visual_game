import pygame

def escenario_combate(MAX_X, SCREEN_HEIGHT):
    # Cargar la imagen de fondo
    fondo = pygame.image.load("imagen/fondo.jpg").convert()
    fondo = pygame.transform.scale(fondo, (MAX_X, SCREEN_HEIGHT))  # Escalar la imagen al tamaño de la sección azul
    return fondo

def pergamino_texto(MAX_X, SCREEN_HEIGHT, SCREEN_WIDTH):
    # Cargar la imagen del pergamino para la sección gris
    pergamino = pygame.image.load("imagen/pergamino.jpg").convert()

    # Escalar la imagen al tamaño dado, sin mantener la relación de aspecto original
    pergamino = pygame.transform.scale(pergamino, (MAX_X, SCREEN_HEIGHT))

    return pergamino
