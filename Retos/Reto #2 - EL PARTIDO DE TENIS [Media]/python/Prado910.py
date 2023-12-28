# ---------------------------------------------------------------------------------------------
# Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
# El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
# gane cada punto del juego.
# 
# - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
# - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
#   15 - Love
#   30 - Love
#   30 - 15
#   30 - 30
#   40 - 30
#   Deuce
#   Ventaja P1
#   Ha ganado el P1
# - Si quieres, puedes controlar errores en la entrada de datos.
# - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
# ---------------------------------------------------------------------------------------------

def analizarJuego(juego):
    p1 = 0
    p2 = 0
    
    for punto in juego:
        match punto, p1, p2:
            case "P1", 0 | 15, _:
                p1 += 15
            case "P1", _, _:
                p1 += 10
            case "P2", _, 0 | 15:
                p2 += 15
            case "P2", _, _:
                p2 += 10
        
        if p1 < 50 and p2 < 50:
            match p1, p2:
                case 40, 40:
                    print("Deuce")
                case 0, _:
                    print("Love -", p2)
                case _, 0:
                    print(p1, "- Love")
                case _, _:
                    print(p1, "-", p2)
        else:
            if p1 == p2:
                print("Deuce")
            elif p1 == p2+10:
                print("Ventaja P1")
            elif p2 == p1+10:
                print("Ventaja P2")
            elif p1 == p2+20:
                print("Ha ganado el P1")
                break
            elif p2 == p1+20:
                print("Ha ganado el P2")
                break

juego = ["P2","P2","P2","P1","P1","P1","P1","P2","P2","P2","P2","P2"]
analizarJuego(juego)
