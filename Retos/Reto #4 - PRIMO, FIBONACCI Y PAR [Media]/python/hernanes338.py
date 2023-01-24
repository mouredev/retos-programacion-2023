# 2 es primo, fibonacci y es par

def prime_fibonacci_even(number):
    prime = True
    fibonacci = False
    even = False
    
    if number > 1:
        for i in range(2, number-1):
            if number % i == 0:
                prime = False
                break
    else:
        prime = False
    
    if number % 2 == 0:
        even = True
    return prime

print('Check if a number is prime, fibonacci and even')

while True:
    number = int(input('Please insert a number greater than 0 without decimals: '))

    if number > 0:
        break

print(prime_fibonacci_even(number))
