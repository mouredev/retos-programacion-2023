import time


def cuenta_atras(inicio, intervalo):
    # Verificar que los parámetros sean enteros positivos
    if (
        not isinstance(inicio, int)
        or not isinstance(intervalo, int)
        or inicio <= 0
        or intervalo <= 0
    ):
        print("Error: Los parámetros deben ser enteros positivos.")
        return

    # Ciclo de cuenta regresiva utilizando un for
    for i in range(inicio, 0, -1):
        print(i)  # Imprimir el número actual
        time.sleep(intervalo)  # Esperar el intervalo de tiempo especificado en segundos

    print("¡Cuenta regresiva finalizada!")


if __name__ == "__main__":
    cuenta_atras(10, 1)
