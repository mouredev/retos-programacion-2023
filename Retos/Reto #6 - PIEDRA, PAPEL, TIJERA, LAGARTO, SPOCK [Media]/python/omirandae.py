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
"""Tijera corta a papel, papel tapa a piedra, piedra aplasta a lagarto, lagarto envenena a Spock,
 Spock rompe a tijera, tijera decapita a lagarto, lagarto devora a papel, papel desautoriza a Spock,
  Spock vaporiza a piedra, y como siempre, piedra aplasta a tijera"""


def jugada(array):
    """
    Metodo para sacar la jugada
    """
    prioridades = {
        '🗿': ['🦎', '✂️'],
        '📄': ['🗿', '🖖'],
        '✂️': ['📄', '🦎'],
        '🦎': ['🖖', '📄'],
        '🖖': ['🗿', '✂️'],
    }
    p1 = 0
    p2 = 0
    for i in array:
        if i[0] in prioridades and i[1] in prioridades[i[0]]:
            p1 += 1
        else:
            p2 += 1
    if p1 > p2:
        ret = "Player_1"
    elif p1 < p2:
        ret = "Player_2"
    else:
        ret = "Empate"
    return ret, p1, p2


def pruebas():
    ganador, p1, p2 = jugada([["🗿", "✂️"], ["✂️", "🗿"], ["📄", "✂️"]])
    print("P1 ha ganado {1} y P2 ha ganado {2}. El ganador es: {0}".format(
        ganador, p1, p2))
    ganador, p1, p2 = jugada([["🗿", "✂️"], ["📄", "✂️"]])
    print("P1 ha ganado {1} y P2 ha ganado {2}. El ganador es: {0}".format(
        ganador, p1, p2))
    ganador, p1, p2 = jugada([["🦎", "✂️"], ["🗿", "✂️"], ["🦎", "🖖"]])
    print("P1 ha ganado {1} y P2 ha ganado {2}. El ganador es: {0}".format(
        ganador, p1, p2))


pruebas()
