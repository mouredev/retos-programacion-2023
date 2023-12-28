"""
Created on Sat Feb 11 11:38:15 2023

@author: rafadataengineer
"""

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
 */
 '''

import os
from random import choice


reglas = {
    'piedra' : ('tijera', 'lagarto'),
    'lagarto' : ('papel', 'spock'),
    'spock' : ('piedra', 'tijera'),
    'tijera' : ('lagarto', 'papel'),
    'papel' : ('spock', 'piedra')
}

elementos = ('piedra', 'lagarto', 'spock', 'tijera', 'papel')


def ganador(partidas : list[tuple]) -> str:
    jugador1 = 0
    jugador2 = 0

    for i in partidas:
        if i[0] != i[1]:
            if i[1] in reglas[i[0]]:
                jugador1 += 1
            else:
                jugador2 += 1
    
    if jugador1 > jugador2:
        return 'Jugador 1'
    elif jugador2 > jugador1:
        return 'Jugador 2'
    else:
        return 'Empate'


def main():
    partida = 0
    resultados = []
    
    while partida < 3:
        os.system('cls')
        print('Juego piedra, papel, tijera, lagarto o spock.\n')
        print(f'''Partida numero {partida + 1}.
        * {elementos[0]}
        * {elementos[1]}
        * {elementos[2]}
        * {elementos[3]}
        * {elementos[4]}
        ''')
        
        jugador1 = input('Seleccione una opcion: ')

        if jugador1 in elementos:
            
            jugador2 = choice(elementos)

            print('~'*30)
            print(f'\nEleccion Jugador 2: {jugador2}\n')
            print(f'Resultado partida numero {partida + 1}: {jugador1} vs {jugador2}\n')
            resultados.append((jugador1, jugador2))
            input('Presione enter para avanzar...')

            partida += 1
        else:
            print('~'*30)
            print('\nLa eleccion no se encuentra en la lista.\n')
            input('Presione enter para avanzar...')

    print('~'*30)
    print(f'\nEl ganador es: {ganador(resultados)}\n')
    input('Presione enter para finalizar...')


if __name__ == '__main__':
    main()