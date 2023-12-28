'''
 Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 Ejemplos:
 - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
'''

#Solución:
print ("Reto #4: PRIMO, FIBONACCI Y PAR\n")

def es_primo(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

def es_fibonacci(num):
    f1 = 0
    f2 = 1

    while f1 + f2 <= num:
        f_aux = f1
        f1 = f2
        f2 = f_aux + f1
        if num == f2:
            return True
        return False

def es_par(num):
    if num % 2 == 0:
        return True
    return False

def app():
    num = int(input("Ingrese un número: "))

    resultado_primo = es_primo(num)
    resultado_fibonacci = es_fibonacci(num)
    resultado_par = es_par(num)

    if resultado_primo == True:
        resultado_primo = (str(num) + " es primo,")
    else:
        resultado_primo = (str(num) + " no es primo,")

    if resultado_fibonacci == True:
        resultado_fibonacci = (resultado_primo + " es fibonacci y")
    else:
        resultado_fibonacci = (resultado_primo + " no es fibonacci y")

    if resultado_par == True:
        resultado_par = (resultado_fibonacci + " es par.")
    else:
        resultado_par = (resultado_fibonacci + " es impar.")

    print(resultado_par)

if __name__ == '__main__':
    app()