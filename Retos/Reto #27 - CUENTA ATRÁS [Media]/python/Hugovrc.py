import time

def cuenta_atras(inicio: int, segundos: int):
    contador = 0
    try:
        if segundos < 0 or inicio < 0 :
            print("Solo se aceptan Numeros Enteros Positivos")
        else:    
            while inicio >= 0:
                contador = inicio
                print(contador)
                inicio -= 1
                if contador == 0:
                    break
                time.sleep(segundos)
    except:
        print("Solo se aceptan Numeros Enteros Positivos")

cuenta_atras(5,3)