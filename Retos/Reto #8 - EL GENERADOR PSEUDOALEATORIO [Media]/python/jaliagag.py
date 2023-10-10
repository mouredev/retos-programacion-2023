#
#Crea un generador de números pseudoaleatorios entre 0 y 100.
#No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
#
#

import datetime
import time

a = int(input('Cuántos números: '))
def my_random(q: int) -> int:
    final = 0
    i = 0
    while i < q:
        now = str(datetime.datetime.now())
        uno = [*now.split(' ')[1].split('.')[1][-1]]
        time.sleep(0.0003)
        dos = [*now.split(' ')[1].split('.')[1][-2]]
        final = int(uno[0]+dos[0])
        print(final)
        i += 1
    return final
    

if __name__ == '__main__':
    my_random(a)