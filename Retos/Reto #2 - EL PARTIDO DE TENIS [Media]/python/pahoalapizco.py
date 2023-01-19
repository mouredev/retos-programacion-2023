# https://es.wikipedia.org/wiki/Tenis#Puntuaci%C3%B3n

"""
 Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 gane cada punto del juego.
 
 - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
   15 - Love, p1=1, p2=0
   30 - Love, p1=2, p2=0
   30 - 15,   p1=2, p2=1
   30 - 30,   p1=2, p2=2,
   40 - 30,   p1=3, p2=2
   Deuce,     p1=3, p2=3
   Ventaja P1,p1=4, p2=3
   Ha ganado el P1
   
 - Si quieres, puedes controlar errores en la entrada de datos.   
 - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
"""

def tennis_game(players, sequence):
  players.sort()
  game_points = ['Love', '15', '30', '40']
  p1 = players[0]
  p2 = players[1]

  p1_points = 0
  p2_points = 0

  finish = False

  for player in sequence:
    p1_points += 1 if player == p1 else 0
    p2_points += 1 if player == p2 else 0

    if p1_points >= 3 and p2_points >= 3:
      if p1_points - p2_points == 0:
        print('Deuce')
      elif p1_points - p2_points == 1:
        print(f'Ventaja {p1}')
      elif p2_points - p1_points == 1:
        print(f'Ventaja {p2}')
      else:
        if p1_points - p2_points == 2:
          print(f'Ha ganado {p1}')
        elif p2_points - p1_points == 2:
          print(f'Ha ganado {p2}')

        pass
    else:
      if p1_points < 4 and p2_points < 4:
        print(f'{game_points[p1_points]} - {game_points[p2_points]}')
  



if __name__ == "__main__":
  sequence = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2", "P2", "P2"]
  players = list(set(sequence))
  
  tennis_game(players, sequence)