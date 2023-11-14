ABECEDARIO = "abcdefghijklmnopqrstuvwxyz"

def juntar_frase(frase: str):
    return ("").join(frase.split(" ")).lower()

def heterograma(palabra: str):
    palabra = juntar_frase(palabra)
    if len(palabra) == len(set(palabra)):
        return True
    return False

def isograma(palabra: str):
    dict_letras = {}
    palabra = juntar_frase(palabra)
    for letra in palabra:
        if letra not in dict_letras.keys():
            dict_letras[letra] = 1
        else:
            dict_letras[letra] += 1

    return len(set(list(dict_letras.values()))) ==  1

def pangrama(palabra: str):
    palabra = juntar_frase(palabra)
    if len(ABECEDARIO) == len(set(palabra)):
        return True
    return False

print(pangrama("The quick brown fox jumps over the lazy dog")) # True

