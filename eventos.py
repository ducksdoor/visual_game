import pygame
import acciones
import sys
class TerminalEnvio:
    def __init__(self, user_input_rect, send_area_rect):
        self.user_input_rect = user_input_rect
        self.send_area_rect = send_area_rect
        self.user_input = ''
        self.terminal_text = []
        self.text_input_mode = False



def control_eventos(self, jugador, enemigo):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Obtener las coordenadas del clic del mouse
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Verificar si el clic del mouse está dentro del área de entrada de texto
            if self.user_input_rect.collidepoint(mouse_x, mouse_y):
                self.text_input_mode = True  # Cambiar al modo diae entrada de texto
            # Verificar si el clic del mouse está dentro del área de envío de texto
            elif self.send_area_rect.collidepoint(mouse_x, mouse_y):
                if self.user_input:  # Verificar si el usuario ha ingresado texto
                    self.termianl_text = acciones.comandos(jugador, enemigo, self.user_input, self.terminal_text)
                    self.user_input = ''  # Reiniciar el texto de entrada del usuario
                self.text_input_mode = False  # Cambiar al modo de movimiento del cuadrado
            elif not self.user_input_rect.collidepoint(mouse_x, mouse_y):  # Verificar si el clic está fuera del área de entrada de texto
                self.text_input_mode = False  # Desactivar el modo de entrada de texto
            # esta parte siempre trae problemas, no hay que eliminarla ni bloquearla con otros ifs...
            if jugador.x < mouse_x < jugador.x + jugador.size and jugador.y < mouse_y < jugador.y + jugador.size:
                jugador.cambiar_color()

        # Manejar eventos de teclado si estamos en modo de entrada de texto
        if event.type == pygame.KEYDOWN and self.text_input_mode:
            if event.key == pygame.K_RETURN:
                if self.user_input:  # Verificar si el usuario ha ingresado texto
                    self.terminal_text = acciones.comandos(jugador, enemigo, self.user_input, self.terminal_text)
                    self.user_input = ''  # Reiniciar el texto de entrada del usuario
                elif event.key == pygame.K_BACKSPACE:
                    self.user_input = self.user_input[:-1]
                elif event.key == pygame.K_ESCAPE:
                    self.user_input = ''
                else:
                    self.user_input += event.unicode
            pass
