"""
    Crea un programa que calcule quien gana más partidas al piedra,
    papel, tijera, lagarto, spock.
    - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
    - La función recibe un listado que contiene pares, representando cada jugada.
    - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
      "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
    - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
    - Debes buscar información sobre cómo se juega con estas 5 posibilidades.

"""

def juego(jugadas: list[tuple]) -> str:
    
    resultado = ''
    jugador_1 = 0
    jugador_2 = 0
    
    reglas = {
        '🗿': {'✂️', '🦎'},
        '✂️': {'📄', '🦎'},
        '📄': {'🗿', '🖖'},
        '🦎': {'📄', '🖖'},
        '🖖': {'✂️', '🗿'}
    }
    
    for turno in jugadas:
        if turno[1] in reglas[turno[0]]:
            jugador_1 += 1
        else:
            jugador_2 += 1
            
    if jugador_1 > jugador_2:
        resultado = 'Gana jugador 1'
    elif jugador_2 > jugador_1:
        resultado = 'Gana jugador 2'
    else:
        resultado = 'Empate'
    
    return resultado


if __name__ == "__main__":
    print(juego([('🗿', '✂️'), ('🖖', '🗿'), ('📄', '✂️')]))
