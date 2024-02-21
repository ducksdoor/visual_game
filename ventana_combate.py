from imports import *
from variables_globales import *

def todo_visual(window, cronometro, font, tiempo_inicio, jugador, terminal_text, send_area_rect,):
    # Dibujar la ventana
    window.blit(fondo, (0, 0))  # Dibujar el fondo en la sección azul
    # Dibujar el cronómetro
    cronometro.mostrar_cronometro(font, window, tiempo_inicio)
    # Dibujar al jugador/a
    jugador.dibujar(window)
    terminal.terminal(window, pergamino, limite_derecha, terminal_text, font)

    
    # Dibujar las vidas del jugador 
    vida_length = jugador.vida * 5
    vida_text_surface = font.render(f"Vidas: {jugador.vida}", True, NEGRO)
    window.blit(vida_text_surface, (limite_derecha + 150, three_fourth_height + 60))
    pygame.draw.rect(window, ROJO, (limite_derecha + 150, three_fourth_height + 80, vida_length, 20))

    # Definir el radio del botón circular
    button_radius = 20
    # Dibujar el área para enviar texto como un círculo
    pygame.draw.circle(window, VERDE, (send_area_rect.x + button_radius, send_area_rect.y + button_radius),
                       button_radius)
    # Dibujar el texto "Enviar" en el centro del círculo
    text_surface = user_font.render("Enviar", True, NEGRO)
    text_rect = text_surface.get_rect(center=(send_area_rect.x + button_radius, send_area_rect.y + button_radius))
    window.blit(text_surface, text_rect)