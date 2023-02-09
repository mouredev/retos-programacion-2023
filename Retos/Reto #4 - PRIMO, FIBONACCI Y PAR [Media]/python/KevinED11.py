def es_par(number: int) -> bool:
    return number % 2 == 0 if number > 0 else False


def es_primo(number: int) -> bool:
    return (number > 1) and not any(number % num == 0 for num in range(2, number))


def es_fibonacci(number: int) -> bool:
    fibonacci_numbers = [0, 1]
    for _ in range(1, number + 1):
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    return number in fibonacci_numbers


def main(number: int) -> str:
    try:
        number = abs(int(number))
        result1, result2, result3 = es_primo(number), es_par(number), es_fibonacci(number)

        if all((result1, result2, result3)):
            return f'El numero "{number}" que proporcionaste es un número primo, fibonacci y ademas es par'
        else:
            return f'el numero proporcionado "{number}" es un numero primo, no es fibonacci y ademas es impar' if result1 and not all(
                (result2,
                 result3)) else f'el número "{number}" un un número primo' if result1 else f'el número "{number}" es un número par' if result2 else f'el número {number} es un número fibonacci'

    except ValueError:
        return 'Proporciona solo números enteros'


if __name__ == '__main__':
    comprobacion1 = main(number=7)
    print(comprobacion1)
    comprobacion2 = main(number=2)
    print(comprobacion2)
