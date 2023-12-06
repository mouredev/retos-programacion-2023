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
#Mismo metodo resuelto mediante las combinaciones ganadoras
def winner_of(partidas):
    player1 = 0
    player2 = 0
    combinaciones_ganadoras = (
        ["🖖","✂️"],
        ["🖖","🗿"],
        ["✂️","📄"],
        ["✂️","🦎"],
        ["📄","🖖"],
        ["📄","🗿"],
        ["🗿","🦎"],
        ["🗿","✂️"],
        ["🦎","📄"],
        ["🦎","🖖"]
    )
    for partida in partidas:
        if (partida[0] == partida[1]):
            player1 += 1
            player2 += 1
        elif partida in combinaciones_ganadoras:
            player1 += 1
        else:
            player2 += 1
    
    if player1 == player2:
        print('Tie')
    elif player1 < player2:
        print('Player 2')
    elif player1 > player2:
        print('Player 1')

#Ejercicio resuelto mediante Match case ya que la mayoria son con combinaciones de listas
def winner_of_match_case(partidas):
    player1 = 0
    player2 = 0

    for partida in partidas:
        match partida[0]:
            case "✂️":
                match partida[1]:
                    case "✂️":
                        player1 += 1
                        player2 += 1
                    case "📄":
                        player1 += 1
                    case "🖖":
                        player2 += 1
                    case "🗿":
                        player2 += 1
                    case "🦎":
                        player1 += 1
            case "📄":
                match partida[1]:
                    case "✂️":
                        player2 += 1
                    case "📄":
                        player1 += 1
                        player2 += 1
                    case "🖖":
                        player1 += 1
                    case "🗿":
                        player1 += 1
                    case "🦎":
                        player2 += 1
            case "🗿":
                match partida[1]:
                    case "✂️":
                        player1 += 1
                    case "📄":
                        player2 += 1
                    case "🖖":
                        player2 += 1
                    case "🗿":
                        player1 += 1
                        player2 += 1
                    case "🦎":
                        player1 += 1
            case "🦎":
                match partida[1]:
                    case "✂️":
                        player2 += 1
                    case "📄":
                        player1 += 1
                    case "🖖":
                        player1 += 1
                    case "🗿":
                        player2 += 1
                    case "🦎":
                        player1 += 1
                        player2 += 1
            case "🖖":
                match partida[1]:
                    case "✂️":
                        player1 += 1
                    case "📄":
                        player2 += 1
                    case "🖖":
                        player1 += 1
                        player2 += 1
                    case "🗿":
                        player1 += 1
                    case "🦎":
                        player2 += 1
        
    if player1 == player2:
        print('Tie')
    elif player1 < player2:
        print('Player 2')
    elif player1 > player2:
        print('Player 1')



print('\nPruebas mediante match case')
winner_of_match_case([["🗿","✂️"], ["✂️","🗿"], ["📄","✂️"]])   # Player 2
winner_of_match_case([["🗿","✂️"], ["📄","✂️"]])               # Tie
winner_of_match_case([["🗿","🗿"], ["✂️", "📄"]])             # Player 1
winner_of_match_case([["🦎","✂️"], ["🖖","🗿"], ["🖖","✂️"]])  # Player 1


print('\nPruebas mediante combinaciones')
winner_of([["🗿","✂️"], ["✂️","🗿"], ["📄","✂️"]])   # Player 2
winner_of([["🗿","✂️"], ["📄","✂️"]])               # Tie
winner_of([["🗿","🗿"], ["✂️", "📄"]])             # Player 1
winner_of([["🦎","✂️"], ["🖖","🗿"], ["🖖","✂️"]])  # Player 1