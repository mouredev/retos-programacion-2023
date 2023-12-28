"""
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
"""

traductor = {
    "a": "4", "b": "l3", "c": "[", "d": ")", "e": "3",
    "f": "|=", "g": "&", "h": "#", "i": "1", "j": ",_|",
    "k": ">|", "l": "1", "m": "/\/\\", "n": "^/", "o": "0",
    "p": "|*", "q": "(,)", "r": "|2", "s": "5", "t": "7",
    "u": "(_)", "v": "\/", "w": "\/\/", "x": "><", "y": "j", "z": "2"
}

def leet_speak(texto):
    leet_text = ""
    for char in texto:
        leet_char = traductor.get(char, char)
        leet_text += leet_char
    return leet_text

while True:
    texto = input("Tu mensaje es: ")
    texto = texto.lower()  # Convertir a minúsculas para manejar mayúsculas
    resultado = leet_speak(texto)
    
    print("Tu mensaje en leet speak es:")
    print("\n" + resultado + "\n")
    
    end = input("¿Deseas repetir? (y/n) ").lower()
    while end not in ["y", "n"]:
        end = input("Por favor, prueba otra vez: ").lower()
        
    if end == "n":
        break
