# Created by luiveldel
# Escribe un programa que reciba un texto y transforme lenguaje natural a
# "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
# se caracteriza por sustituir caracteres alfanuméricos.
# - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
#   con el alfabeto y los números en "leet".
#   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")


# First, create a dictionary for the hacker language
hacker_dict = {'a': '4', 
               'e': '3', 
               'i': '1', 
               'o': '0', 
               'A': '4', 
               'E': '3', 
               'I': '1', 
               'O': '0'}

word = "hacker"

for k, v in hacker_dict.items():
    word = word.replace(k, v)


print(word)