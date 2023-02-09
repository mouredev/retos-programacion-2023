# Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
# El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien gane cada punto del juego.
# 
# -Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
# -Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
#   |15 - Love|
#   |30 - Love|
#   |30 - 15|
#   |30 - 30|
#   |40 - 30|
#   |Deuce|
#   |Ventaja P1|
#   |Ha ganado el P1|
# - Si quieres, puedes controlar errores en la entrada de datos.   
# - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.

def func_punt_tenis(lp):
#    puntos = {0:"Love", 1:"15", 2:"30", 3:"40"} es lo mismo
    puntos = ["Love", "15", "30", "40"]
    j1 = 0
    j2 = 0
    for p in lp:
        if p == "P1":
            j1 += 1
        elif p == "P2":
            j2 += 1
        else:
            print("El numero del player no es correcto, intentelo otra vez")
            return()
        if j1 > (j2 + 1) and j1 > 3:
            print("Ha ganado el P1")
            return()
        elif j2 > (j1 + 1) and j2 > 3:
            print("Ha ganado el P2")
            return()
        elif j1 == j2 and j1 >= 3:
            print("Deuce")
        elif j1 > j2 and j1 > 3:
            print("Ventaja P1")
        elif j1 < j2 and j1 > 3:
            print("Ventaja P2")
        else:
            print(puntos[j1], "-", puntos[j2])

func_punt_tenis(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2", "P2", "P2"])
        
