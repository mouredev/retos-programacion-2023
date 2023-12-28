def check_prime(num: int) -> str:
    if num == 1:
        return "no es"
    for i in range(2, num):
        if (num % i) == 0:
            return "no es"
    else:
        return "es"


def fibonacci(num: int):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


def check_fibonacci(num: int) -> str:
    for n in range(num + 100):
        fibo = fibonacci(n)
        if fibo == num:
            return "es"
        if fibo > num:
            return "no es"


def check_pair(num: int) -> str:
    if (num % 2) == 0:
        return "par"
    else:
        return "impar"


def show_analysis(num: int):
    print(f"{num} {check_prime(num)} primo, {check_fibonacci(num)} fibonacci y es {check_pair(num)}")


while True:
    select = int(input("Ingresar número: "))
    show_analysis(select)
