"""
@javierm_p
chat gtp hizo el reto casi completamente solo con el input:
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.

Tuvo un error en el isograma.
"""


def es_heterograma(cadena):
    """
    Función que determina si una cadena de texto es un heterograma.
    Un heterograma es una palabra que no tiene ninguna letra repetida.
    """
    letras = set()
    print(cadena)
    for letra in cadena:
        if letra.isalpha():
            if letra.lower() in letras:
                return False
            else:
                letras.add(letra.lower())
    return True


def es_isograma(cadena):
    """
    Función que determina si una cadena de texto es un isograma.
    Un isograma es una palabra o frase en la que cada letra aparece el mismo número de veces.
    Si cada letra aparece solo una vez será un heterograma, si aparece dos, un isogroma de segundo orden y así sucesivamente.
    """
    letras = {}
    for letra in cadena:
        letra_minuscula = letra.lower()
        if letra_minuscula in letras:
            letras[letra_minuscula] += 1
        else:
            letras[letra_minuscula] = 1

    repeticion_letras = set(letras.values())
    return len(repeticion_letras) == 1


def es_pangrama(cadena):
    """
    Función que determina si una cadena de texto es un pangrama.
    Un pangrama es una palabra o frase que contiene todas las letras
    del alfabeto al menos una vez.
    """
    letras = set()
    for letra in cadena:
        if letra.isalpha():
            letras.add(letra.lower())
    return len(letras) == 26


if __name__ == "__main__":
    palabra = input("Frase o palabra: ").replace(" ", "")
    es_heterograma = es_heterograma(palabra)
    print(f"es_heterograma: {es_heterograma}")
    es_pangrama = es_pangrama(palabra)
    print(f"es_pangrama: {es_pangrama}")
    es_isograma = es_isograma(palabra)
    print(f"es_isograma: {es_isograma}")
