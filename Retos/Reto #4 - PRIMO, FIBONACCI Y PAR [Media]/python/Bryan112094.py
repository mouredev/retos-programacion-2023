# Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
# Ejemplos:
# - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
# - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"

def comprobarNumero(num):
    # Numero primo 
    primo = " es primo, "
    if num == 0 or num == 1 or num == 4:
        primo = " no primo, "
    for x in range(2, int(num/2)):
        if num % x == 0:
            primo = " no primo, "

    # Si es fibonacci
    a = 1
    b = 1
    total = 0
    if num == 0 or num == 1:
        fibonacci = "fibonacci "
    else:
        fibonacci = "no es fibonacci "
        while total < num:
            total = a + b
            b = a
            a = total
            if total == num:
                fibonacci = "fibonacci "

    # Si es par
    if num%2==0:
        par = "y es par"
    else:
        par = "y es impar"

    print(str(num) + primo + fibonacci + par)

comprobarNumero(7)
