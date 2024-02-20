import mision
import utiles
from variables_color import *


def accion_ayuda(terminal_text):
    # Crea una lista de tuplas con el texto y el color correspondiente
    terminal_text.append(("Tienes la siguiente lista de comandos :", VERDE_OSCURO))
    terminal_text.append(("limpiar:", NEGRO))
    terminal_text.append(("Borra todo los escrito.", VERDE_OSCURO))
    terminal_text.append(("atq/atk:", NEGRO))
    terminal_text.append(("Golpea al enemigo", VERDE_OSCURO))
    return terminal_text


def comandos(Jugador, Enemigo, user_input, terminal_text):
    if user_input == "ayuda":
        terminal_text = accion_ayuda(terminal_text)
        if Jugador.mision == 1:
            mision.mision(Jugador, terminal_text)
    elif user_input == "limpiar":
        terminal_text = []
    elif user_input in ["atq", "atk"]:
        if Enemigo is not None:
            Enemigo.recibir_danio()
        else:
            terminal_text.append(("Actualmente no hay enemigo", VERDE_OSCURO))
    elif user_input == "mision":
        mision.mision(Jugador, terminal_text)
    else:
        # Dividir el texto en líneas de máximo 30 caracteres
        lines = utiles.dividir_en_lineas(user_input, agregar_prefijo=True)
        terminal_text.extend(lines)  # Agregar las líneas a la terminal
    return terminal_text