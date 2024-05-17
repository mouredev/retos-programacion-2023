#!/usr/bin/python3

"""
# Reto #42: Punto de encuentro
/*
 * Crea una función que calcule el punto de encuentro de dos objetos en movimiento
 * en dos dimensiones.
 * - Cada objeto está compuesto por una coordenada xy y una velocidad de desplazamiento
 *   (vector de desplazamiento) por unidad de tiempo (también en formato xy).
 * - La función recibirá las coordenadas de inicio de ambos objetos y sus velocidades.
 * - La función calculará y mostrará el punto en el que se encuentran y el tiempo que tardarán en lograrlo.
 * - La función debe tener en cuenta que los objetos pueden no llegar a encontrarse.   
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




import numpy as np


def punto_encuentro(x1, v1, x2, v2, debug=False):
    assert len(x1) == len(x2)
    assert len(x1) == len(v1)
    assert len(x2) == len(v2)

    delta_v = v1 - v2
    delta_x = x2 - x1

    if debug:
        print("delta_v", delta_v)
        print("delta_x", delta_x)

    # caso 1, que parten del punto de encuentro
    if np.all(delta_x == 0):
        if debug:
            print("caso 1")
        return x1, 0

    # caso 2. existen diferencias entre las posciones
    # relativas pero las velocidades relativas son cero
    # los objetos nunca se encuentran
    if np.all(delta_v == 0) and np.any(delta_x != 0):
        if debug:
            print("caso 2")
        return None, None

    # caso 3. existe al menos una cordenada donde la
    # velocidad velocidad relativa es 0
    # mientras que la distancia es mayor que cero
    # los objetos no se encuentran 
    index_no_vel = delta_v == 0
    value_dis_no_vel = delta_x[index_no_vel]
    if value_dis_no_vel.size > 0 and np.all(value_dis_no_vel != 0):
        if debug:
            print("value_dis_no_vel", value_dis_no_vel)
            print("caso 3")
        return None, None

    nuevo_delta_x = delta_x[delta_v != 0] 
    nuevo_delta_v = delta_v[delta_v != 0]
    # time_vector = nuevo_delta_x / nuevo_delta_v
    time_vector = np.divide(nuevo_delta_x, nuevo_delta_v)

    print(time_vector)

    # caso 5. existe un valor de t
    if np.all(time_vector[0] == time_vector):
        return x1 + time_vector * v1, time_vector[0]

    # caso 6. no existen valores de t que satisfacen la condicion
    return None, None


if __name__ == '__main__':

    # CASO 1

    x1 = np.array([0, 0])
    x2 = np.array([0, 0])
    v1 = np.array([1, 0])
    v2 = np.array([0, 1])
    assert not punto_encuentro(x1=x1, x2=x2, v1=v1, v2=v2)[0] is None
    assert not punto_encuentro(x1=x1, x2=x2, v1=v1, v2=v2)[1] is None

    # CASO 2

    x1 = np.array([3, 2])
    x2 = np.array([2, 3])
    v1 = np.array([1, 0])
    v2 = np.array([1, 0])
    assert punto_encuentro(x1=x1, x2=x2, v1=v1, v2=v2)[0] is None
    assert punto_encuentro(x1=x1, x2=x2, v1=v1, v2=v2)[1] is None


    # CASO 3
    x1 = np.array([3, 2])
    x2 = np.array([2, 3])
    v1 = np.array([1, 0])
    v2 = np.array([1, 2])
    assert punto_encuentro(x1=x1, x2=x2, v1=v1, v2=v2)[0] is None
    assert punto_encuentro(x1=x1, x2=x2, v1=v1, v2=v2)[1] is None

    # CASO 4
    x1 = np.array([0, 1])
    x2 = np.array([1, 0])
    v1 = np.array([1, 0])
    v2 = np.array([0, 1])
    assert not punto_encuentro(x1=x1, x2=x2, v1=v1, v2=v2)[0] is None
    assert not punto_encuentro(x1=x1, x2=x2, v1=v1, v2=v2)[1] is None