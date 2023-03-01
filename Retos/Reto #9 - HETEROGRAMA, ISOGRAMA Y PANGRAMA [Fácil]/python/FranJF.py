"""
/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */
"""

def heterograma(palabra:str):
    if len(palabra) == set(palabra.split()):
        return True
    else:
        return False

def isograma(palabra:str):
    pass

def pangrama(palabra:str):
    pass


print(heterograma('Calumbrientos'))
