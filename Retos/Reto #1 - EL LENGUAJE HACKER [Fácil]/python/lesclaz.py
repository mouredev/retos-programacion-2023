#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ejercicio:
# Escribe un programa que reciba un texto y transforme lenguaje natural a
# "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
#  se caracteriza por sustituir caracteres alfanuméricos.
# - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
#   con el alfabeto y los números en "leet".
#   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")


__leet_speak_alphabet = {
    'a': '4', 'b': 'I3', 'c': '[', 'd': ')', 'e': '3', 'f': '|=', 
    'g': '&', 'h': '#', 'i': '1', 'j': ',_|', 'k': '>|', 'l': '|_',
    'm': '/\/\\', 'n': '^/', 'o': '0', 'p': '|*', 'q': '(_,)', 'r': 'I2',
    's': '5', 't': '7', 'u': '(_)', 'v': '\/', 'w': '\/\/', 'x': '><',
    'y': '\// ', 'z': '2'
}


def main(text: str) -> str:
    encripted_text = ''

    for _ in text.lower():
        encripted_text += __leet_speak_alphabet[_] \
        if __leet_speak_alphabet.get(_) else _
    return encripted_text


if __name__ == '__main__':
    print(main('Encripta esto si puedes'))
