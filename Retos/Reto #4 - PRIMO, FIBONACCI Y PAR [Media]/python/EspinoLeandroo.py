def primo(n):
    if n <= 1:
        return False
    
    for i in range(2,n):
        if n % i == 0:
            return False

    return True


def es_fibonacci(n):
    num1 = 0
    num2 = 1
    counter = 0

    while num1 <= n:
        if num1 == n:
            return True

        num3 = num2 + num1
        num1 = num2
        num2 = num3
        counter += 1
    
    return False


def es_par(n):
    return n % 2 == 0

n =  int(input("Ingresa Número: "))

message = "El número " + str(n)

if primo(n):
    message += " es primo, "
else:
    message += " no es primo, "

if es_fibonacci(n):
    message += "es fibonacci, "
else:
    message += "no es fibonacci, "

if es_par(n):
    message += "es par."
else:
    message += "es impar."


print(message)


