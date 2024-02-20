from variables_color import *


def mision(jugador, terminal_text):
    if jugador.mision == 1:
        terminal_text.append(("Lo primero sera vencer a tu enemigo", MARRON))
        terminal_text.append(("Usa el comando atq/atk", MARRON))
        jugador.mision += 1
        return