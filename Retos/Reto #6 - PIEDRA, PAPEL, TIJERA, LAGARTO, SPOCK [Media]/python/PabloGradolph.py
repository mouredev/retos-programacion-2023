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

 * Reglas del juego: Tijera corta a papel, papel tapa a piedra, piedra aplasta a lagarto, lagarto envenena a Spock, Spock rompe a tijera, 
 * tijera decapita a lagarto, lagarto devora a papel, papel desautoriza a Spock, Spock vaporiza a piedra, y como siempre, piedra aplasta a tijera:
 * (✂️ > 📄) ; (📄 > 🗿) ; (🗿 > 🦎) ; (🦎 > 🖖) ; (🖖 > ✂️) ; (✂️ > 🦎) ; (🦎 > 📄) ; (📄 > 🖖) ; (🖖 > 🗿) ; (🗿 > ✂️)
 */
'''

def reglas(par: tuple) -> int:
    
    # En caso de empate no pasa nada
    if par[0] == par[1]:
        return 0
    else:
        jugador1 = manos[par[0]]
        jugador2 = manos[par[1]]
        jugada = (jugador1, jugador2)

        # Si la tupla está directamente en la lista reglas_juego punto para jugador 1.
        # Sino, es porque será una de las tuplas de reglas_juego pero invertida y punto para jugador 2.
        return 1 if jugada in reglas_juego else 2

def juego(jugadas: list) -> str:

    # Control de errores en la entrada
    if len(jugadas) == 0:
        return "Error, lista de jugadas vacía"
    for par in jugadas:
        if len(par) != 2:
            return "Error, las entradas deben ser pares de jugadas."
        if (par[0] not in manos) or (par[1] not in manos):
            return "Error, alguna de las jugadas no es correcta."
    
    contador_P1 = contador_P2 = 0
    for par in jugadas:
        jugada = reglas(par)
        if jugada == 1:
            contador_P1 += 1
        elif jugada == 2:
            contador_P2 += 1
        elif jugada == 0:
            continue
        else:
            return "Está ocurriendo un error."
    
    if contador_P1 == contador_P2:
        return "Tie"
    elif contador_P1 > contador_P2:
        return "Player1"
    else:
        return "Player2"

def main():
    global manos, reglas_juego
    manos = {"🗿": "piedra", "📄": "papel", "✂️": "tijera", "🦎": "lagarto", "🖖": "spock"}
    
    # Lista de tuplas replicando el apartado "Reglas del juego":
    reglas_juego = [("tijera","papel"), ("papel","piedra"), ("piedra","lagarto"), ("lagarto","spock"), ("spock","tijera"), ("tijera","lagarto"),\
        ("lagarto","papel"), ("papel","spock"), ("spock","piedra"), ("piedra","tijera")]

    # Ejemplos uso correcto
    print(juego([("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]))
    print(juego([("🗿","✂️"), ("✂️","🗿"), ("📄","✂️"), ("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]))
    print(juego([("✂️","🖖"), ("🦎","🖖"), ("🦎","📄"), ("🗿","📄"), ("🖖","🗿")]))
    print(juego([("🗿","✂️"), ("✂️","🗿"), ("📄","✂️"), ("📄","📄"), ("🖖","✂️")]))

    # Ejemplos de mal uso
    print()
    print(juego([]))
    print(juego([("✂️","🖖"), ("🦎","🖖"), ("🦎","📄","🦎")]))
    print(juego([("tijera","🖖"), ("🦎","🖖"), ("🦎","📄","🦎")]))

if __name__ == "__main__":
    main()