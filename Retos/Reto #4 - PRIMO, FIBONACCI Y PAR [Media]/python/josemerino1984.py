"""
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */"""

def par(num):
    if num%2==0:
        return("es par")
    else:
        return("es impar ")
    

def primo(num):
    cont=0
    for i in range(num):
        if num%(i+1)==0:
            cont=cont+1
    if cont==2:
        return("es primo")
    else: 
        return("no es primo")



def fibonacci(num):
    i=0
    b=1
    fib=1
    while fib <=num:  
        fib=i+fib    
        i=b    
        b=fib     
        if fib==num:
            return("es fibonacci")
    return(" no es fibonacci")




while True:
    try:
       num=int(input("digite un numero entero: "))
       dpar=par(num)
       dprimo=primo(num)
       dfibb=fibonacci(num)
       print(f"el {num},{dpar},{dprimo}, {dfibb}")
       break


    except ValueError:
       print("error, digite un numero entero")