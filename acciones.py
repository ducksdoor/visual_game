import mision
import utiles

"""lista de comandos 
"tp", te teletransporta. 
"ayuda", te da información sobre comandos.
"limpiar", creo que es demasiado largo para mi gusto, solo limpia cuando esto podria ser un boton...
("atq", "atk"), quita uno de vida, a esto se le podia añadir ataque o atack para que quite mas ... 
"mision", te da información sobre la mision .
"""



def accion_ayuda(terminal_text):

    terminal_text.append("Tienes la siguiente lista de comandos :")
    terminal_text.append("limpiar: borra todo los escrito.")
    terminal_text.append("tp: teletransportate.")
    terminal_text.append("atq/atk: golpea al enemigo")
    return (terminal_text)

def comandos(Jugador, Enemigo, user_input, terminal_text):
    if user_input == "ayuda":
        terminal_text = []
        terminal_text= accion_ayuda(terminal_text)
        if Jugador.mision == 1:
            mision.mision(Jugador, terminal_text)
    elif user_input == "limpiar":
        terminal_text = []
    elif user_input == "tp":
        Jugador.x, Jugador.y = Jugador.move_square_random()
    elif user_input in ["atq", "atk"]:
        if Enemigo is not None:
            Enemigo.recibir_danio()
        else:
            terminal_text.append("Actualmente no hay enemigo")
    elif user_input == "mision":
        mision.mision(Jugador, terminal_text)
    else:
        # Dividir el texto en líneas de máximo 30 caracteres
        lines = utiles.dividir_en_lineas(user_input, agregar_prefijo=True)
        terminal_text.extend(lines)  # Agregar las líneas a la terminal
    return terminal_text