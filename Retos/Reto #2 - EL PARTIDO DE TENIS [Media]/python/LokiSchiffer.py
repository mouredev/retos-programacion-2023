'''
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
'''
#Inicialización de los puntos de juego
points_table = {
  0: "Love", 1: "15", 2: "30", 3: "40"
}

def score(puntos1, puntos2, adv):
  #Comprobación de si alguien ha ganado el juego y envía bandera para terminar
  if (adv == 2):
    print("El jugador 1 ha ganado")
    return True
  elif (adv == -2):
    print("El jugador 2 ha ganado")
    return True
  #Secuencia para mirar quien de los dos tiene la ventaja, si se tiene deuce o se imprimen los puntos
  if(puntos1 == 3 and puntos2 == 3):
    if (adv > 0):
      print("Ventaja P1")
    elif (adv < 0):
      print("ventaja P2")
    else:
      print("Deuce")
  else:
    print(points_table[puntos1],"-",points_table[puntos2])
  return False

def juego_tenis(arr):
  #Inicialización de variables
  jugador1: int = 0
  jugador2: int = 0
  ventaja: int = 0
  #Control de final de juego
  final: bool = False
  for point in arr:
    #Si el juego no ha finalizado sigue contando puntos
    if (not final):
      #Por cada punto se sube el marcador, pero al llegar a 40, se deja de contar
      if (point == "P1" and jugador1 < 3):
        jugador1 += 1
      elif (point == "P2" and jugador2 < 3):
        jugador2 += 1
      #Si los dos jugadores llegan a 40, se pasa a los escenarios de ventaja
      elif (jugador1 == 3 and jugador2 == 3):
        #Cuando el P1 tiene la ventaja se vuelve positivo y si repite, cumple la condición de victoria
        if (point == "P1"):
          ventaja += 1
        #Cuando el P2 tiene la ventaja se vuelve negativo y si repite, cumple la condición de victoria
        else:
          ventaja -= 1
      #Si el P1 ya tiene 40 puntos y el P2 dos no, cuando el P1 gana punto se cumple la condición de victoria
      elif (point == "P1"):
        ventaja += 2
      #Si el P2 ya tiene 40 puntos y el P1 dos no, cuando el P2 gana punto se cumple la condición de victoria
      elif (point == "P2"):
        ventaja -= 2
      #Mensaje cuando un valor no es valido
      else:
        print("Valor ingresado no valido")      
      #Se envía la información de los puntajes al método de impresión
      final = score(jugador1, jugador2, ventaja)
    #Mensaje especial cuando ya se termino el juego, pero siguen ingresando valores
    else:
      print("El juego ya ha terminado")

#Secuencia de datos para enviar
juego_tenis(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2", "P2", "P1", "P1",
             "P1", "P1", "P2", "P2", "P1", "P2", "P2"])