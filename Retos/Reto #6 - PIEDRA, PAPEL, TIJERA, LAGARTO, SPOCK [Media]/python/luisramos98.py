#!/usr/bin/env python3

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

'''
Reglas del juego

-    Piedra aplasta tijeras.
-    Tijeras cortan papel.
-    Papel cubre a la piedra.
-    Piedra aplasta lagarto.
-    Lagarto envenena a Spock.
-    Spock destroza tijeras.
-    Tijeras decapitan lagarto.
-    Lagarto come papel.
-    Papel refuta a Spock.
-    Spock vaporiza la piedra.

'''

import random

opciones = ['piedra','papel','tijera','lagarto','spock']

fortalezas = {
    'piedra':{'tijera','lagarto'},
    'papel':{'piedra','spock'},
    'tijera':{'papel','lagarto'},
    'lagarto':{'papel','spock'},
    'spock':{'tijera','piedra'}
}

p1 = ''
p2 = ''
jugadas = []
resultado = []
fin_del_juego = False


def op_correct(player):

    return True if [True for op in opciones if op == player ] else False

def setear_jugador(numero):

    op = False
    if not numero == 2:
        while op == False:

            player = input(f'\n[i] Player {numero}: Ingresa una opcion: ')
            op = op_correct(player)

            if not op:
                print('\n\t[!] Ingrese solo las opciones válidas: piedra, papel, tijera, lagarto, spock')

        return player

    return random.choice(opciones)


def setear_resultado(p1,p2):
    for opcion,fortaleza in fortalezas.items():

        if p1 == opcion:
            if p1 == p2:
                return None

            if p2 in fortaleza:
                return 'Player 1'
            else:
                return 'Player 2'


def partida():

    p1 = setear_jugador(1)

    p2 = setear_jugador(2)

    print(f'\n[i] Máquina: {p2}')

    resultado.append(setear_resultado(p1,p2))
    jugadas.append((p1,p2))


while fin_del_juego == False:
    if len(resultado) < 2:
        partida()
    else:
        c1 = 0
        c2 = 0
        for r in resultado:

            c1 += 1 if r == 'Player 1' else 0
            c2 += 1 if r == 'Player 2' else 0 
            
        if c1 == 2 or c2 == 2:               
            # Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
            print(f'\n[+] Entrada: {jugadas}. Resultado: {resultado[-1]}')
            fin_del_juego = True
        else:
            partida()






