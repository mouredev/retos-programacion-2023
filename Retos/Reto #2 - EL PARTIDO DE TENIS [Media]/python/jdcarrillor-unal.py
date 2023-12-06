''' 
  Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
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
def tenis_game(game_array):
  player1 = "P1"
  player2 = "P2"
  p1_puntos = 0
  p2_puntos = 0
  juego = ["Love", "15", "30", "40"]
  finished = False
  print(f'{player1} | {player2}')
  while(not finished):
    for point in game_array:
      if(point == player1):
        p1_puntos +=  1 
      else:
        p2_puntos +=  1   
      if(p1_puntos >= len(juego) -1  and p2_puntos >= len(juego) -1 ):
        if(abs(p1_puntos - p2_puntos ) <= 1):
          if(p1_puntos == p2_puntos):
            print("Deuce")
          elif(p1_puntos > p2_puntos):
            print(f'Ventaja {player1}')
          else:
            print(f'Ventaja {player2}')
        else:
          if(p1_puntos > p2_puntos):
            print(f'Ha ganado {player1}')
          else:
            print(f'Ha ganado {player2}')
          finished = True           
      else:
        if(p1_puntos < 4 and p2_puntos < 4):
          print(f'{juego[p1_puntos]} | {juego[p2_puntos]}')
        else:
          if(p1_puntos > p2_puntos):
            print(f'Ha ganado {player1}')
          else:
            print(f'Ha ganado {player2}')
          finished = True 


tenis_game(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"])
tenis_game(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2","P2","P1","P1","P1"])