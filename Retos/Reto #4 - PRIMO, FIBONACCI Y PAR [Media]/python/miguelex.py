def CheckNumber(number):
    isPrime = "es primo, " if isPrimeNumber(
        number) else "no es primo, "
    isEven = "es par y " if isEvenNumber(
        number) else "no es par y "
    isFibonacci = "es un numero de Fibonacci" if isFibonacciNumber(
        number) else "no es numero de Fibonacci"
    print('El numero {0} {1}{2}{3}'.format(
        number, isPrime, isEven, isFibonacci))


def isPrimeNumber(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def isEvenNumber(number):
    if number % 2 == 0:
        return True
    else:
        return False


def isFibonacciNumber(number):
    a, b = 0, 1
    while a < number:
        a, b = b, a + b
    return a == number


CheckNumber(1)
CheckNumber(2)
CheckNumber(3)
CheckNumber(4)
CheckNumber(5)
CheckNumber(6)
CheckNumber(7)
CheckNumber(8)
CheckNumber(9)
CheckNumber(10)
CheckNumber(1024)
CheckNumber(358742586)
