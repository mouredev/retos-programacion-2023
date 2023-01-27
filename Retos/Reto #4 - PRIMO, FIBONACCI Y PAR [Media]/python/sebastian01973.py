# Reto #4: PRIMO, FIBONACCI Y PAR
#### Dificultad: Media | Publicación: 23/01/23

## Enunciado
#
# Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
# Ejemplos:
# - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
# - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
#

def isPar(num) -> bool:
    return num % 2 == 0

def isPrime(num) -> bool:
    if number == 0 or number == 1 or number == 4:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

def isFibonacci(num) -> bool:
    num1 = 0
    num2 = 1
    counter = 0
    while num1 <= num:
        if num1 == num:
            return True

        num3 = num2 + num1
        num1 = num2
        num2 = num3
        counter += 1
    return False

# Validar que digite un numero y no un caracter
while True:
    try:
        number = int(input("Introduce un numero\n"))
        print(f'Es Par {isPar(number)}')
        print(f'Es Primo {isPrime(number)}')
        print(f'Es fibonacci {isFibonacci(number)}')
        break
    except ValueError:
        print("Tienes que introducir un numero\n")
        continue

