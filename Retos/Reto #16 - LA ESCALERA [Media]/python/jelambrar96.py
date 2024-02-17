#!/usr/bin/python3

"""
# Reto #16: La escalera
/*
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 * 
 * Ejemplo: 4
 *         _
 *       _|       
 *     _|
 *   _|
 * _|
 * 
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



def escalera_pos(numero: int):
    lista_escalera = []
    for i in range(numero):
        temp_string = "  " * i + "_|"
        lista_escalera.append(temp_string)
    lista_escalera.append("  " * numero + "_")
    return reversed(lista_escalera)


def escalera_neg(numero: int):
    lista_escalera = []
    lista_escalera.append("_")
    for i in range(numero):
        temp_string = " " + "  " * i + "|_"
        lista_escalera.append(temp_string)
    return lista_escalera
    

def escalera(numero: int):
    if numero == 0:
        return ["__"]
    elif numero > 0:
        return escalera_pos(numero)
    else:
        return escalera_neg(-1 * numero)


def mostrar_escalera(escalera):
    for item in escalera:
        print(item)


if __name__ == '__main__':

    print("Escalera 0")
    mostrar_escalera(escalera(0))
    print()
    
    print("Escalera 5")
    mostrar_escalera(escalera(5))
    print()
    
    print("Escalera -4")
    mostrar_escalera(escalera(-4))
    print()

