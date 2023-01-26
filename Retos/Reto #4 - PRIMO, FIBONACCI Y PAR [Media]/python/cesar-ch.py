#  * Escribe un programa que, dado un número, compruebe y muestre si es primo,
#  * fibonacci y par.
#  * Ejemplos:
#  * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
#  * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"

def checkNumber(e):
    answer = f"{e} "

    def primeNumber(e):
        prime = True
        for i in range(2, e):
            prime = False if e % i == 0 else prime

        return "es primo, " if prime else "no es primo, "

    def fibonacciNumber(e):
        fibonacci = False
        numOne = 1
        numTwo = 1
        for i in range(2, e+1):
            [numOne, numTwo] = [numTwo, numOne + numTwo]
            fibonacci = True if e == numTwo else fibonacci

        return "fibonacci " if fibonacci else "no es fibonacci "

    def parNumber(e):
        return "y es par" if e % 2 == 0 else "y es impar"

    answer += primeNumber(e)
    answer += fibonacciNumber(e)
    answer += parNumber(e)

    return answer


print(checkNumber(2))  # 2 es primo, fibonacci y es par
print(checkNumber(7))  # 7 es primo, no es fibonacci y es impar
