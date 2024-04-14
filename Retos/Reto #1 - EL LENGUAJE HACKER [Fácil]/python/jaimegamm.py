"""
# Reto #1: EL "LENGUAJE HACKER"
#### Dificultad: Fácil |

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
#### Tienes toda la información extendida sobre los retos de programación semanales en **[retosdeprogramacion.com/semanales2023](https://retosdeprogramacion.com/semanales2023)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.
"""

leetme = {
    'A': '4',
    'B': 'I3',
    'C': '[',
    'D': ')',
    'E': '3',
    'F': '|=',
    'G': '&',
    'H': '#',
    'I': '1',
    'J': ',_|',
    'K': '>|',
    'L': '1',
    'M': '/\\/\\',
    'N': '^/',
    'O': '0',
    'P': '|*',
    'Q': '(_,)',
    'R': '|2',
    'S': '5',
    'T': '7',
    'U': '(_)',
    'V': '\\/',
    'W': '\\/\\/',
    'X': '><',
    'Y': 'j',
    'Z': '2',
    ' ': ' ',
    '!': '!',
    '?': '?',
    '.': '.',
    'Ñ': 'ñ'
}

def leet_converter(text):
    leet_text = ""
    for char in text:
        leet_text += leetme.get(char.upper(), char)
    return leet_text

if __name__ == "__main__":
    input_text = input("Introduce el texto a convertir a leet: ")
    result = leet_converter(input_text)
    print("Texto original: ", input_text)
    print("Texto en leet: ", result)
