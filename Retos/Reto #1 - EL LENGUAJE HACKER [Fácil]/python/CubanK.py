#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 ### Reto #1: EL "LENGUAJE HACKER"” ###

 https://retosdeprogramacion.com/

 Escribe un programa que reciba un texto y transforme lenguaje natural a
 "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
  se caracteriza por sustituir caracteres alfanuméricos.
 - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
   con el alfabeto y los números en "leet".
   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
"""


dictionary = {
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
    "N": " ^/",
    "O": "0",
    "P": " |*",
    "Q": "(_,)",
    "R": "I2",
    "S": "5",
    "T": "7",
    "U": "(_)",
    "V": "\/",
    "W": "\/\/",
    "X": "><",
    "Y": "j",
    "Z": "2",
    "0": "o",
    "1": "L",
    "2": "R",
    "3": "E",
    "4": "A",
    "5": "S",
    "6": "b",
    "7": "T",
    "8": "B",
    "9": "g"
}


def translator(text: str) -> str:
    output = ""
    for ch in text.upper():
        output += dictionary.get(ch, ch)
    return output

def main():
    text = input(f"Please enter natural text:\n")
    print(f"The translation is: {translator(text)}")

main()
    
