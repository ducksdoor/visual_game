import pygame
import escenario
from variables_color import *

# Inicializar Pygame
pygame.init()

# Definir las variables globales
clock = pygame.time.Clock()
screen_info = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = screen_info.current_w, screen_info.current_h
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Juego RPG de Combate")
limite_derecha = SCREEN_WIDTH * 2 // 3
# Calcular 3/4 partes de la altura de la ventana
three_fourth_height = SCREEN_HEIGHT * 3 // 4


#Carga las imagenes de turno
fondo = escenario.escenario_combate(limite_derecha, SCREEN_HEIGHT)
pergamino = escenario.pergamino_texto(limite_derecha, SCREEN_HEIGHT, SCREEN_WIDTH)
#############################################################
font = pygame.font.Font(None, 26)
# Texto ingresado por el usuario
user_input = ''
user_font = pygame.font.Font(None, 30)
user_input_rect = pygame.Rect(limite_derecha + 100, SCREEN_HEIGHT//2 + 100, 400, 40)

input_color = BLUE