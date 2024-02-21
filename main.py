from imports import *
from variables_globales import *

import pausa

# Instanciar el jugador y enemigo
jugador = Jugador(SCREEN_WIDTH // 3, SCREEN_HEIGHT - 50, SCREEN_WIDTH, SCREEN_HEIGHT)
enemigo = Enemigo(SCREEN_WIDTH // 3, SCREEN_HEIGHT // 3)
# Lista de disparos del enemigo
disparos = []

# Texto en la terminal
terminal_text = []
# Mensaje de bienvenida
terminal_text.append(("¡Bienvenido al juego RPG de Combate!", NEGRO))
terminal_text.append(("Deberias escribir 'ayuda' antes de morir", ROJO))

input_active = False

# Definir las coordenadas y dimensiones del área para enviar texto
send_area_rect = pygame.Rect(limite_derecha + 10, SCREEN_HEIGHT// 2 + 150, 200, 50)
send_area_active = False

# Sacar variables de control
run = inicio.mostrar_ventana_inicial(window)
pausa_activa = False  # Inicializa la pausa como inactiva


# Bucle principal del juego
tiempo_inicio = time.time()
text_input_mode = False  # Estado inicial: modo de movimiento del cuadrado

while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if not pausa_activa:  # Si no estamos en pausa, activa la pausa
                    pausa_activa = True
                    while pausa_activa:
                        botones= pausa.mostrar_menu_pausa(window)
                        for event in pygame.event.get():
                            if event.type == pygame.K_ESCAPE:
                                pausa_activa = False
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                if botones[0].collidepoint(event.pos):  # Si se hace clic en el botón de salir
                                    run = False  # Salir del juego si se elige salir desde el menú de pausa
                                    pausa_activa = False
                                elif botones[1].collidepoint(event.pos):  # Si se hace clic en el botón de volver
                                    pausa_activa = False  # Continuar el juego si se elige volver desde el menú de pausa
                else:
                    pausa_activa = False
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
        jugador.mover(keys, SCREEN_WIDTH, SCREEN_HEIGHT)

    # Generar disparos del enemigo
    if random.randint(0, 100) < 3:
        if enemigo is not None:
            enemigo.disparar(jugador)

    ventana_combate.todo_visual(window, cronometro, font, tiempo_inicio, jugador, terminal_text, send_area_rect)

    # Actualizar la ventana y controlar la tasa de fotogramas
    clock.tick(60)

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

    # Dibujar el área de entrada de texto para el usuario
    pygame.draw.rect(window, input_color if text_input_mode else WHITE, user_input_rect)
    user_text_surface = user_font.render(user_input, True, NEGRO)
    window.blit(user_text_surface, (user_input_rect.x + 5, user_input_rect.y + 5))

    # Actualizar la pantalla
    pygame.display.update()

    # Controlar la velocidad de actualización de la pantalla
    pygame.time.Clock().tick(60)

# Salir del juego
pygame.quit()
sys.exit()
