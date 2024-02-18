import pygame

def tutorial(show_tutorial):
    WIDTH, HEIGHT = 1000, 600
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.Font(None, 36)
    BLACK = (0, 0, 0)
    fondo = pygame.image.load("imagen/fondo.jpg").convert()  # Cargar la imagen de fondo del tutorial
    fondo = pygame.transform.scale(fondo, (WIDTH, HEIGHT))  # Escalar la imagen al tamaño de la ventana

    while show_tutorial:
        window.blit(fondo, (0, 0))  # Dibujar el fondo del tutorial en la ventana
        mensaje = font.render("Tutorial: Pulsa Esc para salir del tutorial", True, BLACK)
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