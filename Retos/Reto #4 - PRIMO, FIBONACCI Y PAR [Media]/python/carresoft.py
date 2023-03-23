### Reto #4: PRIMO, FIBONACCI Y PAR ###
'''
 Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 Ejemplos:
 - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
'''

### Decision type of development ###
# The program is carried out with two functions, one to check if the number is Fibonacci and the other to see if it is prime. 
# For the Fibonacci function it is decided to use the Binet approximation, instead of a recursive function, since this for large numbers requires a lot of resources.

# Not optimal for large numbers
def fibonacci_calculation(num :int):
    if num > 1:
        return fibonacci_calculation(num-1) + fibonacci_calculation(num-2)
    return num

def binet_fibonacci_calculation(num :int):
    for i in range(0, num + 2):
        binet = int( (pow((1 + pow(5, .5)), i) - pow((1 - pow(5, .5)), i)) / (pow(2, i) * pow(5, .5)) )
        if binet == num: return True
        elif binet > num: return False

def prime_calculation(num :int):
    i, j, divider = 1, 2, 2
    while i <= num:
        if j % divider == 0:
            if j == divider:
                if j == num: return True
                i += 1 
            divider = 2
            j += 1
        else:
            divider = divider + 1
    return False

def enter_number():
    return int(input("Introduce un número entero positivo: "))


if __name__ == "__main__":
    output_string = ''
    
    print("Programa para indicar si un número es primo, fibonacci y par o impar")
    try:
        i = enter_number()
    except:
        print("Error número.")
        i = enter_number()

    if i < 0: print("Error número."); i = enter_number()

    output_string = str(i)
    output_string += ('' if prime_calculation(i) else ' no') + ' es primo, '
    output_string += ('' if binet_fibonacci_calculation(i) else 'no ') + 'es fibonacci y '
    output_string += 'es par.' if i%2 == 0 else 'es impar.'
    print(output_string)

