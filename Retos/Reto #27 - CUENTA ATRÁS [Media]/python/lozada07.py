import time

# Reto #27: Cuenta atrás
#### Dificultad: Media | Publicación: 03/07/23 | Corrección: 10/07/23

## Enunciado

"""
/*
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
 */
"""
#### Tienes toda la información extendida sobre los retos de programación semanales en **[retosdeprogramacion.com/semanales2023](https://retosdeprogramacion.com/semanales2023)**.


def cuenta_atras(numero, segundos):
    while numero >= 0:
        print(numero)
        time.sleep(segundos)
        numero -= 1


if __name__ == "__main__":
    cuenta_atras(10, 3)
    
