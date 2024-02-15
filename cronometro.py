import time

def mostrar_cronometro(font, window, tiempo_inicio):
    # Obtener el tiempo actual
    tiempo_actual = time.time()

    # Calcular el tiempo transcurrido
    tiempo_transcurrido = tiempo_actual - tiempo_inicio

    # Convertir el tiempo transcurrido a minutos y segundos
    minutos = int(tiempo_transcurrido // 60)
    segundos = int(tiempo_transcurrido % 60)

    # Formatear el tiempo transcurrido como una cadena de texto
    tiempo_transcurrido_str = f"{minutos:02d}:{segundos:02d}"

    # Dibujar el tiempo transcurrido en la ventana
    texto_tiempo = font.render(f"Tiempo transcurrido: {tiempo_transcurrido_str}", True, (255, 255, 255))
    window.blit(texto_tiempo, (10, 10))