'''
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
'''
# Funcion que busca si es primo. Returna strings
def es_primo(var):
    aux = 0
    for i in range(var):
        if i == 0 or i == 1:
            continue
        else:
            aux += 1 if var % i == 0 else aux

    return " no" if aux >= 1 else ""


# Funcion que calcula si es fibonacci, returna string
def es_fibonacci(var):
    aux1 = 0
    aux2 = 1
    for i in range(var):
        c = aux1 + aux2
        aux1 = aux2
        aux2 = c
        if c == var:
            return ""
    return "no es " if var != 0 else ""


# funcion hecha con lambda que busca si el numero es par o impar. Returna los string tambien
def es_par(var): return "par" if var % 2 == 0 or var == 0 else "impar"


#Llamar a las funciones
def llamar_funciones(var):
    print(f'{var}{es_primo(var)} es primo, {es_fibonacci(var)}fibonacci y es {es_par(var)}')


llamar_funciones(int(input("Introduce numero: ")))
