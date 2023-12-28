from typing import List


def obtener_numero() -> int:
    while True:
        try:
            numero = int(input("Ingresa un numero: "))
            return numero
        except Exception:
            print("No ingresaste un numero, intenta de nuevo")


def es_par(numero: int) -> bool:
    return numero % 2 == 0


def generar_fibonacci(max_num: int) -> List[int]:
    lista_fibonacci = [1, 1]
    while lista_fibonacci[-1] < max_num:
        lista_fibonacci.append(lista_fibonacci[-1]+lista_fibonacci[-2])

    return lista_fibonacci


def es_fibonacci(numero: int) -> bool:
    fibonacci = generar_fibonacci(numero)
    return numero in fibonacci


def run():
    numero = obtener_numero()
    par = es_par(numero)
    par = "par" if par else "impar"
    fibonacci = es_fibonacci(numero)
    fibonacci = "es fibonacci" if fibonacci else "no es fibonacci"

    print(f"El numero {numero} es {par} y {fibonacci}")


if __name__ == '__main__':
    run()
