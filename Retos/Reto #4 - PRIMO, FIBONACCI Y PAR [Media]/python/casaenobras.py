

def is_even(num: int) -> bool:
    if num == 0:
        return True

    return True if num % 2 == 0 else False


def is_prime(num: int) -> bool | None:
    if num <= 0:
        return False

    i = 2

    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True


def is_fibonacci(num: int) -> bool | None:
    if num <= 0:
        return False

    fibo = 0
    next_fibo = 1
    while fibo <= num:
        if fibo == num:
            return True
        aux = fibo + next_fibo
        fibo = next_fibo
        next_fibo = aux
    return False


def number_ckeck(num: int) -> str:

    result = f"El número {num}"
    result += f" es primo," if is_prime(num) else " no es primo,"
    result += f" es fibonacci " if is_fibonacci(num) else " no es fibonacci "
    result += f"y es par." if is_even(num) else "y es impar."

    return result


print(number_ckeck(5))
print(number_ckeck(21))
print(number_ckeck(57))
print(number_ckeck(76))

