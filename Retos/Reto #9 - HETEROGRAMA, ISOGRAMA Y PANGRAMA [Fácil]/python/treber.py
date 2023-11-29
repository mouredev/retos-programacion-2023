# Reto #9: Heterograma, isograma y pangrama
#### Dificultad: Fácil | Publicación: 27/02/23 | Corrección: 06/03/23

## Enunciado
"""
/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */
"""
"""
* Heterograma:
Un heterograma (del griego héteros, 'diferente' y gramma, 'letra')
es una palabra o frase que no contiene ninguna letra repetida.

* Isograma:
Un isograma (del griego isos, 'igual' y gramma, 'letra')
es una palabra o frase en la que cada letra aparece el mismo número de veces

* Pangrama:
Un pangrama (del griego pan, 'todo' y gramma, 'letra')
es una frase en la que aparecen todas las letras del abecedario.
Si cada letra aparece sólo una vez, formando por tanto un heterograma, se le llama pangrama perfecto

"""
import string

def pangrama(txt): # 

    txt = txt.lower()
    for i in string.ascii_lowercase:
        if i not in txt:
            return False
    
    return True

def heterograma(txt):
    
    for i in range(len(txt)):
        start = i+1
        if start < len(txt):
            if txt[i] in txt[start:len(txt)]:
                return False
    
    return True 

def isograma(txt):
    
    for i in range(len(txt)):
        start = i+1
        if start < len(txt):
            if txt[i] in txt[start:len(txt)]:
                return True

    return False


def inputTexto():

    txt_input = input("Escriba una palabra o frase: ")

    if pangrama(txt_input):
        print("El texto es un pangrama.")
    elif heterograma(txt_input):
        print("El texto es un heterograma.")
    elif isograma(txt_input):
        print("El texto es un isograma.")
    else:
        print("El texto no es un heterograma, isograma ni pangrama.")


inputTexto()

"""
Probar los siguientes textos:
1. Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú
2. yuxtaponer
3. escritura
"""