#Documentando para aprender
#Importamos la libreria unicodedata para poder usar la función lower() y normalize() para poder convertir las letras en minúsculas y eliminar los acentos de las palabras.

import unicodedata
from unicodedata import normalize
#Luego creamos una función que recibe dos parámetros, el primero es el texto que queremos traducir y el segundo es un booleano que nos indica si queremos traducir de aurebesh a basic o de basic a aurebesh.
def basic_aurebesh_translator (text: str, aurebesh: bool) -> str:

    #En mi caso lo que hice fue crear un diccionario con las letras y su traducción en aurebesh
    basic_dict = {'a': 'aurek', 'b': 'besh','c': 'cresh','ch': 'cherek','d': 'dorn','e': 'esk','eo': 'onith','f': 'forn',
        'g': 'grek','h': 'herf','i': 'isk','j': 'jenth','k': 'krill','kh': 'krenth','l': 'leth','m': 'mern','n': 'nern','ng': 'nen',
        'o': 'osk','oo': 'orenth','p': 'peth','q': 'qek','r': 'resh','s': 'senth','sh': 'shen','t': 'trill','th': 'thesh','u': 'usk',
        'v': 'vev','w': 'wesk','x': 'xesh','y': 'yirt','z': 'zerek','ae': 'enth'
    }

    aurebesh_alphabet = dict() #Declaramos un diccionario vacío 
    for key, value in basic_dict.items():
        aurebesh_alphabet[value] = key #Agregamos al diccionario vacío las letras en aurebesh y su traducción en basic

    # Luego creamos una variable que almacena el texto en minúsculas y sin acentos para poder comparar con el diccionario.
    text = text.lower()
    text = normalize('NFD', text).encode('ascii', 'ignore').decode("utf-8")
    # Creamos una variable que almacena el texto traducido.
    translated_text = ""
    # Creamos un condicional que nos indica si el texto que queremos traducir es de aurebesh a basic o de basic a aurebesh.
    # Si el texto es de aurebesh a basic entra a este condicional.
    if aurebesh:
        translated_text = text
        for key, value in aurebesh_alphabet.items(): #Recorremos el diccionario con las letras en aurebesh y su traducción en basic
            translated_text = translated_text.replace(key, value)   #Reemplazamos las letras en aurebesh por su traducción en basic
    # Si el texto es de basic a aurebesh entra a este condicional.        
    else:
        # Creamos un contador que nos ayudará a recorrer el texto.
        character_index = 0
        # Creamos un ciclo while que recorre el texto y compara con el diccionario, si encuentra una coincidencia lo agrega a la variable translated_text y aumenta el contador en 1, si no encuentra una coincidencia agrega el caracter a la variable translated_text y aumenta el contador en 1.
        while character_index < len(text):
            if text[character_index] in basic_dict:
                translated_text += basic_dict[text[character_index]]
                character_index += 1
            elif text[character_index:character_index+2] in basic_dict:
                translated_text += basic_dict[text[character_index:character_index+2]]
                character_index += 2
            else:
                translated_text += text[character_index]
                character_index += 1
    # Retorna el texto traducido.
    return translated_text

aurebesh = basic_aurebesh_translator("I am Jedi", False)
print(aurebesh)
basic = basic_aurebesh_translator(aurebesh, True)
print(basic)

