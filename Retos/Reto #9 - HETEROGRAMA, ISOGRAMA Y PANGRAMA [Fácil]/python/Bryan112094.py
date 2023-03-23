# Crea 3 funciones, cada una encargada de detectar si una cadena de
# texto es un heterograma, un isograma o un pangrama.
# Heterograma -> no tiene letras repetidas 

import string

#Obtener todas las letras del abecedario
abecedario = list(string.ascii_lowercase)
abecedario.extend('ñ')

def conver_Text(text):
    text_Final = text.lower().replace(" ", "")
    reemplazo = [ ('á', 'a'), ('é', 'e'), ('í', 'i'), ('ó', 'o'), ('ú', 'u')]
    for a, b in reemplazo:
        text_Final = text_Final.replace(a, b)
    
    return text_Final

def is_Heterograma(text):
    texto = conver_Text(text)
    agre = ''

    for letra in abecedario:
        if texto.count(letra) > 1:
            agre = 'no '
            break
    
    print(f"{text} -> {agre}es un Heretograma")

def is_Isograma(text):
    texto = conver_Text(text)
    repeat_char = {}

    for letra in abecedario:
        if texto.count(letra) > 0:
            repeat_char[letra] = texto.count(letra)
            valor_max = max(repeat_char.values())
            valor_min = min(repeat_char.values())

    if valor_max == valor_min:
        print(f"{text} -> es un Isograma")
    else:
        print(f"{text} -> no es un Isograma")

def is_Pangrama(text):
    texto = conver_Text(text)
    repeat_char = {}

    for letra in abecedario:
        if texto.count(letra) > 0:
            repeat_char[letra] = texto.count(letra)

    if len(repeat_char) == 27:
        print(f"{text} -> es un Pangrama")
    else:
        print(f"{text} -> no es un Pangrama")


is_Heterograma('luteranismo')
is_Isograma('UNCOPYRIGTABLE')
is_Pangrama('Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaa del menú')
