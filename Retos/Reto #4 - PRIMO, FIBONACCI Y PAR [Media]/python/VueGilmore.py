'''
Reto #4: PRIMO, FIBONACCI Y PAR

Dificultad: MEDIA

Escribe un programa que, dado un número, compruebe y muestre si es primo,
fibonacci y par.
Ejemplos:
- Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
- Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
'''
def es_fibonacci(numero):
    prev = 0
    next = 1

    secuencia = list()

    for i in range(0, numero + 2):
        secuencia.append(prev)

        next_value = prev + next
        prev = next
        next = next_value

        if prev > numero: # No necesitamos la secuencia entera, sólo encontrar (o no) el número
           break

    if numero in secuencia:
       return True
    else:
       return False


def es_numero_primo(numero):
    if numero < 2:
       return False

    for i in range(2, numero):
      if numero % i == 0:
        return False
    
    return True


def primo_fibonacci_par(numero):
   cadena_imprimir = str(numero)

   if es_numero_primo(numero):
      cadena_imprimir = cadena_imprimir + ' es primo,'
   else:
      cadena_imprimir = cadena_imprimir + ' no es primo,'

   if es_fibonacci(numero):
      cadena_imprimir = cadena_imprimir + ' es fibonacci,'
   else:
      cadena_imprimir = cadena_imprimir + ' no es fibonacci,'

   if numero % 2 == 0:
      cadena_imprimir = cadena_imprimir + ' y es par'
   else:
      cadena_imprimir = cadena_imprimir + ' y es impar'

   print(cadena_imprimir)


primo_fibonacci_par(2)
primo_fibonacci_par(7)
primo_fibonacci_par(12)
primo_fibonacci_par(8)
