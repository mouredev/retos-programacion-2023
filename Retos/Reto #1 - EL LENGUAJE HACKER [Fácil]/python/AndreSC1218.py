"""
Escribe un programa que reciba un texto y transforme lenguaje natural a
"lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
se caracteriza por sustituir caracteres alfanuméricos.
Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
con el alfabeto y los números en "leet".
(Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
"""

def to_leet_speak(text):
    # Diccionario que mapea las letras y números a su equivalente en Leet Speak
    leet_dict = {
        'A':'4', 'B':'I3', 'C':'[', 'D':')' ,'E':'3', 'F':'|=', 'G':'&', 'H':'#', 'I':'1', 'J':',_|', 'K':'>|',
         'L':'1', 'M':'JVI', 'N':'^/', 'O': '0', 'P':'|*', 'Q':'(_,)', 'R':'I2', 'S':'5', 'T': '7', 'U':'(_)', 'V':'\/', 'W':'\/\/', 'X':'><', 'Y':'j', 'Z': '2',
         '1':'L', '2':'R', '3':'E', '4':'A', '5':'S', '6':'b', '7':'T', '8':'B', '9':'g', '0':'o'
    }
    # Inicializa una cadena vacía para almacenar la salida
    leet_text = ''
    # Itera sobre cada carácter en la entrada
    for char in text.upper():
        # Si el carácter es un número y se encuentra en el diccionario, reemplázalo con su equivalente en Leet Speak
        if char.isdigit() and char in leet_dict:
            leet_text += leet_dict[char]
        # Si el carácter es una letra y se encuentra en el diccionario, reemplázalo con su equivalente en Leet Speak
        elif char.isalpha() and char in leet_dict:
            leet_text += leet_dict[char]
        # Si no, agrégalo sin cambios
        else:
            leet_text += char
    # Devuelve la cadena resultante
    return leet_text

# Pide al usuario que introduzca una frase
text = input("Introduce una frase: ")
# Convierte la frase a Leet Speak
leet_text = to_leet_speak(text)
# Imprime la frase resultante
print("Frase en Leet Speak:", leet_text)