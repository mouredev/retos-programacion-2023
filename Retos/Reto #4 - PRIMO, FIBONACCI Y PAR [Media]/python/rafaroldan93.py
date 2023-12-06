def is_prime(number):
    c = 0
    for i in range(1, number + 1):
        if number % i == 0:
            c += 1
    if c < 3:
        return "es primo"
    else:
        return "no es primo"
    
def is_fibonacci(number):
    list_fibonacci = [0, 1]
    while list_fibonacci[-1] <= number:
        fibonacci = list_fibonacci[-1] + list_fibonacci[-2]
        list_fibonacci.append(fibonacci)
    if number in list_fibonacci:
        return "es Fibonacci"
    else:
        return "no es Fibonacci"

def is_even(number):
    if number % 2 == 0:
        return "es par"
    else:
        return "es impar"
    
if __name__ == "__main__":
    number = int(input("Introduce el número: "))
    print(f"El número {number} {is_prime(number)}, {is_fibonacci(number)} y {is_even(number)}")