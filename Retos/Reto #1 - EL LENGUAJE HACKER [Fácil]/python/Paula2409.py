"""
## Enunciado

```
/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
```
"""
import unittest

def hacker_language(text: str):
    """ Converts a text to 'leet' language ased on the mappings in the 'leet_table'

    Args:
        text (str): any text
        
    Returns:
        None
        
    Raise:
        ValueError: if the text is invalid or None
    """
    leet_table = {'a': '4', 'b': 'l3', 'c': '[', 'd': ')', 'e': '3', 'f': '|=', 'g': '&', 'h':'#', 'i': '1', 'j':',_|', 'k':'>|', 'l':'1', 'm':'/\\/\\','n': '^/',
                  'o':'0', 'p':'|*','q':'(_,)','r':'l2','s':'5', 't':'7','u':'(_)','v':'\/', 'w':'\/\/','x':'><','y':'j', 'z':'2',
                  '1':'L', '2':'R', '3':'E', '4': 'A', '5':'S','6':'b','7':'T','8':'B','9': 'g','0':'o'}
    
    text_hacked = ''
    try:
        for char in text.lower():
            if char in leet_table:
                text_hacked += leet_table[char]
            else:
                text_hacked += char
        print(text_hacked)
    except ValueError:
        print('Ingrese un texto valido')
    
hacker_language("python")

    
