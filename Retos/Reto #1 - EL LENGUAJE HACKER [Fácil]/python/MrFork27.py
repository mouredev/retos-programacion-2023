
"""  
Escribe un programa que reciba un texto y transforme lenguaje natural a 
"lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje 
se caracteriza por sustituir caracteres alfanuméricos. 
- Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
con el alfabeto y los números en "leet". 
(Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
"""


# Funcion que transforma una cadena en formato leet
# a partir de una cadena y un diccionario con las transformaciones
def get_leet_string(normal_string, convert_table):
    leet_string = ""
    list_string = list(normal_string)

    for letter in list_string:
        leet_letter = convert_table.get(letter, letter)
        leet_string = leet_string + leet_letter

    return leet_string


# Diccionario con las transformaciones del lenguaje
LEET_TABLE = {
    "A": "4",
    "B": "I3",
    "C": "[",
    "D": ")",
    "E": "3",
    "F": "|=",
    "G": "&",
    "H": "#",
    "I": "1",
    "J": ",_|",
    "K": ">|",
    "L": "1",
    "M": "/\/\\",
    "N": "^/",
    "O": "0",
    "P": "|*",
    "Q": "(_,)",
    "R": "I2",
    "S": "5",
    "T": "7",
    "U": "(_)",
    "V": "\/",
    "W": "\/\/",
    "X": "><",
    "Y": "j",
    "Z": "2"
}

# El usuario introduce una cadena
normal_string = input("Introduce la cadena a transformar: ")
# Transformamos la cadena a lenguaje hacker
leet_string = get_leet_string(normal_string.upper(), LEET_TABLE)
# Imprimos el resultado
print("Cadena origen: ", normal_string.upper())
print("Resultado: ", leet_string)
