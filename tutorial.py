import pygame
from variables_color import *
from variables_globales import *

def tutorial(show_tutorial, window):
    WIDTH, HEIGHT =  window.get_size()
    font = pygame.font.Font(None, 36)

    while show_tutorial:
        window.blit(fondo, (0, 0))  # Dibujar el fondo del tutorial en la ventana
        mensaje = font.render("Tutorial: Pulsa Esc para salir del tutorial", True, NEGRO)
        window.blit(mensaje, (WIDTH // 2 - mensaje.get_width() // 2, HEIGHT // 2 - mensaje.get_height() // 2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                show_tutorial = False
                return (False)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    show_tutorial = False
                    return (True)