""" Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
Ejemplos:
- Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
- Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar" """

def es_par(num):
    if num % 2 == 0:
        return True
    else:
        return False


def run():
    numero = int(input("Escribe un numero: "))
    if es_par(numero):
        print(numero, "es par.")
    else:
        print(numero, "es impar.")


if __name__ == "__main__":
    run()