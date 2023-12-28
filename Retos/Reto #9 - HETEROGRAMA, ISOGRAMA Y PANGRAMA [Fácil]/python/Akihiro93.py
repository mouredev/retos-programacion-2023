# Limpiador de texto

def limpia_texto(texto):
    lista_de_letras_validas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                            'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                            'z', 'ñ', 'á', 'é', 'í', 'ó', 'ú', 'ü']
    texto = texto.lower()
    texto_limpio = ""
    for letra in texto:
        if letra.isdigit():
            continue
        if letra not in lista_de_letras_validas:
            continue
        if letra in "áéíóúü":
            if letra == "á":
                letra = "a"
            elif letra == "é":
                letra = "e"
            elif letra == "í":
                letra = "i"
            elif letra == "ó":
                letra = "o"
            elif letra == "ú" or letra == "ü":
                letra = "u"
        if letra == " ":
            letra = ""
        texto_limpio += letra
    return texto_limpio


def heterograma(palabra):
    letras = []
    for letra in palabra:
        if letra in letras:
            print("No es un eterograma")
        else:
            letras.add(letra)
    print("Es un eterograma")


# Isograma
def isograma(palabra):
    lista_isograma = [i for i in palabra]
    lista_isograma = lista_isograma.lower
    i = ""
    for i in lista_isograma:
        if lista_isograma.count(i) != 1:
            print("No es un isograma")
            break
    else:
        print("Es un isograma")


# Pangrama
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def pangrama(palabra):
    palabra = limpia_texto(palabra)
    lista_pangrama = list(set(i for i in palabra))
    palabra = lista_pangrama.lower
    i = ""
    for i in alphabet_list:
        if lista_pangrama.count(i) != 1:
            print("No es un pangrama")
            break
    else:
        print("Es un pagrama")


print(heterograma(input("¿Cual es la palabra?:")))
print(isograma(input("¿Cual es la palabra?: ")))
print(pangrama(input("El parrafo para comprobar\nsi es un pangrama: ")))
