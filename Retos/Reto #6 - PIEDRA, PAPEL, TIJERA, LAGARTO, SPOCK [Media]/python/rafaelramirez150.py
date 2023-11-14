'''
/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */
 '''

def get_winner(player1, player2):
    if player1 == player2:
        return "Empate"
    elif (
        (player1 == "piedra" and (player2 == "tijera" or player2 == "lagarto")) or
        (player1 == "papel" and (player2 == "piedra" or player2 == "spock")) or
        (player1 == "tijera" and (player2 == "papel" or player2 == "lagarto")) or
        (player1 == "lagarto" and (player2 == "papel" or player2 == "spock")) or
        (player1 == "spock" and (player2 == "piedra" or player2 == "tijera"))
    ):
        return "Player 1"
    else:
        return "Player 2"

def play_game():
    scores = {"Player 1": 0, "Player 2": 0}

    while True:
        player1 = input("Player 1 - Elige: piedra, papel, tijera, lagarto o spock: ").lower()
        player2 = input("Player 2 - Elige: piedra, papel, tijera, lagarto o spock: ").lower()

        if player1 not in ["piedra", "papel", "tijera", "lagarto", "spock"] or player2 not in ["piedra", "papel", "tijera", "lagarto", "spock"]:
            print("Opción inválida. Intenta de nuevo.")
            continue

        winner = get_winner(player1, player2)
        if winner == "Empate":
            print("¡Empate en la partida!")
        else:
            scores[winner] += 1
            print("¡", winner, "gana la partida!")

        play_again = input("¿Quieren jugar de nuevo? (S/N): ").lower()
        if play_again != "s":
            break

    print("Puntuación final:")
    for player, score in scores.items():
        print(player, "-", score, "partidas ganadas")

    if scores["Player 1"] > scores["Player 2"]:
        print("¡Player 1 gana más partidas!")
    elif scores["Player 2"] > scores["Player 1"]:
        print("¡Player 2 gana más partidas!")
    else:
        print("Empate en el número de partidas ganadas.")

play_game()
