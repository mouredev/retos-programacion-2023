import math
 
def primo_Fibo_Par(n):
    #par o impar ?
    if n%2==0: par, primo = " y es par", " no es primo, "
    else: 
        par = " y es impar"
        for i in range(3,n//2):
            if n != i and n%i == 0: 
                primo = " no es primo, "
                break
            else: primo = " es primo, "
    
    #El nro 2, excepcion
    if n == 2: par, primo = " y es par", " es primo, "
    
    # Un numero pertenece a la secuencia de Fibonacci 
    # si y sólo si 5 * n^2 + 4 ó 5 * n^2 – 4 es un cuadrado perfecto.
    a = 5 * n**2 + 4
    b = 5 * n**2 - 4
    if math.sqrt(a)-int(math.sqrt(a)) == 0 or math.sqrt(b)-int(math.sqrt(b)) == 0: fibo = "fibonacci"
    else: fibo = "no es fibonacci"
    
    return str(n)+primo+fibo+par

print(primo_Fibo_Par(8))
