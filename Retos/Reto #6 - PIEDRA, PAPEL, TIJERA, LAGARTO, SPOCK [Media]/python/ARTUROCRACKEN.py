# /*
#  * Crea un programa que calcule quien gana más partidas al piedra,
#  * papel, tijera, lagarto, spock.
#  * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
#  * - La función recibe un listado que contiene pares, representando cada jugada.
#  * - El par puede contener combinaciones de  (piedra), "📄" (papel),
#  *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
#  * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
#  * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
#  */


piedra = "🗿"
papel = "📄"
tijera = "✂️"
lagarto = "🦎"
spock = "🖖"

def wins(p1, p2):
    if p1 == piedra:
        if p2 == lagarto:
            return True
        elif p2 == tijera:
            return True
        else:
            return False
    elif p1 == papel:
        if p2 == piedra:
            return True
        elif p2 == spock:
            return True
        else:
            return False
    elif p1 == tijera:
        if p2 == papel:
            return True
        elif p2 == lagarto:
            return True
        else:
            return False
    elif p1 == lagarto:
        if p2 == papel:
            return True
        elif p2 == spock:
            return True
        else:
            return False
    elif p1 == spock:
        if p2 == piedra:
            return True
        elif p2 == tijera:
            return True
        else:
            return False


def main(arr):
    i = 0
    p1 = 0
    p2 = 0
    while(i < len(arr)):
        
        if arr[i]:
            if wins(arr[i][0], arr[i][1]):
                p1 += 1
            elif arr[i][0] == arr[i][1]:
                p1 += 1
                p2 += 1
            else:
                p2 += 1

        i += 1

    if p1 > p2:
        print('Player 1')
    elif p1 < p2:
        print('Player 2')
    else:
        print('Tie')


game_1 = [(piedra, papel), (spock, piedra), (piedra, papel), (papel, piedra)]
game_2 = [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]
game_3 = [(spock, spock), (piedra, piedra), (papel, papel), (papel, piedra)]
game_4 = [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️"), ("🦎","🖖")]

main(game_1)
main(game_2)
main(game_3)
main(game_4)
