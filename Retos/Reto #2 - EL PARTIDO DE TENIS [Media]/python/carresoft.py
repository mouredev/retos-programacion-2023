import sys

### Reto #2: EL PARTIDO DE TENIS ###
'''
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
 '''
 
# Baseline data
base_scores = ['Love', '15', '30', '40', 'Deuce', 'Advantage']
score = {'P1': 0, 'P2': 0}

# Game data
# This is the score of the last game, the well-known match of the century, between Federer (P1) and Nadal (P2) at Wimbledon in 2008
points_game = ['P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P2', 'P2']

# Control initial data
if not {'P1','P2'} >= frozenset(points_game): 
    print("The input data is incorrect, only P1 and P2 values can exist.")
    sys.exit(1)

# Game progress
print("P1 - P2")
for point in points_game:
    score[point] = score[point] + 1
    pointsP1, pointsP2 = score.get('P1'), score.get('P2')

    #Case of match won
    if (pointsP1 > 3 or pointsP2 > 3) and abs(pointsP1 - pointsP2) >=2:
        print("Game to " + ("P1" if pointsP1 > pointsP2 else "P2"))
        break

    # Reset counter in the event of seconds deuce
    if pointsP1 == pointsP2 == 5: score['P1'], score['P2'] = 4, 4

    # Case of Deuce and Advantage
    if pointsP1 >=3 and pointsP2 >=3:
        print("Advantage P1" if pointsP1 > pointsP2 else ("Advantage P2" if pointsP1 < pointsP2 else "Deuce"))
    # Other cases
    else:
        print(f"{base_scores[pointsP1]} - {base_scores[pointsP2]}")
