# Escribe un programa que simule un juego de tenis y determine quién lo ha ganado.
# El programa aceptará una secuencia formada por "P1" (Player 1) o "P2" (Player 2) indicando
# quién gana cada punto del juego.

# Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
# Por ejemplo, con la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostrará:
#   15 - Love
#   30 - Love
#   30 - 15
#   30 - 30
#   40 - 30  
#   Deuce # a partir de aqui se cambia a deuce, y es cuando los dos escores son>= 3 
#   Ventaja P1
#   Ha ganado el P1

# Puedes implementar manejo de errores para la entrada de datos.
# Si tienes dudas sobre las reglas del juego, consulta la documentación correspondiente.

puntuacion = {0: "Love", 1 : "15", 2 : "30",
                3: "40"}
def marcador(sec : list):
    p1_points = 0 
    p2_points = 0 
    p = ["P1", "P2"]
    
    #obtener puntos
    for player in sec:
        p1_points += 1 if player == 'P1' else 0
        p2_points += 1 if player == "P2" else 0
        #print("{} - {}".format(p1_points, p2_points))
        print(diffPuntos(p1_points, p2_points))
        #print("_______________")
    diff = p1_points - p2_points
    print(f"Ha ganado {'P1' if diff > 0 else 'P2'}")
    
#obtiene la direfencia de puntaje y regresa que debe de imprimir con dicho puntaje
def diffPuntos(P1 : int, P2 : int):
    diff = P1 - P2 
    # si es positivo, va ganando P1, else ganando P2
    if(P1 and P2 >= 3) or (P1 >= 4 or P2 >= 4):
        if diff == 0:
            return "Deuce"
        if diff < 0: 
            return "Ventaja P2"
        if diff > 0: 
            return "Ventaja P1"
    else:
        return f"{puntuacion[P1]} - {puntuacion[P2]}"
sec = ["P2", "P2", "P2", "P2", "P1", "P2", "P1", "P1"]
marcador(sec) 
    