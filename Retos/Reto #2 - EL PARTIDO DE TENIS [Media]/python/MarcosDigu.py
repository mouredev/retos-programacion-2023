import os

os.system('cls')

puntaje = ["0", "15", "30", "40", "Ad"]

P1 = puntaje[0]
P2 = puntaje[0]

game_finished = False

while not game_finished:
    print(f"Score P1: {P1}")
    print(f"Score P2: {P2}")
    print(" ")

    winner = input("Type P1 or P2: ")

    if P1 == "Ad" and P2 == "40" and winner == "P1":
        game_finished = True
    elif P2 == "Ad" and P1 == "40" and winner == "P2":
        game_finished = True
    else:
        index_P1 = puntaje.index(P1)
        index_P2 = puntaje.index(P2)

        if winner == "P1":
            P1 = puntaje[index_P1 + 1]
            if P1 == "Ad" and P2 in ["0", "15", "30"]:
                game_finished = True
        else:
            P2 = puntaje[index_P2 + 1]
            if P2 == "Ad" and P1 in ["0", "15", "30"]:
                game_finished = True

    os.system('cls')

if P1 == "Ad":
    print("Player 1 won")
else:
    print("Player 2 won")
