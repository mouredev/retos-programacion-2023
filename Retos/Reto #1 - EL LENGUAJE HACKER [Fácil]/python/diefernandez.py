"""
    Reto 1
    Escribe un programa que reciba un texto y transforme lenguaje natural a
    "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
     se caracteriza por sustituir caracteres alfanuméricos.
    
    - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
      con el alfabeto y los números en "leet".
      (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
"""

leet_alphabet = {
  ' ':' ', 'A': '4', 'B':'I3', 'C':'[', 'D':')', 'E':'3', 'F':'|=', 'G':'&', 'H':'#', 
  'I':'1',  'J':',_|', 'K':'>|', 'L':'1', 'M':'/\//\/', 'N':'/^/', 'O':'0', 'P':'|*', 
  'Q':'(_,)', 'R':'I2', 'S':'5', 'T':'7', 'U':'(_)', 'V':'/\/', 'W':'/\//\/', 'X':'><', 
  'Y':'j', 'Z':'2', '0':'o', '1':'L', '2':'R', '3':'E', '4':'A', '5':'S', '6':'b', 
  '7':'T', '8':'B', '9':'g',
}

def transform_to_leet(text):
    transformed = ''
    for letter in text.upper():
        transformed += leet_alphabet[letter] if letter in leet_alphabet else ''
    return transformed

print('Enter text to translate into Leet Speak...')
input_text = input()
translation = transform_to_leet(input_text)
print('Input:', input_text)
print('Translation:', translation)