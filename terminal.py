    

def terminal(window, pergamino, limite_derecha, terminal_text, font):
    window.blit(pergamino, (limite_derecha, 0))  # Dibujar el pergamino en la sección gris
    # Dibujar texto en la terminal
    # Este text_y es la altura
    text_y = 150
    for line, color in terminal_text:
        text_surface = font.render(line, True, color)
        window.blit(text_surface, (limite_derecha + 150, text_y))
        text_y += font.get_height()
