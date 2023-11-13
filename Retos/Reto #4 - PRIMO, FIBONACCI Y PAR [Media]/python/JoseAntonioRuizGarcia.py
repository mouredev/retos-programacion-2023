def isPrimeNumber(number: int) -> bool:
    list_numbers = range(1, number)
    number_control = 1
    is_prime_number = False
    
    for num in list_numbers:
        number_control *= num
    
    number_control += 1
    if number_control % number == 0:
        is_prime_number = True

    return is_prime_number

def isFibonacciNumber(number: int) -> bool:
    fibonacci_numbers = [1, 2]
    is_fibonacci = False

    while fibonacci_numbers[-1] < number:
        fibonacci_numbers.append(sum(fibonacci_numbers[-2:]))

    if number in fibonacci_numbers:
        is_fibonacci = True

    return is_fibonacci

def isEvenNumber(number: int) -> bool:
    is_even = False

    if number % 2 == 0:
        is_even = True

    return is_even

def controlNumber(number: int) -> None:
    answer = f'El número {number} '

    if isPrimeNumber(number):
        answer += 'es primo, '
    else:
        answer += 'no es primo, '

    if isFibonacciNumber(number):
        answer += 'es Fibonacci y '
    else:
        answer += 'no es Fibonacci y '
    
    if isEvenNumber(number):
        answer += 'es par.'
    else:
        answer += 'es impar.'

    print(answer)

if __name__=='__main__':
    number = int(input('Introduce un número: '))
    controlNumber(number)
