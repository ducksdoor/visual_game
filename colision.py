import math


def verificar_colision_disparo(x1, y1, r1, x2, y2, r2):
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia < r1 + r2
