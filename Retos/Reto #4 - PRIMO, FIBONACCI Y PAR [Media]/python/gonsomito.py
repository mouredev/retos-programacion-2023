"""
 Reto #4 - PRIMO, FIBONACCI Y PAR [Media]
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""
#------------------------------------------- FUNCIONES
def dame_numero():                          #comprobemos que solo no cargamos números enteros
   while True:
       entrada = input("Dame un número: ")
       try:
           entrada = int(entrada)
           return entrada
       except ValueError:
           print ("VALOR INCORRECTO.\n")

def es_primo(num):                          #comprobemos si es primo o no
    if num == 0 or num == 1:
        return "no es primo, "
    else:
        for n in range(2,num):
            if num%n == 0:
                return "no es primo,"
        return "es primo,"

def es_par_impar(num):                     #comprobemos si es par o impar
    if num%2 == 0:
        return "es par"
    else:
        return "es impar"
    
def es_fibonacci(num):                      #comprobemos si está en fibonacci
    prev_n = 0
    next_n = 1        
    if prev_n == num or next_n == num:
        return "y es fibonacci."
    for n in range(num+1):
        actual_n = prev_n + next_n
        prev_n = next_n
        next_n = actual_n
        if actual_n == num:
            return "y es fibonacci."
    return "y no es fibonacci."    
        
#--------------------------------------COMENCEMOS
que_numero = dame_numero() 			#pedimos número

primo = es_primo(que_numero)                
par_impar = es_par_impar(que_numero)
fibo = es_fibonacci(que_numero)

print(que_numero, primo, par_impar, fibo )
