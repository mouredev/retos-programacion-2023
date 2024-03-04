#!/usr/bin/python3

"""
# Reto #7: El sombrero seleccionador
/*
 * Crea un programa que simule el comportamiento del sombrero seleccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
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


import random


def preguntar(texto_pregunta, valores_validos):
    while True:
        print()
        entrada = input(texto_pregunta)
        indice = valores_validos.index(entrada)
        if indice >= 0:
            return entrada, indice
        print("Respuesta Invalida")


def unzip(zipped_iterables):
    """
    Unzips a list of zipped iterables and returns a tuple of lists.

    :param zipped_iterables: A list of zipped iterables
    :return: A tuple of lists where each list contains the corresponding elements of the zipped iterables
    """
    unzipped = tuple(map(list, zip(*zipped_iterables)))
    return unzipped    


PREGUNTAS = [
    "¿Cómo te definirías?",
    "¿Cuál es tu clase favorita?",
    "¿Dónde pasarías más tiempo?",
    "¿Cuál es tu color favorito?",
    "¿Cuál es tu mascota?",
]

ESCUELAS = [
    "gryffindor",
    "hufflepuff",
    "ravenclaw",
    "slytherin"
]

OPCIONES = [
    [
        "Valiente",
        "Leal",
        "Sabio",
        "Ambicioso",    
    ],
    [
        "Vuelo",
        "Pociones",
        "Defensa contra las artes oscuras",
        "Animales fantásticos",    
    ],
    [
        "Invernadero",
        "Biblioteca",
        "En la sala común",
        "Explorando",    
    ],
    [
        "Rojo",
        "Azul",
        "Verde",
        "Amarillo",    
    ],
    [
        "Sapo",
        "Lechuza",
        "Gato",
        "Serpiente",    
    ],
]


def main(use_random=True):

    # resultado para cada escuela
    resultados = [0, 0, 0, 0]
    # opcion para cada escuela
    respuestas_validas = ['1', '2', '3', '4']

    # se iteran las preguntas
    for i, item in enumerate(PREGUNTAS):
        # se seleccioan las preguntas y las opciones
        pregunta = PREGUNTAS[i]
        lista_opciones = OPCIONES[i]

        # se desordean las opciones y las preguntas de tal manera que las
        # preguntas sigan en el mismo indice que las opciones
        if use_random:
            zipped = [item for item in zip(respuestas_validas, lista_opciones)]
            random.shuffle(zipped)
            temp_respuestas_validas, temp_opciones = unzip(zipped)
        else:
            temp_respuestas_validas, temp_opciones = respuestas_validas, lista_opciones

        # se agrega un numero a las opciones
        temp_opciones = [ (str(j+1) + ". " + jitem) for j, jitem in enumerate(temp_opciones)]
        # se genera el texto de las preguntas
        texto_pregunta = pregunta + "\n" + "\n".join(temp_opciones) + "\n"

        # se toma el indice
        __, indice = preguntar(texto_pregunta, respuestas_validas)
        # se busca el valor
        numero_respuesta = int(temp_respuestas_validas[indice])
        resultados[numero_respuesta - 1] += 1


    # se organiza aleatoriamente con el fin de que en caso de un empate
    # se haga una seleccion aleatoria
    zipped = list(zip(resultados, ESCUELAS))
    random.shuffle(zipped)
    random_resultados, random_ESCUELAS = unzip(zipped)

    # se busca el maximo valor y el maximo indice
    maximo_valor = max(random_resultados)
    maximo_indice = random_resultados.index(maximo_valor)
    escuela_seleccionada = random_ESCUELAS[maximo_indice].upper() 

    # print(f"\n¡{escuela_seleccionada}!")
    return escuela_seleccionada



if __name__ == '__main__':
    escuela_seleccionada = main()
    print(f"\n¡{escuela_seleccionada}!")


