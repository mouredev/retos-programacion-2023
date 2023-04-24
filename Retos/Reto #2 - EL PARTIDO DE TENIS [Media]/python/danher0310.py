
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
#  *   Deuce
#  *   Ventaja P1
#  *   Ha ganado el P1
#  * - Si quieres, puedes controlar errores en la entrada de datos.   
#  * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
#  */

def point_for():
  point = input("Introduce quien anoto el punto: ")
  point = point.lower()
  if (point == "p1") or (point == "p2"):
    return point
  else:    
    print("Disculpa comando no valido vuelve a intentar ") 
    return point_for()
  
p1 = 0
p2 = 0

def game():
  
  p1 = 0  
  p2 = 0
  game = ['Love','15','30','40']  
  winner = False
  
  while( winner != True):    
    
    point = point_for()
    if point == "p1":
      p1 += 1
    
    elif point == "p2":
      p2 += 1

    if p1 >= 3 and p2 >=3:
      if abs(p1 - p2) <= 1:        
        print("Deuce" if(p1 == p2) else 
              "Ventaja P1" if p1 > p2 else "Ventaja P2")
      else:
        winner = True
        msj = ("Ha ganado el P1" if(p1>p2) else "Ha Ganado el P2")
    
    else:
      if p1 < 4 and p2 < 4:
        print(f"{game[p1]} - {game[p2]}")
      else:
         winner = True
         msj = ("Ha ganado el P1" if(p1>p2) else "Ha Ganado el P2")
      
    
  return msj
  
print(game())

    
