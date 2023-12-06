PIEDRA  = "🗿"
PAPEL   = "📄"
TIJERA  = "✂️" 
LAGARTO = "🦎"
SPOCK   = "🖖"

def buscar_ganardor(lista):
    """
    Recibe una lista de tuplas que contienen iconos de piedra, papel, tijera, lagarto, spock.
    Args:
        lista(tuple): Cadena a evaluar.
    Return:
        str: Retorna el jugador que más ganó.
    """
    jugador_01 = 0
    jugador_02 = 0
    
    for jugada in lista:
        if jugada[0] == PIEDRA:
            if jugada[1] == PAPEL or jugada[1] == SPOCK:
                jugador_02 += 1
            elif jugada[1] == LAGARTO or jugada[1] == TIJERA:
                jugador_01 += 1
        elif jugada[0] == LAGARTO:
            if jugada[1] == TIJERA or jugada[1] == PIEDRA:
                jugador_02 += 1
            elif jugada[1] == SPOCK or jugada[1] == PAPEL:
                jugador_01 += 1
        elif jugada[0] == SPOCK:
            if jugada[1] == PAPEL or jugada[1] == LAGARTO:
                jugador_02 += 1
            elif jugada[1] == TIJERA or jugada[1] ==  PIEDRA:
                jugador_01 += 1
        elif jugada[0] == TIJERA:
            if jugada[1] == SPOCK or jugada[1] == PIEDRA:
                jugador_02 += 1
            elif jugada[1] == LAGARTO or jugada[1] == PAPEL:
                jugador_01 += 1
        elif jugada[0] == PAPEL:
            if jugada[1] == TIJERA or jugada[1] == LAGARTO:
                jugador_02 += 1
            elif jugada[1] == SPOCK or jugada[1] == PIEDRA:
                jugador_01 += 1

    if jugador_01 > jugador_02:
        return 'Player 1'
    if jugador_01 < jugador_02:
        return 'Player 2'
    return 'Tie'

def main():
    lista = [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")] 
    ganador = buscar_ganardor(lista)
    print(ganador)

if __name__ == "__main__":
    main()
