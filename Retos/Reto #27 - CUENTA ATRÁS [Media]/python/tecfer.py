'''
Crea una función que reciba dos parámetros para crear una cuenta atrás.
- El primero, representa el número en el que comienza la cuenta.
- El segundo, los segundos que tienen que transcurrir entre cada cuenta.
- Sólo se aceptan números enteros positivos.
- El programa finaliza al llegar a cero.
- Debes imprimir cada número de la cuenta atrás.
'''
import threading
import time

def count_down_pause(start:int, pause:int) -> None:
    start = max(start, 0)
    pause = max(pause, 0)
    for x in range(start,-1,-1):
        print(x)
        if x==0:
            return
        time.sleep(pause)


def main() -> None:
    t = threading.Thread(target=count_down_pause, args=(5, 1))
    t.start()

    t.join()
    print("Finalizado")


if __name__=='__main__':
    main()