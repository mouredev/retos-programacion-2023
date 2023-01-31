import math


def eval_number(number: int) -> str:
    out_str = f'{number} '
    out_str += 'es primo, ' if is_prime(number) else 'no es primo, '
    out_str += 'fibbonacci ' if is_fibbonacci(number) else 'no es fibbonacci '
    out_str += 'y es par ' if number % 2 == 0 else 'y es impar'
    return out_str


def is_prime(number: int) -> bool:
    return len([x for x in range(2, number) if number % x == 0]) == 0


def is_perfect_square(square: int) -> bool:
    return math.pow(int(math.sqrt(square)), 2) == square


def is_fibbonacci(number: int) -> bool:
    return is_perfect_square(5 * number * number + 4) or is_perfect_square(5 * number * number - 4)


def start() -> None:
    print(eval_number(2))
    print(eval_number(7))
    print(eval_number(49))
    print(eval_number(64))
    print(eval_number(13))


if __name__ == '__main__':
    start()
