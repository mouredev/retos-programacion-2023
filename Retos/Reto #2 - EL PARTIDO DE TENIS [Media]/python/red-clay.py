# /*
#  * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
#  * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
#  * gane cada punto del juego.
#  * 
#  * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
#  * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
#  *   15 - Love
#  *   30 - Love
#  *   30 - 15
#  *   30 - 30
#  *   40 - 30 
#  *   Deuce    [3] 40 == [3] 40
#  *   Ventaja P1   [4] < [3]
#  *   Ha ganado el P1  if not [4]<[3] and 
#  * - Si quieres, puedes controlar errores en la entrada de datos.   
#  * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
#  */

def tenismatchresolver(Secuencia):
    points1=0
    points2=0
    NormalGame=["Love", "15", "30", "40"]   
    for player in Secuencia:
        
        if player == "P1":
            points1+=1

        elif player =="P2":
            points2+=1

        if points1>=4 and (points1-points2) >= 2:
            print("Ha ganado P1")
            break
        elif points2>=4 and (points2-points1) >= 2:
            print("Ha ganado P2")
            break
        elif points2>=4 and (points2-points1) == 1:
            print("Ventaja P2")
        elif points1>=4 and (points1-points2) == 1:
            print("Ventaja P1")
        elif points1>=3 and (points1-points2) == 0:
            print("Deuce")
        elif points1<=3 and points2<=3:
            print(f"{NormalGame[points1]} - {NormalGame[points2]}")
def main():
    Secuencia=["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
    Secuencia2=["P1", "P2", "P2", "P2", "P1", "P2", "P1", "P1"]
    Secuencia3=["P1", "P1", "P1", "P2", "P1", "P1"]
    Secuencia4=["P2", "P1","P2", "P1","P2", "P1","P2", "P1", "P2", "P1", "P1", "P2", "P1", "P1"]
    tenismatchresolver(Secuencia)
    print("-"*40)
    tenismatchresolver(Secuencia2)
    print("-"*40)
    tenismatchresolver(Secuencia3)
    print("-"*40)
    tenismatchresolver(Secuencia4)

if __name__=="__main__":
    main()