'''
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
'''

# HAcer una funcion que genere todos los fibo hasta el numero
# hacer una funicòn que diga si es fibo
# hacer una funcion que genere los primos

def es_fibo(n):
    fibo = [1,2]
    for i in range(1, n+1):
        fibo.append(fibo[i]+fibo[i-1])
        if fibo[i]>n:
            break
    if n in fibo:
        return True
    else:
        return False
    
def es_primo(n):
    primos=[]
    for i in range(1, n +1):
        primo = 1
        for j in range(2,i):
            if i % j == 0:
                primo = 0
        if primo == 1:
            primos.append(i)
    if n in primos:
        return True
    else:
        return False

def es_par(n):
    if n%2 == 0:
        return True
    else:
        return False

def staus(n):
    if es_primo(n):
        primo = "es primo"
    else:
        primo = "no es primo"
    
    if es_fibo(n):
        fibo = "es fibonacci"
    else:
        fibo = "no es fibonacci"
    
    if es_par(n):
        par = "es par"
    else:
        par = "no es par"       
    return (str(n) + " - " + primo + ", " + fibo + " y " + par)
print(staus(5))
print(staus(18))
print(staus(2))
print(staus(3))