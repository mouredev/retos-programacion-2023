#  Ejemplos:
# - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
# - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"


def par(num):
    if num % 2 == 0:
        print("El Numero", num, "es par")
    else:
        print("El Numero", num, "es Impar")

def primo(num):
    contador=num-1
    primo=0
    noprimo=False
    if num == 2:
        primo=1
        noprimo=True
    else:
        while contador > 1:
            if num % contador == 0:
                primo+=1
                if primo > 1:
                    noprimo=False
                    break          
            else:    
                noprimo=True
            contador -= 1
       
    if noprimo:
        print("El Numero", num, "es primo")
    else:
        print("El Numero", num, "no es primo")
        

def fibonacci(fibo):
    if fibo < 1:
        fibo = 0
        return fibo     
    elif fibo == 1:
        fibo = 1
        return fibo
    else:
        fibo = fibonacci(fibo-1) + fibonacci(fibo-2)
        return fibo
   

def calcular(num):

    par(num)

    if num == 1:
        print("El Numero", num, "no es primo")
    else:
        primo(num)

    i=1
    while i >= 1:   
        if fibonacci(i) == num:
            print("El Numero", num, "es Fibonacci")
            break
        elif fibonacci(i) > num:
            print("El Numero", num, "no es Fibonacci")
            break
        else:
            i+=1
        


num = int(input("Indique el Numero: "))
calcular(num)

