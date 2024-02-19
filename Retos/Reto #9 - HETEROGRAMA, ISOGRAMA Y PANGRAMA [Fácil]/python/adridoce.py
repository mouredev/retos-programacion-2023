import string

"""
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
"""

#Un heterograma es una palabra o frase que no contiene ninguna letra repetida.
def heterograma(cadena):
    letras = []

    for letra in cadena.lower():
        if letra not in letras:
            letras.append(letra)
        else:
            print(f"La palabra {cadena} no es un heterograma")
            return

    print(f"La palabra {cadena} es un heterograma")

#Un isograma es una palabra o frase en la que cada letra aparece el mismo número de veces.
def isograma(cadena):
    contador_letras = dict()
    palabra = cadena.lower().strip()

    for letra in palabra:
        # Obtenemos el valor asociado a la clave letra, si no existe la añade con valor 0
        veces = contador_letras.get(letra, 0) + 1
        contador_letras[letra] = veces

    for tupla in contador_letras.items():
        if tupla[1] != veces:
            print(f"La palabra {cadena} no es un isograma")
            return False
        
        print(f"La palabra {cadena} es un isograma")
        return True
    
#Un pangrama es una frase en la que aparecen todas las letras del abecedario.
def pangrama(cadena):
    cadena = cadena.lower().strip()
    letras_en_cadena = set(filter(str.isalpha, cadena))
    
    if set(string.ascii_lowercase) == letras_en_cadena:
        print("La cadena introducida es un pangrama")
        return True
    else:
        print("La cadena introducida no es un pangrama")
        return False


heterograma("Adrian")
heterograma("letra")
isograma("murciélago")
isograma("jazz")
pangrama("abcdefghijklmnopqrstuvwxyz")
pangrama("abcdefghijklmnñopqrstuvwxyz")