"""
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
"""
def par_impar(num):
    if not(num % 2):
        return 'es par'
    return 'es impar'

def primo(num):
    for n in range(2, num):
        if not(num%n):
            return 'no es primo'
    return 'es primo'

def fibonacci(num):
    lista = [0,1]
    for n in range(2,num+2):
        lista.append(lista[n-1] + lista[n-2])
    if num in lista:
        return 'fibonacci'
    return 'no es fibonacci'

def main():
    num = 8
    print(f"{num} {primo(num)}, {fibonacci(num)} y {par_impar(num)}")

if __name__ == "__main__":
    main()
