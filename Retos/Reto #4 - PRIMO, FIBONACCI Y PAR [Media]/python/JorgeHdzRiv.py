"""
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
"""

# Generaremos una serie de numeros de fibbonaci
def generate_fibo(limit):
    a,b = 1,1
    while a < limit:
        yield a
        a,b = b, a+b

# Si se requiere un numero mas grande aumentar el limite
serie_fibo = [f for f in generate_fibo(limit=100)]

def primo(number):
    if number < 2:
        c1 = 'no es primo'
    elif number == 2:
        c1 = 'es primo'
    elif number > 2 and number %2 ==0:
        c1 = 'no es primo'
    else:
        for i in range(3,number):
            if number %i == 0:
                c1 = 'no es primo'
        c1 = 'es primo'
    
    return c1

def fibo(number):
    if number in serie_fibo:
        c2 = 'fibonacci'
    else:
        c2 = 'no es fibonacci'
    return c2
        
def par(number):
    if number %2 == 0:
        c3 = 'es par'
    else:
        c3 = 'es impar'
    return c3 
    
def what_number(number:int):
    c1 = primo(number)
    c2 = fibo(number)
    c3 = par(number)    
    
    print(f'El numero {number} {c1},{c2} y {c3}')   
    
    
what_number(2)
print()
what_number(7)
    

############### Main ####################
while True: 
    try:
        number = int(input('Digite un numero entero: '))    
        what_number(number)
        break
    
    except:
        print('No es un numero entero, intente de nuevo')
