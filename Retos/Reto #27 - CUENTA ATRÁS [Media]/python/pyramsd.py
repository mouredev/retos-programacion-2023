import time
from colorama import Fore

def countDown(n:int, s:int):
    
    while True:
                
        if n < 0 :
            n = int(input("\nIngrese numero POSITIVO de conteo atras!: "))
        elif s < 0:
            s = int(input("\nIngrese numero POSITIVO de segundos a transcurrir!: "))

        else:
            #print(Fore.GREEN + f"{n}", end="\r")
            print(Fore.GREEN + f"{n}")
            time.sleep(s)
            n -= 1

            if n == 0:
                print(Fore.RED + f"{n}")
                break

    print("Tiempo acabado!!!" + Fore.RESET)

n = int(input("Ingrese numero de conteo atras: "))
s = int(input("Ingrese numero de segundos a transcurrir: "))

countDown(n, s)
