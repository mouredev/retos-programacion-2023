#Reto #2 - EL PARTIDO DE TENIS

"""
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love              1 - 0
 *   30 - Love              2 - 0
 *   30 - 15                2 - 1
 *   30 - 30                2 - 2
 *   40 - 30                3 - 2
 *   Deuce                  3 - 3
 *   Ventaja P1             4 - 3
 *   Ha ganado el P1        5 - 3
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 """

points = {0:"love",1:15, 2:30, 3:40, 4:"Ventaja", 5:"Ha Ganado"}

def tenis_scores(scores: list) -> str:
  P1, P2 = [], []
  for i in range(len(scores)):
    if i == 0:
      if scores[i] == "P1":
        P1.append(1)
        P2.append(0)
      else:
        P1.append(0)
        P2.append(1)
    else:
      if scores[i] == "P1":
        P1.append(P1[i-1] + 1)
        P2.append(P2[i-1])
      else:
        P1.append(P1[i-1])
        P2.append(P2[i-1] + 1)
 
  return(result_pretty(P1, P2))

def result_pretty(P1_scores: list, P2_scores: list) -> list:
  result = ["P1 - P2"]
  for i in range(len(P1_scores)):
    if points.get(P1_scores[i]) == 40 and points.get(P2_scores[i]) == 40:
        result.append("Deuce")
        continue
    result.append(str(points.get(P1_scores[i])) + " - " + str(points.get(P2_scores[i])))          
  
  return '\n'.join(result)      


if __name__ == "__main__":
    print(tenis_scores(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]))

    # print(tenis_scores(["P2", "P2", "P1", "P1", "P2", "P1", "P2", "P2"]))
