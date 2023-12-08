"""
Write a program that shows how a tennis game is played and who has won it. The program will receive a sequence consisting of "P1" (Player 1) or "P2" (Player 2), depending on who wins each point of the game.
who wins each point of the game.

- The scores of a game are "Love" (zero), 15, 30, 40, "Deuce" (tie),    advantage.

- Given the sequence [P1, P1, P2, P2, P2, P1, P2, P1, P1, P1], the program would display the following:
  15 - Love
  30 - Love
  30 - 15
  30 - 30
  40 - 30
  Deuce
  Advantage P1
  P1 has won
- If you want, you can check for input errors.   
- Consult the rules of the game if you have doubts about the point system.
"""
flagGame1 = True
flagSet = True
pointsP1 = 0
pointsP2 = 0

print("\n----- Enter the results of set -----")

while flagSet == True:
    winner = input("Who is the winner of this game? ")
    #Love - 15
    if winner == "P1" and flagGame1 == True:
        pointsP1 = 15
        flagGame1 = False
        print(f"Player 1: {pointsP1}")
        print(f"Player 2: {pointsP2}")
    elif winner == "P2" and flagGame1 == True:
        pointsP2 = 15
        flagGame1 = False
        print(f"Player 1: {pointsP1}")
        print(f"Player 2: {pointsP2}")        
    #15 - 30
    elif winner == "P1" and pointsP1 == 15:
        pointsP1 = 30
        print(f"Player 1: {pointsP1}")
        print(f"Player 2: {pointsP2}")        
    elif winner == "P2" and pointsP2 == 15:
        pointsP2 = 30
        print(f"Player 1: {pointsP1}")
        print(f"Player 2: {pointsP2}")
    elif winner == "P1" and pointsP1 == 0:
        pointsP1 = 15
        print(f"Player 1: {pointsP1}")
        print(f"Player 2: {pointsP2}")
    elif winner == "P2" and pointsP2 == 0:
        pointsP2 = 15
        print(f"Player 1: {pointsP1}")
        print(f"Player 2: {pointsP2}")
    #30 - 40
    elif winner == "P1" and pointsP1 == 30:
        pointsP1 = 40
        print(f"Player 1: {pointsP1}")
        print(f"Player 2: {pointsP2}")        
    elif winner == "P2" and pointsP2 == 30:
        pointsP2 = 40
        print(f"Player 1: {pointsP1}")
        print(f"Player 2: {pointsP2}")        
    elif winner == "P1" and pointsP1 == 15:
        pointsP1 = 30
        print(f"Player 1: {pointsP1}")
        print(f"Player 2: {pointsP2}")        
    elif winner == "P2" and pointsP2 == 15:
        pointsP2 = 30
        print(f"Player 1: {pointsP1}")
        print(f"Player 2: {pointsP2}")        
    elif winner == "P1" and pointsP1 == 0:
        pointsP1 = 15
        print(f"Player 1: {pointsP1}")
        print(f"Player 2: {pointsP2}")        
    elif winner == "P2" and pointsP1 == 0:
        pointsP2 = 15
        print(f"Player 1: {pointsP1}")
        print(f"Player 2: {pointsP2}")        
    #Score verification
    if pointsP1 == 40 and pointsP2 == 15:
        print("The Winner of this set is Player 1")
        print(f"P1 - {pointsP1}")
        print(f"P2 - {pointsP2}")
        flagSet = False
    elif pointsP2 == 40 and pointsP1 == 15:
        print("The Winner of this set is Player 2")
        print(f"P1 - {pointsP1}")
        print(f"P2 - {pointsP2}")
        flagSet = False
    elif pointsP1 == 30 and pointsP2 == 0:
        print("The Winner of this set is Player 1")
        print(f"P1 - {pointsP1}")
        print(f"P2 - {pointsP2}")
        flagSet = False
    elif pointsP2 == 0 and pointsP1 == 30:
        print("The Winner of this set is Player 2")
        print(f"P1 - {pointsP1}")
        print(f"P2 - {pointsP2}")
        flagSet = False
    elif pointsP1 == 40 and pointsP2 == 40:
        print("Tie")
        print(f"P1 - {pointsP1}")
        print(f"P2 - {pointsP2}")
        pointsP1 = 0
        pointsP2 = 0
