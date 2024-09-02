"""/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */

Reglas:

Las tijeras cortan el papel, el papel envuelve la piedra, la piedra aplasta al lagarto,
el lagarto envenena a Spock, Spock aplasta las tijeras, las tijeras decapitan al lagarto,
el lagarto devora el papel, el papel desaprueba a Spock, Spock desintegra la piedra y, 
como siempre, la piedra aplasta las tijeras.

"""


reglas = {"🗿": ["✂️", "🦎"],
        "📄": ["🗿", "🖖"],
        "✂️": ["📄", "🦎"],
        "🦎": ["🖖", "📄"],
        "🖖": ["🗿", "✂️"]}


def partida(manos:list)->str:
    
    p1,p2=0,0
    
    for mano in manos:
        p1_hand=mano[0]
        p2_hand=mano[1]
        if p1_hand != p2_hand:
            if p1_hand in reglas[p2_hand]:
                p2 += 1
            else:
                p1 += 1
    return 'Empate' if p1 == p2 else 'Ganador -> Jugador 1' if p1 > p2 else 'Ganador -> Jugador 2'  
    

print(partida([("🗿", "✂️")]))
print(partida([("✂️", "🗿")]))
print(partida([("🗿", "🗿"), ("🗿", "🗿"), ("🗿", "🗿"), ("🗿", "🗿")]))
print(partida([("🖖", "🗿"), ("✂️", "📄"), ("🗿", "🗿"), ("🦎", "🖖")]))