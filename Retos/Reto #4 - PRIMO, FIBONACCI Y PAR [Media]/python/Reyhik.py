def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True
    
def fib(n):
    if n < 2:
        return n
    else:
        # fn = fn-1 + fn-2
        return fib(n-1) + fib(n-2)
    
def comprobacion(num):
    x = 0
    a = []
    while True:
        a.append(fib(x))
        if num <= fib(x):
            break
        x += 1
    if es_primo(num):
        if num % 2 == 0:
            if num in a:
                print ("{} es primo, es fibonacci y es par".format(num))
                return True
            print ("{} es primo, no es fibonacci y es par".format(num))
            return True
        else:
            if num in a:
                print ("{} es primo, es fibonacci y es impar".format(num))
                return True
            print ("{} es primo, no es fibonacci y es impar".format(num))
    else:
        if num % 2 == 0:
            if num in a:
                print ("{} no es primo, es fibonacci y es par".format(num))
                return True
            print ("{} no es primo, no es fibonacci y es par".format(num))
            return True    
        else:
            if num in a:
                print ("{} no es primo, es fibonacci y es impar".format(num))
                return True
            print ("{} no es primo, no es fibonacci y es impar".format(num))
        
comprobacion(34)
comprobacion(0)
comprobacion(7)
