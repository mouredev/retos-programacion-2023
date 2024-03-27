#!/usr/bin/python3

"""
# Reto #8: El generador pseudoaleatorio
/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
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


import time


def linear_congruential_generator(x_0, a_const, b_const, module, n_iterations):
    assert module > 0, f'm={module}'
    assert a_const > 0 and a_const < module, f'a={a_const}'
    assert b_const >= 0 and b_const < module, f'b={b_const}'
    assert x_0 > 0 and x_0 < module, f'x_0={x_0}'
    x_final = x_0
    for __ in range(n_iterations):
        x_final = (x_final + a_const + b_const) % module
    return x_final


def random_integer_generator(min_value: int, max_value: int):
    range_value = max_value - min_value
    # take from microseconds
    # print(time.time())
    semilla = 1 + int(time.time() * 1000 * 1000) % (range_value - 1)
    a = 1 + int(time.time() * 1000) % (range_value - 1)
    b = int(time.time()) % range_value
    n = 10 + ( semilla % 32 )
    # print("a: ", a)
    # print("b: ", b)
    # print("n: ", n)
    # print("semilla: ", semilla)
    return min_value + linear_congruential_generator(semilla, a, b, range_value, n)


if __name__ == '__main__':
    # for i in range(20):
    #     print(random_integer_generator(0, 100))
    #     time.sleep(0.01)

    from collections import Counter

    lista = [ random_integer_generator(0, 100) for i in range(100)]
    for item in lista:
        print (item)
    print(Counter(lista))


