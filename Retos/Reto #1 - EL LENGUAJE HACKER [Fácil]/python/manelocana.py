# Reto #1 el lenguaje hacker

# hacemos un diccionario, copia/pega
diccionario_leet = {
    'a': '4',
    'b': '8',
    'c': '<',
    'd': '[)',
    'e': '3',
    'f': '|=',
    'g': '6',
    'h': '#',
    'i': '1',
    'j': '_|',
    'k': '|<',
    'l': '1',
    'm': '/\\/\\',
    'n': '|\\|',
    'o': '0',
    'p': '|*',
    'q': '0,',
    'r': '|2',
    's': '5',
    't': '7',
    'u': '|_|',
    'v': '\\/',
    'w': '\\/\\/',
    'x': '><',
    'y': '`/',
    'z': '2'
}

# iteramos el texto input, mirando las coincidencias con el diccionario, y hacemos el cambio almacenando
# los nuevos caracteres en texto_convers 
def convertidor_texto():
    texto_convers = ''
    texto_input = input('dame el texto a convertir en leet: ')
    for letra in texto_input.lower():
        if letra in diccionario_leet:
            texto_convers += diccionario_leet[letra]
        else:
            texto_convers += letra    
    return texto_convers

convertir_texto = convertidor_texto()
print(f'aqui la traduccion: {convertir_texto}')
