# -*- coding: utf-8 -*-

# Reto #6: PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK
#
# 
#  * Crea un programa que calcule quien gana más partidas al piedra,
#  * papel, tijera, lagarto, spock.
#  * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
#  * - La función recibe un listado que contiene pares, representando cada jugada.
#  * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
#  *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
#  * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
#  * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
#  */
#  
# *Las tijeras cortan el papel, 
# *el papel cubre a la piedra, 
# *la piedra aplasta al lagarto, 
# *el lagarto envenena a Spock, 
# *Spock destroza las tijeras, 
# *las tijeras decapitan al lagarto, 
# *el lagarto se come el papel, 
# *el papel refuta a Spock, 
# *Spock vaporiza la piedra, y, como es habitual… 
# *la piedra aplasta las tijeras.

RESULTS = {
    0: "Tie",
    1: "Player 1",
    2: "Player 2"
}

OPTIONS = {
    "Rock": [
    "🗿", "piedra", "rock", "roca"
    ],
    "Paper": [
    "📄", "papel", "paper"
    ],
    "Scissors": [
    "✂️", "tijera", "scissors", "tijeras"
    ],
    "Lizard": [
    "🦎", "lagarto", "lizard", "lagartija"
    ],
    "Spock": [
    "🖖", "spock"
    ]
}

RULES = {
    "Rock": [
    "Lizard", "Scissors"
    ],
    "Paper": [
    "Rock", "Spock"
    ],
    "Scissors": [
    "Paper", "Lizard"
    ],
    "Lizard": [
    "Paper", "Spock"
    ],
    "Spock": [
    "Rock", "Scissors"
    ]
}


def valid_option(option: str):
    for k, v in OPTIONS.items():
        if option.lower() in v:
            return k
    return False

def single_play(player1: str, player2: str):
    play1 = valid_option(player1)
    play2 = valid_option(player2)
    if play1 and play2:
        if play1 == play2:
            print(f"{RESULTS[0]}")
            return 0
        elif play2 in RULES[play1]:
            print(RESULTS[1])
            return -1
        else:
            print(RESULTS[2])
            return 1
    else:
        print(f"Invalid option(s): ({player1},{player2}) ")
        return 0

def play(game: str):
    result = 0
    # winner = ""
    plays = game.split(sep=" ")
    for p in plays:
        p = p.replace(" ", "")
        if p and p != "":
            options = p.split(",")
            if len(options) == 2:
                player1 = options[0].replace(" ","")
                player2 = options[1].replace(" ","")
                result += single_play(player1, player2)
            elif len(options) > 2:
                print(f"Too many players: {options}")
            else:
                print(f"Insufficient players: {options}")

    if result < 0:
        winner = RESULTS[1]
    elif result > 0:
        winner = RESULTS[2]
    else:
        winner = RESULTS[0]
    print(f"The winner is: {winner}!!")

if __name__ == "__main__":
    print(f"""Rock, Paper, Scissors, Lizard, Spock:
    - Valid options:
    * Rock: {OPTIONS['Rock']}
    * Paper: {OPTIONS['Paper']}
    * Scissors: {OPTIONS['Scissors']}
    * Lizard: {OPTIONS['Lizard']}
    * Spock: {OPTIONS['Spock']}
    """)
    seq = input("""Enter a sequence with:
    - Games separated by space
    - Players one and two, separated by commas whithout space
    - Example: piedra,papel spock,lagarto papel,papel tijeras,wom gusano,roca 
    \n""")
    play(seq)  

OPTIONS = {
    "Rock": [
    "🗿", "piedra", "rock", "roca"
    ],
    "Paper": [
    "📄", "papel", "paper"
    ],
    "Scissors": [
    "✂️", "tijera", "scissors", "tijeras"
    ],
    "Lizard": [
    "🦎", "lagarto", "lizard", "lagartija"
    ],
    "Spock": [
    "🖖", "spock"
    ]
}