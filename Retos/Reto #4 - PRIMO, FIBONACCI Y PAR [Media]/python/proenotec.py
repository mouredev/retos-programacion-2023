'''
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
 '''
# Manuel Castro C.
# Proenotec
# 2023/01/23

def es_primo(ElNumero):
    resultado = True
    if ElNumero < 2:
        resultado = True
    else:
        for index in range(2,ElNumero):
            if ElNumero % index == 0:
                resultado = False
    return resultado

def es_fibonacci(ElNumero):
    resultado = False
    numero_a = 0
    numero_b = 1
    while ((numero_a < ElNumero) | (numero_b < ElNumero)):
        siguiente = numero_a + numero_b
        numero_a = numero_b
        numero_b = siguiente
        resultado = True if ((ElNumero == numero_a) | (ElNumero == numero_b)) else False
    return resultado

def es_par(ElNumero):
    resultado = True if ElNumero % 2 == 0 else False
    return resultado

def check_number(numero):
    print("El número %i " % numero , end="")
    if es_primo(numero):
        print("es primo, " , end="")
    else:
        print("no es primo, " , end="")
    if es_fibonacci(numero):
        print("es fibonacci y " , end="")
    else:
        print("no es fibonacci y " , end="")
    if es_par(numero):
        print("es par.")
    else:
        print("es impar.")


# Testing... 
check_number(2)
check_number(7)
check_number(34)
check_number(100)
check_number(1597)
check_number(121393)