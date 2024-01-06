# /*
#  * Escribe un programa que reciba un texto y transforme lenguaje natural a
#  * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
#  *  se caracteriza por sustituir caracteres alfanuméricos.
#  * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
#  *   con el alfabeto y los números en "leet".
#  *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
#  */


diccionario_leet = {
    "A": "4", "B": "|3", "C": "[", "D": ")",
    "E": "3", "F": "|=", "G": "&", "H": "#",
    "I": "1", "J": ",_|", "K": ">|", "L": "1",
    "M": "/\\/\\", "N": "^/", "O": "0", "P": "|*",
    "Q": "(_,)", "R": "I2", "S": "5", "T": "7",
    "U": "(_)", "V": "\\/", "W": "\\/\\/", "X": "><",
    "Y": "j", "Z": "2", "0": "o", "1": "L",
    "2": "R", "3": "E", "4": "A", "5": "S",
    "6": "b", "7": "T", "8": "B", "9": "g",
    " ": " ", ",": ",", ".": ".", ";": ";"
}


def convertir_texto(texto_normal):
    texto_convertido = ""
    for letra in texto_normal:
        letra = letra.upper()
        if letra in diccionario_leet:
            texto_convertido += diccionario_leet[letra]
        else:
            texto_convertido += letra
    return texto_convertido

def main():
    seguir_preguntando = True
    print("Bienvenidos al conversor al lenguaje Hacker")
    print("¿Desea convertir un texto?")
    while seguir_preguntando:
        opcion_menu = input(f"(Pulse 's' para convertir o cualquier otra letra para salir) \n")
        if opcion_menu.upper() == "S":
            texto_introducido = input("Introduzca el texto que quiere pasar a lenguaje hacker \n")
            resultado = convertir_texto(texto_introducido)   
            print("*" * 40)
            print("Su texto original es el siguiente:")
            print(texto_introducido)
            print("-" * 40)
            print("Su texto convertido es el siguiente:")
            print(resultado)
            print("*" * 40 + "\n")
            print("¿Desea convertir un nuevo texto?")
        else:
            print("Hasta pronto!")
            seguir_preguntando = False

if __name__ == "__main__":
    main()
