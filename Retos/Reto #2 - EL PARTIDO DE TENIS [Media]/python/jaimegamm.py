"""
Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
gane cada punto del juego.

- Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
- Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
15 - Love
30 - Love
30 - 15
30 - 30
40 - 30
Deuce
Ventaja P1
Ha ganado el P1
- Si quieres, puedes controlar errores en la entrada de datos.
- Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
"""

puntuaciones = ["Love", "15", "30", "40"]
jugador_actual = ""

def jugar_tenis(secuencia):
    score_p1 = 0
    score_p2 = 0
    for jugada in secuencia:
        if jugada == "P1":
            score_p1 += 1
        elif jugada == "P2":
            score_p2 += 1
        else:
            print("Error: Entrada inválida")
            return
        
        puntuacion_actual = mostrar_puntuacion(score_p1, score_p2)
        print(puntuacion_actual)

        if "Ha ganado" in puntuacion_actual:
            break

    return
        
def mostrar_puntuacion(score_p1, score_p2):
    if score_p1 == score_p2:
        if score_p1 < 3:
            return f"{puntuaciones[score_p1]} - All"
        else:
            return "Deuce"
    elif score_p1 >= 4 or score_p2 >= 4:
        diff = abs(score_p1 - score_p2)
        if diff == 1:
            return f"Ventaja {jugador_actual}"
        else:
            return f"Ha ganado el {jugador_actual}"
    else:
        return f"{puntuaciones[score_p1]} - {puntuaciones[score_p2]}"
    

# Secuencia de prueba
secuencia_juego = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]

# Iniciar el juego
jugar_tenis(secuencia_juego)