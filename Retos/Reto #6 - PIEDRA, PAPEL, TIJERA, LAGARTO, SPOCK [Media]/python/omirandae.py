'''
/*
 * Crea un programa que calcule quien gana mΓ‘s partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La funciΓ³n recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "πΏ" (piedra), "π" (papel),
 *   "βοΈ" (tijera), "π¦" (lagarto) o "π" (spock).
 * - Ejemplo. Entrada: [("πΏ","βοΈ"), ("βοΈ","πΏ"), ("π","βοΈ")]. Resultado: "Player 2".
 * - Debes buscar informaciΓ³n sobre cΓ³mo se juega con estas 5 posibilidades.
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
        'πΏ': ['π¦', 'βοΈ'],
        'π': ['πΏ', 'π'],
        'βοΈ': ['π', 'π¦'],
        'π¦': ['π', 'π'],
        'π': ['πΏ', 'βοΈ'],
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
    ganador, p1, p2 = jugada([["πΏ", "βοΈ"], ["βοΈ", "πΏ"], ["π", "βοΈ"]])
    print("P1 ha ganado {1} y P2 ha ganado {2}. El ganador es: {0}".format(
        ganador, p1, p2))
    ganador, p1, p2 = jugada([["πΏ", "βοΈ"], ["π", "βοΈ"]])
    print("P1 ha ganado {1} y P2 ha ganado {2}. El ganador es: {0}".format(
        ganador, p1, p2))
    ganador, p1, p2 = jugada([["π¦", "βοΈ"], ["πΏ", "βοΈ"], ["π¦", "π"]])
    print("P1 ha ganado {1} y P2 ha ganado {2}. El ganador es: {0}".format(
        ganador, p1, p2))


pruebas()
