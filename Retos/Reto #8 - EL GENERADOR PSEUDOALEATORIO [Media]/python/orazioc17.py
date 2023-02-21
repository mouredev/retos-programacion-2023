import time
import math

def random() -> int:
    """
    Obtendre el tiempo actual, del cual voy a obtener los decimales, y ese seria el numero "random"
    Si se llama la funcion en un ciclo, es muy probable que salgan los mismos numeros por la velocidad
    en la que se chequea el reloj, pero si se llama una sola vez en una funcionalidad que no se ejecuta
    repetitivamente, efectivamente el numero generado sera distinto
    """

    numero = time.time()
    decimal, _ = math.modf(numero)
    if int(decimal * 1000) == 100:
        return 100
    else:
        return int(decimal * 100)


if __name__ == '__main__':
    numero = random()
    print(numero)