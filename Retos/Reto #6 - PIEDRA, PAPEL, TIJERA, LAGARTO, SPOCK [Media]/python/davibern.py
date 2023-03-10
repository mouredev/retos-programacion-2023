"""
    Crea un programa que calcule quien gana mΓ‘s partidas al piedra,
    papel, tijera, lagarto, spock.
    - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
    - La funciΓ³n recibe un listado que contiene pares, representando cada jugada.
    - El par puede contener combinaciones de "πΏ" (piedra), "π" (papel),
      "βοΈ" (tijera), "π¦" (lagarto) o "π" (spock).
    - Ejemplo. Entrada: [("πΏ","βοΈ"), ("βοΈ","πΏ"), ("π","βοΈ")]. Resultado: "Player 2".
    - Debes buscar informaciΓ³n sobre cΓ³mo se juega con estas 5 posibilidades.

"""

def juego(jugadas: list[tuple]) -> str:
    
    resultado = ''
    jugador_1 = 0
    jugador_2 = 0
    
    reglas = {
        'πΏ': {'βοΈ', 'π¦'},
        'βοΈ': {'π', 'π¦'},
        'π': {'πΏ', 'π'},
        'π¦': {'π', 'π'},
        'π': {'βοΈ', 'πΏ'}
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
    print(juego([('πΏ', 'βοΈ'), ('π', 'πΏ'), ('π', 'βοΈ')]))
