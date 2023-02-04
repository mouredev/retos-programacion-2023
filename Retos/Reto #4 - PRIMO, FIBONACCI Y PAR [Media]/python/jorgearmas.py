"""
 Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 Ejemplos:
 - Con el número 2, nos dirá: "2 es primo fibonacci y es par"
 - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""
def fibonacci(usr_number):
    prev_number = 0
    next_number = 1
    main_number = 0
    fib = ""
    while main_number < usr_number:
        main_number = next_number + prev_number
        if main_number == usr_number:
            fib = " IS a fibonacci number"
        else:
            fib = " IS NOT a fibonacci number"
        prev_number = next_number
        next_number = main_number
    return(f"{usr_number}{fib}")

def even(usr_number):
    even = ""
    if usr_number%2 == 0:
        even = " IS an EVEN number"
    else:
        even = " IS an ODD number"
    return(f"{usr_number}{even}")

def prime(usr_number):
    counter = usr_number
    determ = 0
    prim = ""
    if usr_number == 1:
        prim = " IS NOT a prime number"
    else:
        while counter != 0:
            if usr_number%counter == 0:
                determ += 1
            counter -= 1
        if determ > 2:
            prim = " IS NOT a prime number"
        else:
            prim = " IS a prime number"
    return(f"{usr_number}{prim}")

if __name__ == "__main__":
    usr_number = int(input("Ingrese numero: "))
    resultEv = even(usr_number)
    resultPr = prime(usr_number)
    resultFib = fibonacci(usr_number)
    print(f"{resultEv} - {resultPr} - {resultFib}")

