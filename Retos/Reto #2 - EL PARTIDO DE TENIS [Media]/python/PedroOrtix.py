PUNTUACIONES = {0: "Love", 1: "15", 2: "30", 3: "40"}

def obtener_puntuacion_str(puntuacion):
    if puntuacion < len(PUNTUACIONES):
        return PUNTUACIONES[puntuacion]
    return "Love"

def estado_resultado(tupla_puntos):
    puntuacion_p1, puntuacion_p2 = tupla_puntos

    if puntuacion_p1 >= 3 and puntuacion_p2 >= 3:
        if puntuacion_p1 == puntuacion_p2:
            return "Deuce", ""
        elif puntuacion_p1 - puntuacion_p2 == 1:
            return "Ventaja", "P1"
        elif puntuacion_p1 - puntuacion_p2 == -1:
            return "Ventaja", "P2"
        elif puntuacion_p1 - puntuacion_p2 >= 2:
            return "Gana", "P1"
        elif puntuacion_p1 - puntuacion_p2 <= -2:
            return "Gana", "P2"

    return obtener_puntuacion_str(puntuacion_p1), obtener_puntuacion_str(puntuacion_p2)

def estado_juego(lista_puntos):
    estado_dinamico = [0, 0]
    for punto in lista_puntos:
        if punto == "P1":
            estado_dinamico[0] += 1
        elif punto == "P2":
            estado_dinamico[1] += 1

        puntuacion_p1_str, puntuacion_p2_str = estado_resultado(estado_dinamico)
        if puntuacion_p1_str == "Gana":
            print("Ha ganado el P1")
            break
        elif puntuacion_p2_str == "Gana":
            print("Ha ganado el P2")
            break
        else:
            print(f"{puntuacion_p1_str} - {puntuacion_p2_str}")

# Probamos el código con la secuencia proporcionada
# [P1, P1, P2, P2, P1, P2, P1, P1]
estado_juego(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1'])
