import pygame
import tutorial

def mostrar_ventana_inicial(window):

    screen_info = pygame.display.Info()
    WIDTH, HEIGHT = screen_info.current_w, screen_info.current_h
    font = pygame.font.Font(None, 36)
    BLACK = (0, 0, 0)
    fondo = pygame.image.load("imagen/fondo.jpg").convert()  # Cargar la imagen de fondo
    fondo = pygame.transform.scale(fondo, (WIDTH, HEIGHT))  # Escalar la imagen al tamaño de la ventana
    show_tutorial = False
    init_run = True
    while init_run:
        window.blit(fondo, (0, 0))  # Dibujar el fondo en la ventana
        mensaje = font.render("Para empezar a jugar, pulsa Enter", True, BLACK)
        window.blit(mensaje, (WIDTH // 2 - mensaje.get_width() // 2, HEIGHT // 2 - mensaje.get_height() // 2))
        mensaje_p = font.render("Si pulsas 'P', entra al tutorial", True, BLACK)
        window.blit(mensaje_p, (WIDTH // 2 - mensaje_p.get_width() // 2, HEIGHT // 2 + mensaje.get_height() // 2 + 20))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                init_run = False
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    init_run = False
                    return True
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_p:
                    show_tutorial = True
                    return tutorial.tutorial(show_tutorial, window)

