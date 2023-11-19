'''
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
'''

def es_primo(numero: int) -> bool:
    if numero <= 1:
        return False  # Los números menores o iguales a 1 no son primos

    if numero <= 3:
        return True  # 2 y 3 son primos

    if numero % 2 == 0 or numero % 3 == 0:
        return False  # Los múltiplos de 2 o 3 no son primos

    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False  # Si n es divisible por i o i+2, no es primo
        i += 6

    return True

def es_fibonacci(numero: int) -> bool:
    a, b = 0, 1
    while a < numero:
        a, b = b, a + b
    if a == numero:
        return True
    else:
        return False

def es_par(numero: int) -> bool:
    if numero % 2 == 0:
        return True
    return False

def main():
    try:
        num = int(input("Ingrese un número: "))
        print(f"""El número {num} es primo: {es_primo(num)} \nEl número {num} es fibonacci: {es_fibonacci(num)} \nEl número {num} es par: {es_par(num)}""")
    except:
        print("Entrada incorrecta")

if __name__ == "__main__":
    main()
