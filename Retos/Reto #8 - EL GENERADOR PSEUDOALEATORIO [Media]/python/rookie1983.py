import time

cont = 0
while cont < 100:
    hora_actual = time.time()
    udd = int(str(hora_actual)[-3:])
    convertir = udd % 101
    print("UDD: " + str(udd))
    print("Numero SA: " + str(convertir))
    cont = cont + 1
    time.sleep(0.05)
    