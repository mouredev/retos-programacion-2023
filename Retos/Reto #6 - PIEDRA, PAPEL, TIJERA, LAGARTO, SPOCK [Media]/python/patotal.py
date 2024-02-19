import random

print("PIEDRA, PAPEL, TIJERA, LAGARTO ... SPOCK\n")
i = random.choice (["PIEDRA", "PAPEL", "TIJERA", "LAGARTO", "SPOCK"])
j = random.choice (["PIEDRA", "PAPEL", "TIJERA", "LAGARTO", "SPOCK"])

def main(i, j):
    print (f"Player 1 ha sacado {i}")
    print (f"Player 2 ha sacado {j}\n")

    if i == j:
        return "Tie"
    elif i == "PIEDRA" and j == "TIJERA" or i == "PIEDRA" and j == "LAGARTO":
        return "Ha ganado Player 1"
    elif i == "PAPEL" and j == "PIEDRA" or i == "PAPEL" and j == "SPOCK":
        return "Ha ganado Player 1"
    elif i == "TIJERA" and j == "PAPEL" or i == "TIJERA" and j == "LAGARTO":
        return "Ha ganado Player 1"
    elif i == "LAGARTO" and j == "PAPEL" or i == "LAGARTO" and j == "SPOCK":
        return "Ha ganado Player 1"
    elif i == "SPOCK" and j == "PIEDRA" or i == "SPOCK" and j == "TIJERA":
        return "Ha ganado Player 1"
    else:
        return "Ha ganado Player 2"

print(main(i, j))