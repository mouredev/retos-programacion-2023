"""
 * Crea un programa que calcule los puntos de una palabra.
 * - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
 *   español de 27 letras, la A vale 1 y la Z 27.
 * - El programa muestra el valor de los puntos de cada palabra introducida.
 * - El programa finaliza si logras introducir una palabra de 100 puntos.
 * - Puedes usar la terminal para interactuar con el usuario y solicitarle
 *   cada palabra.
"""
import re

abedecario = "abcdefghijklmnñopqrstuvwxyz"
def WordPoints():
    real_word = ""
    points_word = 0
    list_letters = list()
    word = str(input("hola, escribe una palabra, solo una palabra "))

    for i in word:

        if i == " ":
            break
        real_word += i

    real_word = real_word.lower()
    pattern = r'[a-z]'
    real_word = re.findall(pattern, real_word)
    print(real_word)
    
    for letters in real_word:
        for index, letter in enumerate(abedecario):
            if letter == letters:
                points_word += index +  1

    print(points_word)

    if points_word < 100:
        print("no es mayor que 100 puntos, intenta de nuevo crack")
        WordPoints()
    elif points_word >= 100:
        print("LO LOGRASTE")
        try_again = input("quieres volver a jugar?(y/n) ")
        if try_again == "y":
            try_again = ""
            WordPoints()
        elif try_again == "n":
            print("OK")
        else:
            try_again = ""
            print("lo tomare como un si")
            WordPoints()


   
    


WordPoints()
