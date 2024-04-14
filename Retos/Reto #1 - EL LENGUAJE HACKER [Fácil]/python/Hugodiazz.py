#Escribe un programa que reciba un texto y transforme lenguaje natural a
#"lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
#se caracteriza por sustituir caracteres alfanuméricos.
#- Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
#    con el alfabeto y los números en "leet".
#(Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")

diccionarioHacker = {
    'A': '4', 'B': 'I3', 'C': '[',
    'D': ')', 'E': '3', 'F': '|=',
    'G': '&', 'H': '#', 'I': '1',
    'J': ',_|', 'K': '>|', 'L': '1',
    'M': '/\/\\', 'N': '^/', 'O': '0',
    'P': '|*', 'Q': '(_,)', 'R': 'I2',
    'S': '5', 'T': '7', 'U': '(_)',
    'V': '\/', 'W': '\/\/', 'X': '><',
    'Y': 'j', 'Z': '2'
}

def cifrarPalabra(str): 
    palabra = ''
    for letra in str.upper(): #Recorre cada letra de la palabra convertida a mayúsculas
        if letra in diccionarioHacker.keys(): #Si la letra coincide con la clave del diccionario, se agrega el valor a la palabra
            palabra += diccionarioHacker[letra]
        else:
            palabra += letra #Si no se encuentra en el diccionario, agrega la letra a la palabra

    return palabra

print(cifrarPalabra(input('Ingresa una palabra: ')))
