'''
Escribe un programa que reciba un texto y transforme lenguaje natural a
"lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
se caracteriza por sustituir caracteres alfanuméricos.
- Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
con el alfabeto y los números en "leet".
(Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
'''
def translator(text):
  leet_speak = {'a': 4, 'b': 8, 'c': '<', 'd': '>', 'e': '&', 'f': 'v', 'g': 9, 'h': '#', 
                'i': 1, 'j': ';', 'k': '1<', 'l': '£', 'm': '^^', 'n': 'И', 'o': 0, 'p': 9, 
                'q': 2, 'r': 'Я', 's': 5, 't': 7, 'u': 'µ', 'v': '\/', 'w': 'Ш', 'x': 'ecks', 
                'y': '¥', 'z': 's'}
  list_ls = []

  for letter in text:
    if letter in leet_speak.keys():
      list_ls.append(leet_speak[letter])
    else:
      list_ls.append(letter)
  
  end_text = ''.join(map(str, list_ls))
  return end_text


test = 'Leet speak o leet es un tipo de escritura compuesta de caracteres alfanuméricos'
print(translator(test))

user = input('Texto a traducir: ').lower()
print(translator(user))