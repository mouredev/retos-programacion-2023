#Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
#El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
#gane cada punto del juego
#Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
#Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
# 15 - Love
# 30 - Love
# 30 - 15
# 30 - 30
# 40 - 30
#Deuce
#Ventaja P1
#Ha ganado el P1
#Si quieres, puedes controlar errores en la entrada de datos.   
#Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   




def tenis_game(juego: list):
    puntos = {0 : "Love", 1 : 15, 2 : 30, 3 : 40}
    pp1 = 0
    pp2 = 0
    for i in juego:
        pp1 += 1 if i == "P1" else 0
        pp2 += 1 if i == "P2" else 0
        if pp1 > 4 and pp1 == pp2 + 1:
            print("Ventaja P1")
        elif pp2 > 4 and pp2 == pp1 + 1:
            print("Ventaja P2")
        if pp1 >= 4 and pp1 >= pp2 + 2 :
            print( "Gano P1")
            quit()
        elif pp2 >= 4 and pp2 >= pp1 + 2 :
            print( "Gano P2")
            quit()
        if pp1 and pp2 <3:
            print(f"{(puntos[pp1])} - {(puntos[pp2])}")




tenis_game(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1", "P2", "P1"])
