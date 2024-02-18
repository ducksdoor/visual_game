import pygame
import sys
import random
import time
###############archivos

import inicio
from jugador import Jugador
from enemigo import Enemigo
import acciones
import colision
import cronometro
# Inicializar Pygame, ventana de intro, y cronometro

pygame.init()

clock = pygame.time.Clock()
# Definir colores
WHITE = (255, 255, 255)
ROJO = (255, 0, 0)
BLACK = (0, 0, 0)
VERDE = (0, 255, 0)
MARRON = (139, 69, 19)
BLUE = pygame.Color('lightskyblue3')
# Obtener el tamaño de la pantalla del ordenador
screen_info = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = screen_info.current_w, screen_info.current_h

# Configurar la ventana en pantalla completa
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Juego RPG de Combate")

# Limitar la posición máxima del cuadrado a las 2/3 partes izquierdas de la pantalla
MAX_X = SCREEN_WIDTH * 2 // 3

# Instanciar el jugador y enemigo
jugador = Jugador(SCREEN_WIDTH // 3, SCREEN_HEIGHT - 50)
enemigo = Enemigo(SCREEN_WIDTH // 3, SCREEN_HEIGHT // 3)
vida_length = jugador.vida * 5

# Lista de disparos del enemigo
disparos = []

# Texto en la terminal
terminal_text = []
font = pygame.font.Font(None, 24)

# Texto ingresado por el usuario
user_input = ''
user_font = pygame.font.Font(None, 30)
user_input_rect = pygame.Rect(MAX_X + 10, SCREEN_HEIGHT// 2 + 100, 400, 40)
input_color = BLUE
input_active = False

# Definir las coordenadas y dimensiones del área para enviar texto
send_area_rect = pygame.Rect(MAX_X + 10, SCREEN_HEIGHT// 2 + 150, 200, 50)
send_area_color = (0, 255, 0)  # Cambiar a verde
send_area_active = False

# Mensaje de bienvenida
welcome_message = "¡Bienvenido al juego RPG de Combate!"
welcome_index = 0
welcome_display = ""

# Cargar la imagen de fondo
fondo = pygame.image.load("imagen/fondo.jpg").convert()
fondo = pygame.transform.scale(fondo, (MAX_X, SCREEN_HEIGHT))  # Escalar la imagen al tamaño de la sección azul

# Cargar la imagen del pergamino para la sección gris
pergamino = pygame.image.load("imagen/pergamino.jpg").convert()
pergamino = pygame.transform.scale(pergamino, (SCREEN_WIDTH - MAX_X, SCREEN_HEIGHT))  # Escalar la imagen al tamaño de la sección gris



#############################################################

# Bucle principal del juego
run = inicio.mostrar_ventana_inicial()

tiempo_inicio = time.time()
text_input_mode = False  # Estado inicial: modo de movimiento del cuadrado

# Flag para indicar si se ha mostrado el mensaje de bienvenida
welcome_displayed = False

while run:

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Obtener las coordenadas del clic del mouse
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Verificar si el clic del mouse está dentro del área de entrada de texto
            if user_input_rect.collidepoint(mouse_x, mouse_y):
                text_input_mode = True  # Cambiar al modo de entrada de texto
            # Verificar si el clic del mouse está dentro del área de envío de texto
            elif send_area_rect.collidepoint(mouse_x, mouse_y):
                if user_input:  # Verificar si el usuario ha ingresado texto
                    terminal_text = acciones.comandos(jugador, enemigo, user_input, terminal_text)
                    user_input = ''  # Reiniciar el texto de entrada del usuario
                text_input_mode = False  # Cambiar al modo de movimiento de jugador
            elif not user_input_rect.collidepoint(mouse_x, mouse_y):  # Verificar si el clic está fuera del área de entrada de texto
                text_input_mode = False  # Desactivar el modo de entrada de texto
            #esta parte siempre trae problemas, no hay que eliminarla ni bloquearla con otros ifs...
            if jugador.rect.collidepoint(mouse_x, mouse_y):
                jugador.cambiar_imagen()

        # Manejar eventos de teclado si estamos en modo de entrada de texto
        if event.type == pygame.KEYDOWN and text_input_mode:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_RETURN:
                if user_input:  # Verificar si el usuario ha ingresado texto
                    terminal_text = acciones.comandos(jugador, enemigo, user_input, terminal_text)
                    user_input = ''  # Reiniciar el texto de entrada del usuario
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            elif event.key == pygame.K_ESCAPE:
                user_input = ''
            else:
                user_input += event.unicode
            pass

    # Manejar eventos relacionados con el movimiento del cuadrado
    if not text_input_mode:
        keys = pygame.key.get_pressed()
        jugador.mover(keys)

    # Generar disparos del enemigo
    if random.randint(0, 100) < 3:
        if enemigo is not None:
            enemigo.disparar(jugador)

    # Dibujar la ventana
    window.blit(fondo, (0, 0))  # Dibujar el fondo en la sección azul
    # Dibujar el cronómetro
    cronometro.mostrar_cronometro(font, window, tiempo_inicio)

    # Actualizar la ventana y controlar la tasa de fotogramas
    clock.tick(60)
    # Calcular 3/4 partes de la altura de la ventana
    three_fourth_height = SCREEN_HEIGHT * 3 // 4

    # Dibujar al jugadora
    jugador.dibujar(window)

    if enemigo is not None:
        tiempo_actual = time.time()
        enemigo.mover_enemigo(tiempo_actual)
        enemigo.dibujar(window)
        # Dibujar y mover los disparos del enemigo
        for disparo in enemigo.projectiles:
            window.blit(enemigo.projectile_image, (int(disparo['x']), int(disparo['y'])))
            # Mover el disparo en su dirección
            disparo['x'] += disparo['dx']
            disparo['y'] += disparo['dy']
            # Verificar si el disparo ha salido de la pantalla y eliminarlo
            if not (0 <= disparo['x'] <= SCREEN_WIDTH and 0 <= disparo['y'] <= SCREEN_HEIGHT):
                enemigo.projectiles.remove(disparo)
            # Verificar colisión con el jugador
            elif colision.verificar_colision_disparo(jugador.rect.x, jugador.rect.y, jugador.size, disparo['x'], disparo['y'], 5):
                jugador.recibir_danio()
                enemigo.projectiles.remove(disparo)
        enemigo.actualizar_proyectiles()
        # Verificar si el enemigo ha perdido todas sus vidas
        if enemigo.vida <= 0:
            enemigo = None  # Eliminar al enemigo
            print("Enemigo eliminado")


    # Verificar si el jugador ha perdido todas sus vidas
    if jugador.vida <= 0:
        print("Game Over")
        run = False

    window.blit(pergamino, (MAX_X, 0))  # Dibujar el pergamino en la sección gris

    # Dibujar el segundo rectángulo que cubre el cuarto restante de la altura total
    pygame.draw.rect(window, MARRON, (MAX_X, three_fourth_height, SCREEN_WIDTH - MAX_X, SCREEN_HEIGHT - three_fourth_height))

    # Simular escritura del mensaje de bienvenida
    if welcome_index < len(welcome_message):
        welcome_display += welcome_message[welcome_index]
        welcome_index += 1
    elif not welcome_displayed:
        terminal_text.append(welcome_message)
        terminal_text.append("Deberias escribir 'ayuda' antes de morir")
        welcome_displayed = True

    # Dibujar texto en la terminal
    text_y = 60
    for line in terminal_text:
        text_surface = font.render(line, True, BLACK)
        window.blit(text_surface, (MAX_X + 10, text_y))
        text_y += font.get_height()

    # Dibujar las vidas del jugador en la parte marrón de la pantalla
    vida_text_surface = font.render(f"Vidas: {jugador.vida}", True, BLACK)
    window.blit(vida_text_surface, (MAX_X + 10, three_fourth_height + 60))
    pygame.draw.rect(window, ROJO, (MAX_X + 10, three_fourth_height + 80, vida_length, 20))

    # Dibujar el área de entrada de texto para el usuario
    pygame.draw.rect(window, input_color if text_input_mode else WHITE, user_input_rect)
    user_text_surface = user_font.render(user_input, True, BLACK)
    window.blit(user_text_surface, (user_input_rect.x + 5, user_input_rect.y + 5))

    # Definir el radio del botón circular
    button_radius = 20
    # Dibujar el área para enviar texto como un círculo
    pygame.draw.circle(window, VERDE, (send_area_rect.x + button_radius, send_area_rect.y + button_radius),
                       button_radius)
    # Dibujar el texto "Enviar" en el centro del círculo
    text_surface = user_font.render("Enviar", True, BLACK)
    text_rect = text_surface.get_rect(center=(send_area_rect.x + button_radius, send_area_rect.y + button_radius))
    window.blit(text_surface, text_rect)

    # Actualizar la pantalla
    pygame.display.update()

    # Controlar la velocidad de actualización de la pantalla
    pygame.time.Clock().tick(60)

# Salir del juego
pygame.quit()
sys.exit()

