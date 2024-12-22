# /*
#  * Crea 3 funciones, cada una encargada de detectar si una cadena de
#  * texto es un heterograma, un isograma o un pangrama.
#  * - Debes buscar la definición de cada uno de estos términos.
#  */

def heterograma(cadena):
    cadena = cadena.replace(" ", "").lower()
    return len(cadena) == len(set(cadena))

def isograma(cadena):
    cadena = cadena.replace("", " ").lower()
    return len(cadena) == len(set(cadena))

def pangrama(cadena):
    print(cadena.replace(" ", "").lower())
    cadena = cadena.replace(" ", "").lower()
    return len(set(cadena)) == 27


cadena = "abcdefghijklmnño pqrstuvwxyz"
print(heterograma(cadena)) # True
print(isograma(cadena)) # True
print(pangrama(cadena)) # True
