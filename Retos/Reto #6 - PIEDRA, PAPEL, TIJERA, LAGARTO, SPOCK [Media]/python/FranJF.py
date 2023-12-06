"""
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
"""

COMBINACIONES_GANADORAS = {
    "piedra": ["tijeras", "lagarto"],
    "papel": ["piedra", "spock"],
    "tijeras": ["papel", "lagarto"],
    "lagarto": ["papel", "spock"],
    "spock": ["piedra", "tijeras"]
}

def juego(combinaciones:list):
    puntos_player1:int = 0
    puntos_player2:int = 0

    for combinacion in combinaciones:
        eleccion_player1:str = combinacion[0]
        eleccion_player2:str = combinacion[1]

        if eleccion_player1 not in COMBINACIONES_GANADORAS.keys():
            raise Exception("No existe dicha posibilidad en este juego.")
        if eleccion_player2 not in COMBINACIONES_GANADORAS.keys():
            raise Exception("No existe dicha posibilidad en este juego.")

        if eleccion_player1 != eleccion_player2:
            if eleccion_player2 in COMBINACIONES_GANADORAS[eleccion_player1]:
                puntos_player1 += 1
            else:
                puntos_player2 += 1

    if puntos_player1 > puntos_player2:
        return "Player 1"
    elif puntos_player1 < puntos_player2:
        return "Player 2"
    else:
        return "Tie"


print(juego([("piedra", "papel"), ("spock", "lagarto"), ("tijeras", "piedra")]))
print(juego([("papel", "papel"), ("spock", "spock"), ("tijeras", "tijeras")]))
print(juego([("papel", "papel"), ("spock", "spock"), ("tijeras", "papel")]))
