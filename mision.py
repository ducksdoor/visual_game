VERDE =(0, 255, 0)




def mision(jugador, terminal_text):
    if jugador.mision == 1:
        terminal_text.append("Lo primero sera vencer a tu enemigo")
        terminal_text.append("Usa el comando atq/atk")
        jugador.mision += 1
        return