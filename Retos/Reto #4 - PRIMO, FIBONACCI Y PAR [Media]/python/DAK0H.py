'''
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
'''

# Validar número por input
while True:
    try:
        number = int(input("Introduce un número: "))
        break
    except ValueError:
        print("Por favor ingresa un número entero.")

def check_number(number):
    result = ""
    # Comprobar número fibonacci (es la suma de los dos numeros anteriores),
    if number == 0 or number == 1:
        result += 'es Fibonacci'
    else:
        a = 0
        b = 1
        fibonacci_numbers = [a, b]
        while b < number:
            a, b = b, a + b
            fibonacci_numbers.append(b)
        result += 'es Fibonacci,' if number in fibonacci_numbers else 'no es Fibonacci,'
        
    # Comprobar número par (divisible entre 2)
    result += ' es par' if number % 2 == 0 else ' es impar'

    # Comprobar número primo (divisible entre 1 y si mismo)        
    if number == 1:
        result += ' y no es primo.'
    elif number == 2:
        result += ' y es primo.'
    else:
        for i in range(2, number):
            if number % i == 0:
                result += ' y no es primo'
                break
        else:
            result += ' y es primo'
    return result

result = check_number(number)
print(f"El número {number} {result}")
