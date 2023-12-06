"""
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
"""

def main():
    game1 = [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]
    game2 = [("✂️","✂️"), ("✂️","✂️"), ("✂️","✂️")]
    rock_paper_scissors(game1)
    rock_paper_scissors(game2)
    
def rock_paper_scissors(list_games):
    wins_player1 = 0
    wins_player2 = 0
    for play in list_games:
        wins_player1,wins_player2 = check_win(wins_player1,wins_player2,play[0],play[1])
    if wins_player1 > wins_player2:
        print("Gana Player 1")
    elif wins_player1 < wins_player2:
        print("Gana Player 2")
    else:
        print("Empate")
    
def check_win(wins_player1,wins_player2,strplayer1,strplayer2):
    if strplayer1 == strplayer2:
        wins_player1 = wins_player1
        wins_player2 = wins_player2
    else:
        if strplayer1 == "🗿" and (strplayer2 =="🦎" or strplayer2 =="✂️"):
            wins_player1 += 1
        elif strplayer2 == "🗿" and (strplayer1 =="🦎" or strplayer1 =="✂️"):
            wins_player2 += 1
        if strplayer1 == "🦎" and (strplayer2 =="🖖" or strplayer2 =="📄"):
            wins_player1 += 1
        elif strplayer2 == "🦎" and (strplayer1 =="🖖" or strplayer1 =="📄"):
            wins_player2 += 1
        if strplayer1 == "🖖" and (strplayer2 =="✂️" or strplayer2 =="🗿"):
            wins_player1 += 1
        elif strplayer2 == "🖖" and (strplayer1 =="✂️" or strplayer1 =="🗿"):
            wins_player2 += 1
        if strplayer1 == "✂️" and (strplayer2 =="🦎" or strplayer2 =="📄"):
            wins_player1 += 1
        elif strplayer2 == "✂️" and (strplayer1 =="🦎" or strplayer1 =="📄"):
            wins_player2 += 1
        if strplayer1 == "📄" and (strplayer2 =="🖖" or strplayer2 =="🗿"):
            wins_player1 += 1
        elif strplayer2 == "📄" and (strplayer1 =="🖖" or strplayer1 =="🗿"):
            wins_player2 += 1
    return wins_player1,wins_player2

if __name__ == "__main__":
    main()