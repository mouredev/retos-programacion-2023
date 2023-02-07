def game(sequence):
    player1 = 0
    player2 = 0

    combinations = {
        "lagartopapel":  "lagarto",
        "lagartopiedra": "piedra",
        "lagartospock":  "lagarto",
        "lagartotijera": "tijera",
        "papelpiedra":   "papel",
        "papelspock":    "papel",
        "papeltijera":   "tijera",
        "piedraspock":   "spock",
        "piedratijera":  "piedra",
        "spocktijera":   "spock"
    }

    for attempt in sequence:
        key = sorted(attempt)[0] + sorted(attempt)[1]

        if key in combinations:
            if combinations[key] == attempt[0]:
                player1 += 1

            else:
                player2 += 1
    
    return "Tie" if player1 == player2 else "Player 1" if player1 > player2 else "Player 2"


print(game([["spock", "tijera"], ["spock", "papel"], ["piedra", "spock"]]))
