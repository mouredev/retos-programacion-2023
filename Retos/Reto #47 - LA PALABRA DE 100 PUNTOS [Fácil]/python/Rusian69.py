"""
 * La última semana de 2021 comenzamos la actividad de retos de programación,
 * con la intención de resolver un ejercicio cada semana para mejorar
 * nuestra lógica... ¡Hemos llegado al EJERCICIO 100! Gracias 🙌
 *
 * Crea un programa que calcule los puntos de una palabra.
 * - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
 *   español de 27 letras, la A vale 1 y la Z 27.
 * - El programa muestra el valor de los puntos de cada palabra introducida.
 * - El programa finaliza si logras introducir una palabra de 100 puntos.
 * - Puedes usar la terminal para interactuar con el usuario y solicitarle
 *   cada palabra.
"""
import string

abc_list = string.ascii_lowercase

def indentificador_de_palabras ():
    
    total = 0
    print ("Igrese la palabra para indentificar su valor: ")
    word = input(": ")
    for index in word:
        total += abc_list.index(index) + 1

    if total != 100:
        print (f"you lose, your word have {total} vaule")
        respomt = input ("try again? [y/n]:")
        if respomt == "y":
            indentificador_de_palabras ()
        else:
            exit()
    else:
        return("YOU WIN")
print (indentificador_de_palabras())
