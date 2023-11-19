'''/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */'''


import random

jugador1_puntuacion = 0
jugador2_puntuacion = 0


def piedra_papel_tijera_lagarto_spock(jugada1, jugada2, jugador1_puntuacion, jugador2_puntuacion):
    ganador = ''

    for n in range(len(jugada1)):
        if jugada1[n] == jugada2[n]:
            ganador = 'Tie'
        elif jugada1[n] == '🗿':

            if jugada2[n] == '✂️' or jugada1[n] == '🦎':
                ganador = 'Player 1'
                jugador1_puntuacion += 1
            else:
                ganador = 'Player 2'
                jugador2_puntuacion += 1

        elif jugada1[n] == '📄':

            if jugada2[n] == '🗿' or jugada2[n] == '🖖':
                ganador = 'Player 1'
                jugador1_puntuacion += 1
            else:
                ganador = 'Player 2'
                jugador2_puntuacion += 1

        elif jugada1[n] == '✂️':

            if jugada2[n] == '📄' or jugada2[n] == '🦎':
                ganador = 'Player 1'
                jugador1_puntuacion += 1
            else:
                ganador = 'Player 2'
                jugador2_puntuacion += 1

        elif jugada1[n] == '🦎':

            if jugada2[n] == '📄' or jugada2[n] == '🖖':
                ganador = 'Player 1'
                jugador1_puntuacion += 1
            else:
                ganador = 'Player 2'
                jugador2_puntuacion += 1

        elif jugada1[n] == '🖖':

            if jugada2[n] == '🗿' or jugada2[n] == '✂️':
                ganador = 'Player 1'
                jugador1_puntuacion += 1
            else:
                ganador = 'Player 2'
                jugador2_puntuacion += 1

        print(f'El ganador es: {ganador}')
    return jugador1_puntuacion, jugador2_puntuacion


jugada1 = []
jugada2 = []
for i in range(5):
    jugada1.append(random.choice(['🗿', '📄', '✂️', '🦎', '🖖']))
    jugada2.append(random.choice(['🗿', '📄', '✂️', '🦎', '🖖']))

print(jugada1, jugada2)
jugador1_puntuacion, jugador2_puntuacion = piedra_papel_tijera_lagarto_spock(
    jugada1, jugada2, jugador1_puntuacion, jugador2_puntuacion)
print(f'El ganador es el Player 1 con {jugador1_puntuacion} puntos') if jugador1_puntuacion > jugador2_puntuacion else print(
    f'El ganador es el Player 2 con {jugador2_puntuacion} puntos')
