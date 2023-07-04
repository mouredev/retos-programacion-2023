# Reto #27: Cuenta atrás
#### Dificultad: Media | Publicación: 03/07/23 | Corrección: 10/07/23

## Enunciado


#
# Crea una función que reciba dos parámetros para crear una cuenta atrás.
# - El primero, representa el número en el que comienza la cuenta.
# - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
# - Sólo se aceptan números enteros positivos.
# - El programa finaliza al llegar a cero.
# - Debes imprimir cada número de la cuenta atrás.
#

import time

class CuentaAtras:
    def __init__(self, numero_inicial, segundos_entre_cuentas):
 
        if not isinstance(numero_inicial, int) or not isinstance(segundos_entre_cuentas, int):
            raise ValueError("Ambos parámetros deben ser números enteros.")
        if numero_inicial <= 0 or segundos_entre_cuentas <= 0:
            raise ValueError("Ambos parámetros deben ser enteros positivos.")
        if isinstance(numero_inicial, str) or isinstance(segundos_entre_cuentas, str):
            raise ValueError("Ambos parámetros no pueden ser cadenas de caracteres.")

        

        self.numero_inicial = numero_inicial
        self.segundos_entre_cuentas = segundos_entre_cuentas

    def iniciar_cuenta_atras(self):

        while self.numero_inicial > 0:
            print(self.numero_inicial)
            time.sleep(self.segundos_entre_cuentas)
            self.numero_inicial -= 1

        print("Cuenta atrás finalizada...")

if __name__ == "__main__":
    cuenta = CuentaAtras(5, 3)
    cuenta.iniciar_cuenta_atras()