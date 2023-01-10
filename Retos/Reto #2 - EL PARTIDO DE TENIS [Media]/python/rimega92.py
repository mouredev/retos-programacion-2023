"""
   Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
   El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
   gane cada punto del juego.
   - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
   - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
      15 - Love
      30 - Love
      30 - 15
      30 - 30
      40 - 30
      Deuce
      Ventaja P1
      Ha ganado el P1
   - Si quieres, puedes controlar errores en la entrada de datos.
   - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
"""

def game(gamePoints):
   scores = ["love", "15", "30", "40", "Deuce", "Advantage", "Win"]
   player1Score = 0
   player2Score = 0
   end = True

   # Itera sobre los puntos de la secuencia
   for point in gamePoints:
      # Incrementa la puntuación del jugador que ha ganado el punto
      if (point == "P1"):
         player1Score += 1
      else:
         player2Score += 1

      #Ganador sin usar el deuce
      if(player1Score == 4) and (player2Score <3):
         print("P1 Win")
         end = False
         break
      elif(player2Score == 4) and (player1Score <3):
         print("P2 Win")
         end = False
         break

      # Definición puntos hasta el deuce
      if (player1Score == 3) and (player2Score == 3):
         print("40 - 40 -> Deuce")
      elif (player1Score < 3) or (player2Score < 3):
         print(scores[player1Score] + " " + scores[player2Score])

      #Definición del advantage o volver a deuce
      if (player1Score == 4) and (player2Score < 4):
         print("Advantage P1")
      elif (player2Score == 4) and (player1Score < 4):
         print("Advantage P2")
      elif (player1Score == 4) and (player2Score == 4):
         player1Score = player1Score - 1
         player2Score = player2Score - 1
         print("40 - 40 -> Deuce")

      #Definición de Ganador después de deuce
      if (player1Score == 5):
         print("P1 Win")
         end = False
         break
      elif (player2Score == 5):
         print("P2 Win")
         end = False
         break

   if end:
      print("Faltaron puntos por jugar en el Array entregado")


if __name__ == "__main__":
   gamePoints = ["P1", "P1", "P1", "P1"]
   print("\nPrueba 0: " + str(gamePoints))
   game(gamePoints)

   gamePoints = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
   print("\nPrueba 1: " + str(gamePoints))
   game(gamePoints)

   gamePoints = ["P1", "P2", "P1", "P2", "P1", "P1"]
   print("\nPrueba 2: " + str(gamePoints))
   game(gamePoints)

   gamePoints = ["P1", "P2", "P1", "P2", "P1", "P2", "P1", "P2", "P1", "P1"]
   print("\nPrueba 3: " + str(gamePoints))
   game(gamePoints)

   gamePoints = ["P1", "P2", "P1", "P2", "P1", "P2", "P1", "P2", "P1", "P2", "P2", "P2"]
   print("\nPrueba 4: " + str(gamePoints))
   game(gamePoints)

   gamePoints = ["P1", "P2", "P1"]
   print("\nPrueba 5: " + str(gamePoints))
   game(gamePoints)
