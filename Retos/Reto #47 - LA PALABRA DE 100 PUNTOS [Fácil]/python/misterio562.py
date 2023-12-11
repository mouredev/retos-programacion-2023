"""/*
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
 */"""

abecedario = 'abcdefghijklmnñopqrstuvwxyz'

def alphabet():
    alphabet = {}

    for i, item in enumerate(abecedario):
        letter = i + 1
        alphabet[abecedario[i]] = letter

    return alphabet

def calculate_word(word): 
    if word.isalpha():
        lower_word = word.lower()       
        value = 0

        get_alphabet = alphabet()
        for item in lower_word:
            if item in get_alphabet:
                value += get_alphabet[item]
                print(f'{item} vale {get_alphabet[item]} puntos')   

        validate(value)   
    else:
        print('Solo se admiten letras')
        main()
        
def validate(total):
    if total == 100:
        print(f'¡Ganaste!, sacaste {total}')
    else:
        print(f'Sigue intentando, sacaste {total}')
        main()
    
def main():
    print('\n Cada letra de la palabra tiene un valor \n'
          +'ej: a = 1 ; hasta z = 27. Ingresa una palabra, si vale 100 ganas')
    input_word = input('Ingresa una palabra en idioma español [a-z]: ')    
    calculate_word(input_word)

main()    