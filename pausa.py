import pygame
from variables_color import *
from variables_globales import *

# Función para mostrar el menú de pausa
def mostrar_menu_pausa(window):
    # Dibuja el fondo oscuro para resaltar el menú de pausa
    pygame.draw.rect(window, NEGRO, (0, 0, window.get_width(), window.get_height()), 0)
    
    # Dibujar texto del menú de pausa
    texto_pausa = font.render("Juego en pausa", True, BLANCO)
    rect_pausa = texto_pausa.get_rect(center=window.get_rect().center)
    window.blit(texto_pausa, rect_pausa)

    # Dibujar botones del menú de pausa
    botones = botones_pausa(window)

    pygame.display.flip()

    # Devolver la lista de botones
    return botones

# Función para dibujar los botones del menú de pausa
def botones_pausa(window):
    # Cargar imágenes base de los botones con un color de fondo
    imagen_salir_normal = pygame.image.load('imagen/botones/normal.png')
    imagen_volver_normal = pygame.image.load('imagen/botones/normal.png')
    imagen_salir_encima = pygame.image.load('imagen/botones/encima.png')
    imagen_volver_encima = pygame.image.load('imagen/botones/encima.png')

    # Superponer texto en la imagen de fondo para cada botón
    font = pygame.font.Font(None, 24)
    texto_salir = font.render("Salir", True, ROJO)
    texto_volver = font.render("Volver", True, VERDE)

    # Superponer texto en la imagen de fondo
    rect_salir = texto_salir.get_rect(center=(imagen_salir_normal.get_width() // 2, imagen_salir_normal.get_height() // 2))
    imagen_salir_normal.blit(texto_salir, rect_salir)

    rect_volver = texto_volver.get_rect(center=(imagen_volver_normal.get_width() // 2, imagen_volver_normal.get_height() // 2))
    imagen_volver_normal.blit(texto_volver, rect_volver)

    # Obtener la posición del ratón
    mouse_pos = pygame.mouse.get_pos()

    # Verificar si el ratón está sobre los botones y cambiar la imagen correspondiente
    if rect_salir.collidepoint(mouse_pos):
        rect_salir = window.blit(imagen_salir_encima, (window.get_width() // 2 - imagen_salir_encima.get_width() // 2, window.get_height() // 2 + 30))
    else:
        rect_salir = window.blit(imagen_salir_normal, (window.get_width() // 2 - imagen_salir_normal.get_width() // 2, window.get_height() // 2 + 30))

    if rect_volver.collidepoint(mouse_pos):
        rect_volver = window.blit(imagen_volver_encima, (window.get_width() // 2 - imagen_volver_encima.get_width() // 2, window.get_height() // 2 - 120))
    else:
        rect_volver = window.blit(imagen_volver_normal, (window.get_width() // 2 - imagen_volver_normal.get_width() // 2, window.get_height() // 2 - 120))

    # Devolver las coordenadas de los botones
    return [rect_salir, rect_volver]