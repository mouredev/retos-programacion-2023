#!/usr/bin/env python3

'''
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
 '''
import math

numero = int(input("\n[i] Ingrese un número para comprobar si es primo, fibonacci o par: "))

es_primo = all((numero % i) != 0 for i in range(2, int(numero ** 0.5) + 1))

es_par = True if (numero % 2) == 0 else False

es_cuadrado_perfecto = lambda n: True if (int(math.sqrt(n)) * int(math.sqrt(n))) == n else False
es_fibonacci = True if es_cuadrado_perfecto(5 * numero * numero + 4) or es_cuadrado_perfecto(5 * numero * numero - 4) else False

resultados = []

resultados.append('primo' if es_primo else 'no es primo')
resultados.append('par' if es_par else 'impar')
resultados.append('fibonacci' if es_fibonacci else 'no es fibonacci')

respuesta = f'\n[+] {numero} es '

for resultado in resultados:

    if resultados[-1] == resultado:
        respuesta += f'y {resultado}.'
        break
    else:
        respuesta += f'{resultado}, '


print(respuesta)



