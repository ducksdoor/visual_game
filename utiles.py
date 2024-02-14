def dividir_en_lineas(frase, agregar_prefijo=True):
    palabras = frase.split()  # Dividir la frase en palabras
    lineas = []
    linea_actual = ""
    for palabra in palabras:
        if len(linea_actual) + len(palabra) + 1 <= 30:  # Comprobar si la palabra cabe en la línea actual
            if linea_actual:  # Agregar un espacio si no es la primera palabra de la línea
                linea_actual += " "
            linea_actual += palabra
        else:
            lineas.append(linea_actual)  # Agregar la línea actual a la lista de líneas
            linea_actual = palabra  # Empezar una nueva línea con la palabra actual
    if linea_actual:  # Agregar la última línea si no está vacía
        lineas.append(linea_actual)

    # Agregar el prefijo si es necesario
    if agregar_prefijo and lineas:
        lineas[0] = "Has dicho: " + lineas[0]

    return lineas

