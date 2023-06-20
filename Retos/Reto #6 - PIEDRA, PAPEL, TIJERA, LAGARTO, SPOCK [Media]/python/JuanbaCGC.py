#  * Crea un programa que calcule quien gana más partidas al piedra,
#  * papel, tijera, lagarto, spock.
#  * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
#  * - La función recibe un listado que contiene pares, representando cada jugada.
#  * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
#  *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
#  * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
#  * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.


# All the possible plays in different tuples with the winner in the first element of each tuple
WINNER_PLAYS=[("🗿","✂️"),("🗿","🦎"),("📄","🗿"),("📄","🖖"),("✂️","📄"),("✂️","🦎"),("🦎","🖖"),("🦎","📄"),("🖖","✂️"),("🖖","🗿")]
def play(sequence):
    score_p1 = 0
    score_p2 = 0
    checked = True
    for tuple in eval(sequence):
        if check_choice(tuple[0]) and check_choice(tuple[1]):
            if (tuple[0],tuple[1]) in WINNER_PLAYS:
                score_p1 += 1
            elif tuple[0] != tuple[1]:
                score_p2 += 1
        else:
            print("The sequence entered is incorrect")
            checked = False
    if checked:
        show_winner(score_p1,score_p2)
        
def show_winner(score_p1,score_p2):
    if score_p1 > score_p2:
        print("Player 1")
    elif score_p2 > score_p1:
        print("Player 2")
    else:
        print("Tie")


def check_choice(choice):
    if choice != "🗿" and choice != "📄" and choice != "✂️" and choice != "🦎" and choice != "🖖":
        return False
    return True

sequence = input("Introduce the sequence: ")
play(sequence)