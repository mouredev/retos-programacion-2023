'''
 Crea un generador de números pseudoaleatorios entre 0 y 100.
 No puedes usar ninguna función "random" (o semejante) del 
 lenguaje de programación seleccionado.

 Es más complicado de lo que parece...

'''
import time;

def genera_aleatorio():
    aleatorio = str(time.time())
    if aleatorio[len(aleatorio)-3:len(aleatorio)] == "000":
        print("00")
    elif aleatorio[len(aleatorio)-3:len(aleatorio)] == "100":
        print("100")
    else:
        print(aleatorio[len(aleatorio)-2:len(aleatorio)])

if __name__ == '__main__':
    while True:
        play = input('Para generar un número aleatorio, presiona "Enter" ("s" para salir):\n')
        if play.lower() == "s":
            break
        else:
            genera_aleatorio()