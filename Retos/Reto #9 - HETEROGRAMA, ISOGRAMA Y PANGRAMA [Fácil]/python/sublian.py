# Reto #9: Heterograma, isograma y pangrama
#### Dificultad: Fácil | Publicación: 27/02/23 | Corrección: 06/03/23

## Enunciado

"""
* Crea 3 funciones, cada una encargada de detectar si una cadena de
* texto es un heterograma, un isograma o un pangrama.
* - Debes buscar la definición de cada uno de estos términos.

Heterograma: es una palabra o frase que no contiene ninguna letra repetida.
isograma: es una palabra o frase en la que cada letra aparece el mismo número de veces
pangrama: es un texto que usa todas las letras posibles del alfabeto de un idioma.
"""
from unidecode import unidecode
import re

def __char_Counter(text: str)->dict[str, int]:
    
    no_number_text = re.sub(r"\d+", "", text.lower().replace(" ", ""))
    no_punt_text = re.sub(r"[^\w\s]", "", no_number_text)

    # Obtenemos el unicode pero preservando la ñ
    unicode = unidecode(no_punt_text.replace("ñ", ".")).replace(".", "ñ")
    
    char_counter = dict()
    
    for char in unicode:
        if char in char_counter.keys():
            char_counter[char] +=1
        else:
            char_counter[char] = 1
            
    return char_counter

def isHeterogram(text: str) -> bool:
    for counter in __char_Counter(text).values():
        if counter >1 :
            return False
    return True

def isIsogram(text: str) -> bool:
    order = 0
    for counter in __char_Counter(text).values():
        if order == 0:
            order = counter
        if order is not counter:
            return False
    return True
        

def isPangram(text: str) -> bool:
    return len(__char_Counter(text).keys()) == 27

#test
if __name__ == '__main__':
    string_test_1 = "El cadáver de Wamba, rey godo de España, fue exhumado y trasladado en una caja de zinc que pesó un kilo."
    string_test_2 = "murcielago"
    string_test_3 = "hiperblanduzcós    !!w"
    result = ""
    result += "Es Heterograma " if isHeterogram(string_test_3) else "No es Heterograma "
    result += "Es Isograma " if isIsogram(string_test_3) else "No es Isograma "
    result += "y es Pangrama." if isPangram(string_test_3) else "y no es Pangrama"
    print(result)
