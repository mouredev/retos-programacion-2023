def es_fibo(num: int) -> bool:
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num

def es_par(num: int) -> bool:
    return num % 2 == 0

def es_primo(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    return True


try:
    num = int(input("Introduce un número: "))
    result = "" + str(num)
    result += " es primo, " if es_primo(num) else " no es primo, "
    result += "es fibonacci y" if es_fibo(num) else "no es fibonacci y"
    result += " es par" if es_par(num) else " es impar"
    print(result)
except ValueError:
    print("Introduce un número")