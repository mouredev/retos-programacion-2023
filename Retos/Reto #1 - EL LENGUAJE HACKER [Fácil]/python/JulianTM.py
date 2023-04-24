# Reto #1: EL "LENGUAJE HACKER"


diccionario = {'A': '4', 'B': 'I3', 'C': '[', 'D': ')', 'E': '3', 'F': '|=', 'G': '&',
               'H': '#', 'I': '1', 'J': ',_|', 'K': '>|', 'L': '1', 'M': '[V]', 'N': '^/',
               'O': '0', 'P': '|*', 'Q': '(_,)', 'R': 'I2', 'S': '5', 'T': '7', 'U': '(_)',
               'V': '\/', 'W': '\/\/', 'X': '><', 'Y': 'j', 'Z': '2', '1': 'L', '2': 'R', '3': 'E',
               '4': 'A', '5': 'S', '6': 'b', '7': 'T', '8': 'B', '9': 'g', '0': 'o'}


texto = input('Ingrese su texto:\n').upper()
traduccion = ''

# "Letra" recorre el texto y verifica que la letra exista en el diccionario.
for letra in texto:
    if letra in diccionario.keys():
        traduccion += diccionario[letra]
# Si no se encuentra en el diccionario se agrega a la traducción igual a como fue ingresada
    else:
        traduccion += letra

print(traduccion)


"""
* Escribe un programa que reciba un texto y transforme lenguaje natural a
* "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
*  se caracteriza por sustituir caracteres alfanuméricos.
* - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
*   con el alfabeto y los números en "leet".
*   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
"""
