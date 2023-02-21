def is_fibo(num):
    previous = 0
    last = 1
    aux = 0
    serie = list()
    while last <= num:
        if num == last:
            return True
        aux = previous
        previous = last
        last = aux+previous
    return False

def is_even(num):
    if(num % 2 == 0):
        return True
    return False
    
def is_prime(num):
    if(is_even(num) and num != 2):
        return False
    if(num % 3 == 0 and num != 3):
        return False
    if(num % 5 == 0 and num != 5):
        return False
    else:
        return True

def prime_fibo_even():
    num = int(input("introduzca un numero: "))
    result = ""
    if(is_prime(num)):
        result += str(num) + " es primo,"
    else:
        result += str(num) + " no es primo,"
    if(is_fibo(num)):
        result += " fibonacci,"
    else:
        result += " no es fibonacci,"
    if(is_even(num)):
        result += " es par"
    else:
        result += " es impar"
    return result

print(prime_fibo_even())

