"""""
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""

def escribir_texto(es_primo,es_fibonacci,es_par):
    list = []

    if(es_primo):
        list.append("es primo,")
    else:
        list.append("no es primo,")

    if(es_fibonacci):
        list.append(" es fibonacci,")
    else:
        list.append(" no es fibonacci,")

    if(es_par):
        list.append(" es par")
    else:
        list.append(" es impar")

    texto = "".join(list)
    print(numero,texto)



def primo(numero):
    es_primo = True
    i = 1 
    if(numero <= 1):
        es_primo = False
    else:    
        while(i <= numero):
            if(numero % i == 0 and i != 1 and i != numero):
                es_primo = False
                break

            i += 1

    return es_primo


def fibonnaci(numero):
    num_sec1 = 1
    num_sec2 = 1
    suma_fibonacci = 0
    i = 0
    es_fibonacci = False

    if numero == 1:
        es_fibonacci = True
    else:
        while(i < numero):
            suma_fibonacci = num_sec1 + num_sec2
            if(numero == suma_fibonacci):
                es_fibonacci = True
                break
        
            num_sec2 = num_sec1
            num_sec1 = suma_fibonacci
            i += 1

    return es_fibonacci


def par(numero):
    es_par = False
    if numero % 2 == 0:
        es_par = True
    return es_par

numero = int(input("ingresa un numero: "))
es_primo = primo(numero)
es_fibonacci = fibonnaci(numero)
es_par = par(numero)
escribir_texto(es_primo,es_fibonacci,es_par)





