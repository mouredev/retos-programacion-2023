def is_even(n):
    return n % 2 == 0
 
 
def is_fibonacci(n):
    a = 0
    b = 1
    while b < n:
        c = a + b
        a = b
        b = c
    return b == n


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def main(n):
    resultado = f'{n} {"" if is_prime(n) else "no "}es primo, '
    resultado += f'{"" if is_fibonacci(n) else "no "}es fibonacci '
    resultado += f'y es {"par" if is_even(n) else "impar"}.'
    print(resultado)


for n in range(10):
    main(n)
