'''
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
'''

def is_prime(number: int) -> str:

    # Caso 0
    if number == 0:
        return "El número no es primo"

    # Caso positivo
    if number > 0:
        for i in range(2, number):
            if number % i == 0:
                return "El número no es primo"
        return "El número es primo"
    
    # Caso negativo
    if number < 0:
        for i in range(-2, number, -1):
            if number % i == 0:
                return "El número no es primo"
        return "El número es primo"

def is_even(number: int) -> str:
    if number%2 == 0:
        return "El número es par"
    else:
        return "El número es impar"

def is_fibonacci(number: int) -> str:

    # Controlamos los números negativos
    if number < 0:
        return "El número no es fibonacci"

    # Primeros números de la serie
    elif number == 0 or number == 1:
        return "El número es fibonacci"
    else:
        two_previous = 0
        previous = 1
        while previous < number:
            current = previous + two_previous
            two_previous = previous
            previous = current
            if current == number:
                return "El número es fibonacci"
        
        return "El número no es fibonacci"

def main():
    number = int(input("Inserte un número para realizar las comprobaciones: "))
    print()
    print(f"--> {is_prime(number)}")
    print(f"--> {is_fibonacci(number)}")
    print(f"--> {is_even(number)}")

if __name__ == "__main__":
    main()