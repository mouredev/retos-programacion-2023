'''/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.

 # Heterograma: Palabra que no tiene ninguna letra repetida.
    # Isograma: palabra o frase en la que cada letra aparece el mismo número de veces
    # Pangrama: Palabra que contiene todas las letras del alfabeto.
    # Pangrama perfecto: Pangrama y además no tiene ninguna letra repetida.

 */'''


def heterograma(cadena):
    '''Devuelve True si la cadena es un heterograma.'''
    for letra in cadena:
        if cadena.count(letra) > 1:
            return False
    return True


def isograma(cadena):
    '''Devuelve True si la cadena es un isograma.'''
    for letra in cadena:
        if cadena.count(letra) != cadena.count(letra.lower()) + cadena.count(letra.upper()):
            return False
    return True


def pangrama(cadena):
    '''Devuelve True si la cadena es un pangrama.'''
    for letra in 'abcdefghijklmnñopqrstuvwxyz':
        if letra not in cadena.lower():
            return False
    return True


def pangrama_perfecto(cadena):
    '''Devuelve True si la cadena es un pangrama perfecto.'''
    if heterograma(cadena) == True and pangrama(cadena) == True:
        return True
    return False


cadena = input('Introduce una cadena de texto: ')
print('Heterograma: ', heterograma(cadena))
print('Isograma: ', isograma(cadena))
print('Pangrama: ', pangrama(cadena))
print('Pangrama perfecto: ', pangrama_perfecto(cadena))
