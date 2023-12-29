# Reto 2: El partido de tenis

"""Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
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
Si quieres, puedes controlar errores en la entrada de datos.   
Consulta las reglas del juego si tienes dudas sobre el sistema de puntos."""

def tennis_game(points=None):

    # Verificamos que la entrada no sea None o una lista vacía
    if points is None or not points:
        print("Error: Debe proporcionar una lista de puntos")
        return
    
    mapeo_puntos = {0: "Love", 1: "15", 2: "30", 3: "40"}
    puntajes = {"P1" : 0, "P2": 0}

    # Verificamos que la entrada que recibimos es una lista
    if not isinstance(points, list):
        print("Error: La entrada debe ser una lista")
        return
    
    # Comprobamos que los valores que serán incluidos en la lista son P1 y P2
    for point in points:
        if point != "P1" and point != "P2":
            print("Error: Los valores de la lista deben ser P1 o P2")
            return
        
        puntajes[point] += 1
        # Comprobaremos las diferentes condiciones para obtener la victoria e imprimir 

        if puntajes[point] >= 4 and puntajes[point] >= puntajes["P1" if point == "P2" else "P2"] + 2:
            print("Ha ganado el", point)
            break
        elif puntajes["P1"] >= 3 and puntajes["P2"] >= 3 and puntajes["P1"] != puntajes["P2"]:
            print("Ventaja", point)
        elif puntajes["P1"] >= 3 and puntajes["P2"] >= 3 and puntajes["P1"] == puntajes["P2"]:
            print("Deuce")
        else:
            print(f"{mapeo_puntos[puntajes['P1']]} - {mapeo_puntos[puntajes['P2']]}")

tennis_game(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"])