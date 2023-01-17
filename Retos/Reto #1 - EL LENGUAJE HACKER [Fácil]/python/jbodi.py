# Reto #1: EL "LENGUAJE HACKER"
#### Dificultad: Fácil | Publicación: 02/01/23 | Corrección: 09/01/23

## Enunciado

"""
/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
"""
traductor = {
    "a" : "4",
    "b" : "I3",
    "c" : "[",
    "d" : ")",
    "e" : "3",
    "f" : "|=",
    "g" : "&",
    "h" : "#",
    "i" : "1",
    "j" : ",_|",
    "k" : ">|",
    "l" : "1",
    "m" : "/\\/\\",
    "n" : "^/",
    "ñ" : "^/~",
    "o" : "0",
    "p" : "|*",
    "q" : "(_,)",
    "r" : "I2",
    "s" : "5",
    "t" : "7",
    "u" : "(_)",
    "v" : "\\/",
    "w" : "\\/\\/",
    "x" : "><",
    "y" : "j",
    "z" : "2",
}

texto_a_traducir = input("Inserte texto a traducir: ")


texto_traducido = ""
for letra in texto_a_traducir.lower():
    if letra in traductor:
        texto_traducido += traductor[letra]
print(texto_traducido)