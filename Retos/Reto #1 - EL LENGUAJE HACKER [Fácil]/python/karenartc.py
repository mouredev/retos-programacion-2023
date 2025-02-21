#  Escribe un programa que reciba un texto y transforme lenguaje natural a
#  "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
#   se caracteriza por sustituir caracteres alfanuméricos.
#  - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
#   con el alfabeto y los números en "leet".
#  (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")

def convertir_leet(texto):

    nuevo_alfabeto = {
        'a': '4', 'B': 'b', 'c': '[', 'd': ')', 'e': '3', 'f': '|=',
        'g': '&', 'h': '#', 'i': '1', 'j': ',_|', 'k': '>|', 'l': '1',
        'm': '/\/\\', 'n': '^/', 'o': '0', 'p': '|*', 'q': '(_,)', 'r': 'I2',
        's': '5', 't': '7', 'u': '(_)', 'v': '\/', 'w': '\/\/', 'x': '><',
        'y': 'j', 'z': '2', '1': 'L', '2': 'R', '3': 'E', '4': 'A', '5': 'S', '6': 'b',
        '7': 'T', '8': 'B', '9': 'g', '0': 'o'
    }
    nuevo_texto = ''

    for caracter in texto:
        
        nuevo_caracter = nuevo_alfabeto.get(caracter, caracter)
        nuevo_texto += nuevo_caracter
    
    return nuevo_texto

def obtener_texto():
    texto = input('Ingrese un texto: ')
    return  texto.lower()

def main():
    texto = obtener_texto()
    resultado = convertir_leet(texto)
    print(f'Tu texto {texto},\nen lenguaje Hacker es: {resultado}')

main()