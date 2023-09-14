# Reto #4: PRIMO, FIBONACCI Y PAR
#### Dificultad: Media | Publicación: 23/01/23 | Corrección: 30/01/23

## Enunciado

"""
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
"""
import math

def ask_number():
    return int(input("Número: "))

def perfect_square(number):
    sq = int(math.sqrt(number))
    return (sq * sq) == number

def check_number_fibonacci(number):
    return perfect_square(5*number*number + 4 ) or perfect_square(5*number*number - 4)
def check_number_even(number):
    return number % 2 == 0
def check_number_prime(number):
    if number == 1:
        return False
    elif number > 1:
        for i in range(2,number):
            if number%i == 0:
                return False
        return True
    else:
        return False
def str_constructor(number,bool_fibonacci,bool_even,bool_prime):
    str = {"number": number}
    if bool_fibonacci:
        str["fibonacci"] = "es fibonacci"
    else:
        str["fibonacci"] = "no es fibonacci"
    if bool_even:
        str["even"] = "es par"
    else:
        str["even"] = "es impar"
    if bool_prime:
        str["prime"] = "es primo"
    else: 
        str["prime"] = "no es primo"
    return str
    
def main():
    number = ask_number()
    string_object = str_constructor(number,check_number_fibonacci(number),check_number_even(number),check_number_prime(number))
    print(f"{number} {string_object['prime']}, {string_object['fibonacci']} y {string_object['even']}")
    
if __name__ == "__main__":
    main()