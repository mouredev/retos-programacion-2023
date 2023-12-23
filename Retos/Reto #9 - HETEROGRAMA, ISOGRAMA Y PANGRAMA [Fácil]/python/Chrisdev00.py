"""
* Crea 3 funciones, cada una encargada de detectar si una cadena de
* texto es un heterograma, un isograma o un pangrama.
* - Debes buscar la definición de cada uno de estos términos.

Un heterograma es una palabra, frase u oración en la que ninguna letra del alfabeto aparece más de una vez. 

Un isograma es una palabra en la que las letras aparecen el mismo número de veces. En un isograma de primer orden, 
cada letra aparece solo una vez, mientras que en un isograma de segundo orden, cada letra aparece dos veces. 

Un pangrama es una oración o frase que contiene cada letra del alfabeto al menos una vez. 

Por tanto, la principal diferencia entre estos términos es que un heterograma y un isograma se centran en la repetición de letras, 
mientras que un pangrama se centra en la presencia de todas las letras del alfabeto al menos una vez.
 
"""

import re

def heterogram_word(word): 
    
    no_number_text = re.sub(r"\d+", "", word.lower().replace(" ", ""))
    no_punt_text = re.sub(r"[^\w\s]", "", no_number_text)
    result = len(set(no_punt_text))
    if result == len(no_punt_text):
        print(f'La palabra "{word}" es HETEROGRAMA.')
    else:
        print(f'La palabra "{word}" no es HETEROGRAMA.')


def isogram_word (word):
    
    count = {}
    for letra in word.lower():         # Cuento cada letra de la palabra y la convierto en un dictionario clave valor
        if letra in count:
            count[letra] += 1
        else:
            count[letra] = 1
    #print(count.values())
    suma_values = sum(count.values())     # Sumo los valores del diccionario 
    if suma_values % 2 == 0:
        count_list = list(count.values())
        if (all(val == count_list[0] for val in count_list)):  # Utilizo la funcion "all" para verificar si todos los valores son iguales al primer valor del diccionario
            print(f'La palabra "{word}" es un ISOGRAMA')
        else:
            print(f'La palabra "{word}" no es un ISOGRAMA')
    else:
        print(f'La palabra "{word}" no es un ISOGRAMA')


def pangram_word(word):
    count = {}
    for letra in word.lower():      # Cuento cada letra de la palabra y la convierto en un diccionario clave-valor
        if letra.isalpha():         # Ignorar caracteres que no son letras
            if letra in count:
                count[letra] += 1
            else:
                count[letra] = 1
    #print(count)
    list_alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    es_pangram = all(letra in count for letra in list_alfabeto)
    if es_pangram:
        print(f'La palabra "{word}" Es un PANGRAMA')
    else:
        print(f'La palabra "{word}" No es un PANGRAMA')

    return es_pangram


palabra_ejemplo = "PATHFinder"
palabra_ejemplo_2 = "VivieNne"
palabra_ejemplo_3 = "Jaded zombies acted quaINtly BUT kept driving their oxen forward"

heterogram_word(palabra_ejemplo)
isogram_word(palabra_ejemplo)
pangram_word(palabra_ejemplo)

heterogram_word(palabra_ejemplo_2)
isogram_word(palabra_ejemplo_2)
pangram_word(palabra_ejemplo_2)

heterogram_word(palabra_ejemplo_3)
isogram_word(palabra_ejemplo_3)
pangram_word(palabra_ejemplo_3)






        
