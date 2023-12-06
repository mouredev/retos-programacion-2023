'''
* Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
'''

def obtener_ganador(jugador1, jugador2):
    if jugador1 == jugador2:
        return "Tie"

    if (jugador1 == "piedra" and (jugador2 == "tijera" or jugador2 == "lagarto")) or \
       (jugador1 == "papel" and (jugador2 == "piedra" or jugador2 == "spock")) or \
       (jugador1 == "tijera" and (jugador2 == "papel" or jugador2 == "lagarto")) or \
       (jugador1 == "lagarto" and (jugador2 == "papel" or jugador2 == "spock")) or \
       (jugador1 == "spock" and (jugador2 == "piedra" or jugador2 == "tijera")):
        return "Player 1"
    else:
        return "Player 2"

def main():
    partidas = int(input("Ingrese el número de partidas a jugar: "))

    jugador1_victorias = 0
    jugador2_victorias = 0

    for i in range(partidas):
        jugador1 = input("Jugador 1 - Elige: piedra, papel, tijera, lagarto o spock: ")
        jugador2 = input("Jugador 2 - Elige: piedra, papel, tijera, lagarto o spock: ")

        ganador = obtener_ganador(jugador1, jugador2)

        if ganador == "Player 1":
            jugador1_victorias += 1
        elif ganador == "Player 2":
            jugador2_victorias += 1

        print(f"Ganador de la partida {i+1}: {ganador}")

    print("----- Resultado Final -----")
    print(f"Jugador 1: {jugador1_victorias} victorias")
    print(f"Jugador 2: {jugador2_victorias} victorias")

    if jugador1_victorias == jugador2_victorias:
        print("Empate en el total de partidas")
    elif jugador1_victorias > jugador2_victorias:
        print("¡Jugador 1 es el ganador!")
    else:
        print("¡Jugador 2 es el ganador!")

if __name__ == "__main__":
    main()