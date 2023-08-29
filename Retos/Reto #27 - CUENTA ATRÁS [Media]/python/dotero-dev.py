import time
parametro1 = int(input(""))
parametro2 = int(input(""))
while True:
    if not parametro1 > parametro2: 
        parametro1 = int(input(""))
        parametro2 = int(input(""))
    else:
        break
cuenta = parametro1
for i in range(parametro1):
    print(cuenta)
    time.sleep(parametro2)
    cuenta-=1
print(cuenta)