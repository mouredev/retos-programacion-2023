#!/usr/bin/env python3

def is_even(number):
    return number % 2 == 0

def is_prime(number):
    if number <= 1:
        return False
    else:
        for i in range(2,number):
            if number % i == 0:
                return False
        return True

def fibonacci(number):
    if number <= 1:
        return number
    else:
        return fibonacci(number-1) + fibonacci(number-2)

def is_fibonacci(number):
    for i in range(0, 2*number):
        fibo = fibonacci(i)
        if fibo > number:
            break
        if fibo == number:
            return True
    return False

def process_number(number):
    msg = str(number)

    if is_prime(number):
        msg = msg + " es primo,"
    else:
        msg = msg + " no es primo,"

    if is_fibonacci(number):
        msg = msg + " es fibonacci y"
    else:
        msg = msg + " no es fibonacci y"

    if is_even(number):
        msg = msg + " es par"
    else:
        msg = msg + " es impar"

    print(msg)

if __name__ == "__main__":
    process_number(2)
    process_number(7)
