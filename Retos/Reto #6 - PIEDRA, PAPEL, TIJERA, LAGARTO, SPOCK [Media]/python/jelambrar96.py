#!/usr/bin/python3

"""
# Reto #6: Piedra, Papel, Tijera, Lagarto, Spock
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */
"""

__author__ = "Jorge Lambraño - jelambrar96"
__copyright__ = "Copyright 2024, retos-programacion-2023"
__credits__ = ["Brais Moure - mouredev"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Jorge Lambraño"
__email__ = "jelambrar@gmail.com"
__status__ = "Production"


from enum import Enum
from random import randint



class Mano(Enum):
    PIEDRA = 0
    LAGARTO = 1
    SPOCK = 2
    TIJERAS = 3
    PAPEL = 4


DICCIONARIO_TRADUCTOR = {
    "✂️" : Mano.TIJERAS,
    "🖖" : Mano.SPOCK,
    "📄" : Mano.PAPEL,
    "🗿" : Mano.PIEDRA,
    "🦎" : Mano.LAGARTO,
}

LISTA_TRADUCTOR = [ "🗿", "🦎", "🖖", "✂️", "📄", ]


class Resultado(Enum):
    GANA_P1 = -1
    GANA_P2 = 1
    EMPATE = 0


def batalla(p1: Mano, p2: Mano):
    """
    Tijeras cortan papel
    Papel cubre piedra
    Piedra aplasta lagarto
    Lagarto envenena Spock
    Spock destruye tijeras
    Tijeras decapitan lagarto
    Lagarto come papel
    Papel desaprueba Spock
    Spock vaporiza piedra
    Piedra aplasta tijeras
    """
    if p1.value == p2.value:
        return Resultado.EMPATE
    value_p1 = p1.value
    value_p2 = p2.value
    value_p2 =+ 5
    diferencia = value_p2 - value_p1
    if diferencia % 2 == 1:
       return Resultado.GANA_P1
    else:
       return Resultado.GANA_P2


def juego_Mano(lista_batallas):
    resultado_batalla = [ batalla(p1, p2).value for p1, p2 in lista_batallas ]
    suma_batallas = sum(resultado_batalla)
    return "Tie" if suma_batallas == 0 else ("Player 1" if suma_batallas > 0 else "Player 2")


def juego_iconos(lista_batallas):
    juego_mano_temp = [ (DICCIONARIO_TRADUCTOR[p1], DICCIONARIO_TRADUCTOR[p2]) for p1, p2 in lista_batallas ]
    return juego_Mano(juego_mano_temp)


def crear_juego_aleatorio(n_batallas=10):
    return [ (LISTA_TRADUCTOR[randint(0,4)], LISTA_TRADUCTOR[randint(0,4)]) for i in range(n_batallas) ]



if __name__ == '__main__':
    N = 12
    juego = crear_juego_aleatorio(N)
    print(juego)
    resultado = juego_iconos(juego)
    print(resultado)

