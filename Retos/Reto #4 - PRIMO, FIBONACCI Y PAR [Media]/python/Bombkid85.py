
def main(num):
    number_data = (f"{num} {prime(num)}, {fibonacci(num)} y {pair(num)}")
    return number_data 


def pair(num):
    if num % 2 == 0:
        pair = "es par"
        return pair
    else:
        pair = "es impar"
        return pair

def prime(num):
    if num < 2:
        prime = "no es primo"
        return prime
    for i in range(2, num):
        if num % i == 0:
            prime = "no es primo"
            return prime
    prime = "es primo"
    return prime

def fibonacci(num):
    if num == 0:
        fibonacci = " es fibonacci"
        return fibonacci
    fibonacci_num = 1
    prev_fibonacci = 0
    while fibonacci_num <= num:
        if fibonacci_num == num:
            fibonacci = "es fibonacci"
            return fibonacci
        else:
            fibonacci_num = prev_fibonacci + fibonacci_num
            prev_fibonacci = fibonacci_num - prev_fibonacci
            
    fibonacci = "no es fibonacci"
    return fibonacci

print(main(2))
print(main(7))
print(main(13))
print(main(1))
print(main(0))
