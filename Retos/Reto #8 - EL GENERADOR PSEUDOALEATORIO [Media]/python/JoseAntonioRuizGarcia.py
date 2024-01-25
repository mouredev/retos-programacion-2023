import numpy as np
import time

def randomNumber() -> None:
    # Extrae los últimos 3 números de la hora de ejecución del código
    seconds = time.time()
    number = int(str(seconds)[-3:])

    if number > 100:
        number = int(np.round(number / 10, 0))

    print(number)

if __name__=='__main__':
    randomNumber()
