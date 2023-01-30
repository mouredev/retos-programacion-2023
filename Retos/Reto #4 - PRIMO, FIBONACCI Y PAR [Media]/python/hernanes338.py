def prime_fibonacci_even(number):
    prime = True
    fibonacci = False
    even = False
    
    list_fibonacci = [0,1]
    count = 30

    while count >= 1:
        next_number = list_fibonacci[-1] + list_fibonacci[-2]
        list_fibonacci.append(next_number)
        count -= 1
    
    if number > 1:
        for i in range(2, number-1):
            if number % i == 0:
                prime = False
                break
    else:
        prime = False
    
    if number % 2 == 0:
        even = True

    if number in list_fibonacci:
        fibonacci = True
        
    resultado = '{} is '.format(number)
    
    resultado += 'prime, ' if prime else 'not prime, '
    resultado += 'fibonacci and ' if fibonacci else 'not fibonacci and ' 
    resultado += 'even.' if even else 'odd.'
    return resultado

print('Check if a number is prime, fibonacci and even')

while True:
    number = int(input('Please insert a number greater than 0 without decimals: '))

    if number > 0:
        break

print(prime_fibonacci_even(number))
