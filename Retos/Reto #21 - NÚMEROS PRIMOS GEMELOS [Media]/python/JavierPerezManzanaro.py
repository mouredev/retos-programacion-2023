"""
   /*
 * Crea un programa que encuentre y muestre todos los pares de números primos
 * gemelos en un rango concreto.
 * El programa recibirá el rango máximo como número entero positivo.
 *
 * - Un par de números primos se considera gemelo si la diferencia entre
 *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
 *
 * - Ejemplo: Rango 14
 *   (3, 5), (5, 7), (11, 13)
 */

"""

# Doctest
# python3 -m doctest -v "#21 Números primos gemelos.py"


import os


def es_primo(numero: int)->bool:
    """Vemos si un número es primo o no

    Args:
        numero (int): número a estudiar

    Returns:
        bool: True si, False no lo es


    >>> es_primo(3)
    True
    >>> es_primo(23)
    True
    >>> es_primo(4)
    False
    >>> es_primo(9)
    False
    """
    if numero == 1:
        return False
    for i in range(2, numero):
        if (numero % i) == 0:
            return False
    return True


def primos_gemelos(rango: int)->list:
    """Retorna la lista de los números primos que son gemelos

    Args:
        rango (int): El rango que decide el cliente

    Returns:
        list: La lista de tuplas con los números primos que son gemelos

    # https://elpais.com/ciencia/el-juego-de-la-ciencia/2023-01-27/primalidad.html#
    # https://es.wikipedia.org/wiki/Número_primo_gemelo

    >>> primos_gemelos(100)
    [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43), (59, 61), (71, 73)]
    >>> primos_gemelos(1000)
    [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43), (59, 61), (71, 73), (101, 103), (107, 109), (137, 139), (149, 151), (179, 181), (191, 193), (197, 199), (227, 229), (239, 241), (269, 271), (281, 283), (311, 313), (347, 349), (419, 421), (431, 433), (461, 463), (521, 523), (569, 571), (599, 601), (617, 619), (641, 643), (659, 661), (809, 811), (821, 823), (827, 829), (857, 859), (881, 883)]
    """
    lista_primos_gemelos = []
    for numero in range(1, rango):
        if es_primo(numero):
            # es primo

            if es_primo(numero+2):
                #print(f'{numero} -- {numero+2}')
                tupla = (numero, numero+2)
                lista_primos_gemelos.append(tupla)
    return lista_primos_gemelos




if __name__ == '__main__':
    os.system('clear')
    import doctest
    doctest.testmod(verbose=True)

    rango = int(input('El rango va desde el 1 hasta ¿Cual quieres que sea el límite? '))
    print(primos_gemelos(rango))
