
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
  winner = False
  while( winner != True):
    point = point_for()
    if point == "p1":
      p1 += 1
      if(p1 == 1 and p2 ==0):
        print("15 - Love")
      elif(p1 == 2 and p2 == 0):
        print("30 - Love")
      elif(p1 == 3 and p2 ==0):
        print("40 - Love") 
      elif(p1 == 4 and p2 == 0):
        print("Set - Love")
        msj = "El ganador es el P1"
        winner = True
        
      elif(p1 == 1 and p2 == 1):
        print("15 - 15")
      elif(p1 == 2 and p2 == 1):
        print("30 - 15")
      elif(p1 == 3 and p2 == 1):
        print("40 - 15") 
      elif(p1 == 4 and p2 == 1):
        print("Set - 15")
        msj = "El ganador es el P1"
        winner = True
      
      elif(p1 == 1 and p2 == 2):
        print("15 - 30")
      elif(p1 == 2 and p2 == 2):
        print("30 - 30")
      elif(p1 == 3 and p2 == 2):
        print("40 - 30") 
      elif(p1 == 4 and p2 == 2):
        print("Set - 30")
        msj = "El ganador es el P1"
        winner = True
        
      elif(p1 == 1 and p2 == 3):
        print("15 - 40")
      elif(p1 == 2 and p2 == 3):
        print("30 - 40")
      elif(p1 >= 3 and p2 >=3):
        if(p1 == p2):
          print("Deuce - Deuce")     
        elif((p1-p2) == 1):          
          print("Ventaja a P1")
        elif((p1-p2) == 2):          
          msj = "El ganador es el P1"
          winner = True
       
      
      
      
    elif point == "p2":
      p2 += 1 
      if(p2 == 1 and p1 ==0):
        print("Love - 15")
      elif(p2 == 2 and p1 == 0):
        print("Love - 30")
      elif(p2 == 3 and p1 ==0):
        print("Love - 40") 
      elif(p2 == 4 and p1 == 0):
        print("Love - Set")
        msj = "El ganador es el P2"
        winner = True
        
      elif(p2 == 1 and p1 == 1):
        print("15 - 15")
      elif(p2 == 2 and p1 == 1):
        print("15 - 30")
      elif(p2 == 3 and p1 == 1):
        print("15 - 40") 
      elif(p2 == 4 and p1 == 1):
        print("15 - Set")
        msj = "El ganador es el P2"
        winner = True
      
      elif(p2 == 1 and p1 == 2):
        print("30 - 15")
      elif(p2 == 2 and p1 == 2):
        print("30 - 30")
      elif(p2 == 3 and p1 == 2):
        print("30 - 40") 
      elif(p2 == 4 and p1 == 2):
        print("30 - Set")
        msj = "El ganador es el P2"
        winner = True
        
      elif(p2 == 1 and p1 == 3):
        print("40 - 15")
      elif(p2 == 2 and p1 == 3):
        print("40 - 30")
      elif(p1 >= 3 and p2 >=3):
        if(p1 == p2):
          print("Deuce - Deuce")     
        elif((p2-p1) == 1):
          print("Ventaja P2")
        elif((p2-p1) == 2):
          
          msj = "El ganador es el P2"
          winner = True
      
    
  return msj
  
print(game())

    
