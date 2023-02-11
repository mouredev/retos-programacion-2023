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
"""Tijera corta a papel, papel tapa a piedra, piedra aplasta a lagarto, lagarto envenena a Spock,
 Spock rompe a tijera, tijera decapita a lagarto, lagarto devora a papel, papel desautoriza a Spock,
  Spock vaporiza a piedra, y como siempre, piedra aplasta a tijera"""

# Añado los enfrentamientos posibles con sus inicales. Primero iría la inciial que está delante en orden alfabético que su enfrentamiento.
enfrentamientos = {"PaT": "T", "PaPi": "Pa", "LPi": "Pi", "LS": "L", "ST": "S",
                   "LT": "T", "LPa": "L", "PaS": "Pa", "PiS": "S", "PiT": "Pi"}
cambiostring = {"🗿": "Pi", "📄": "Pa", "✂️": "T", "🦎": "L", "🖖": "S"}


def juego(var):  # Esta funcion recibe una lista de 2 strings, la ordena y returna el ganador del enfrentamiento
    var.sort()
    a = "".join(var)
    return enfrentamientos[a]


# Esta funcion recibe la entrada de los emojis y returna en string para poder operar luego.
def pasar_a_string(var):
    b, aux = [], []
    for i in range(len(var)):
        for j in range(2):
            aux.append(cambiostring[var[i][j]])
        b.append(aux)
        aux = []
    return b


# Recibe la entrada, la pasa a string y por cada enfrentamiento suma o player1 o player2, finalmente calcula cual tiene mas.
def juegofinal(entrada):
    entrada = pasar_a_string(entrada)
    player1, player2 = 0, 0
    for i in range(len(entrada)):
        var = entrada[i][:]
        player1 += 1 if entrada[i][0] == juego(var) else 0
        player2 += 1 if entrada[i][1] == juego(var) else 0
    if player1 > player2:
        print("player1")
    elif player2 < player1:
        print("player2")
    else:
        print("tie")


juegofinal([("🗿", "✂️"), ("✂️", "🗿"), ("🗿", "✂️")])
