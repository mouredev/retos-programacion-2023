#!/usr/bin/python3

"""
RETO #2 EL PARTIDO DE TENIS
/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
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


labels = ["Love", 15, 30, 40]


def tenis(lista_jugadores):

    if len(lista_jugadores) < 4:
        print("Fallo")
        return

    p1_count, p2_count = 0, 0
    
    for item in lista_jugadores:
        
        if "P1" == item:
            p1_count += 1
        elif "P2" == item:
            p2_count += 1
        
        # print(p1_count, p2_count)
        
        if "P1" == item and p1_count - p2_count > 1 and p1_count > 3:
            print("Ha ganado el jugador 1")
            break
        if "P2" == item and p2_count - p1_count > 1 and p2_count > 3:
            print("Ha ganado el jugador 2")
            break

        if p1_count > 3 or p2_count > 3:
            if p1_count == p2_count:
                print("Deuce")
            elif p1_count > p2_count:
                print("Ventaja P1")
            elif p2_count > p1_count:
                print("Ventaja P2")
        else:
            print(labels[p1_count], "-", labels[p2_count])

if __name__ == '__main__':
    tenis(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"])



