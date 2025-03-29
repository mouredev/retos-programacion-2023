# Reto #1: EL "LENGUAJE HACKER"
#### Dificultad: Fácil | Publicación: 02/01/23 | Corrección: 09/01/23

## Enunciado

#  Escribe un programa que reciba un texto y transforme lenguaje natural a
#  "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
#   se caracteriza por sustituir caracteres alfanuméricos.
#  - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
#    con el alfabeto y los números en "leet".
#    (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")

def text_transform(text):
    leet_dict = {
    'A': '4',
    'B': '8',
    'C': '<',
    'D': '|)',
    'E': '3',
    'F': 'ƒ',
    'G': '6',
    'H': '#',
    'I': '1',
    'J': '_|',
    'K': '|<',
    'L': '1_',
    'M': '/\\/\\',
    'N': '|\\|',
    'O': '0',
    'P': '|°',
    'Q': '0,',
    'R': 'Я',
    'S': '$',
    'T': '7',
    'U': 'µ',
    'V': '\\/',
    'W': '\\/\\/',
    'X': '}{',
    'Y': '`/',
    'Z': '2'
    }
    
    # Ejemplo de uso
    leet_text = ''.join(leet_dict.get(letra, letra) for letra in text.upper())

    # Salida en leet speak
    print(leet_text)  

text_transform("cawabonga")
