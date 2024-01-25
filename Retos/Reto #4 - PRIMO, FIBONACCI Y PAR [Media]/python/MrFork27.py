import math


def show_number_info(number):
    prime_message = "no es primo"
    fibonacci_message = "no es fibonacci"
    even_message = "es impar"

    if is_prime(number):
        prime_message = "es primo"

    if is_fibonacci(number):
        fibonacci_message = "es fibonacci"

    if is_even(number):
        even_message = "es par"

    print(f"{number} {prime_message}, {fibonacci_message} y {even_message}")


def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


def is_fibonacci(number):
    current_fibonacci_number = 1
    previous_fibonacci_number = 1

    while current_fibonacci_number <= number:
        if current_fibonacci_number == number:
            return True

        current_fibonacci_number = current_fibonacci_number + previous_fibonacci_number
        previous_fibonacci_number = current_fibonacci_number - previous_fibonacci_number

    return False


def is_even(number):
    return number % 2 == 0


number = 2
show_number_info(number)
number = 7
show_number_info(number)
number = 1
show_number_info(number)
number = 8
show_number_info(number)
number = 1597
show_number_info(number)
number = 0
show_number_info(number)
number = -2
show_number_info(number)
