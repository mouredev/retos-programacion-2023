import time

def cuenta_regresiva(comienzo: int, segundos:int):
    if isinstance(comienzo, int)>=0 and isinstance(segundos, int)>=0 :
        for i in range(comienzo, -1, -1):
            print(i)
            if i == 0 :
                break
            time.sleep(segundos)

cuenta_regresiva(5, 2)