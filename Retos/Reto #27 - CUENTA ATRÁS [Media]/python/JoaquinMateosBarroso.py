import time
import threading

def countdown(init: int, space: int) -> None:
    """Crea una función que reciba dos parámetros para crear una cuenta atrás.
    - El primero, representa el número en el que comienza la cuenta.
    - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
    - Sólo se aceptan números enteros positivos.
    - El programa finaliza al llegar a cero.
    - Debes imprimir cada número de la cuenta atrás."""
    for i in range(init, -1, -space):
        print(i)
        time.sleep(space)
        
        

if __name__ == "__main__":
    threading.Thread(target=countdown, args=(10, 1)).start()