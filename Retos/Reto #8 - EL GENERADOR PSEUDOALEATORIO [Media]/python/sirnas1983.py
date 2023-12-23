import time

def random():
    now = str(time.time())
    ms = now[-5:]
    rand = int(float(ms)//999)
    return rand

#Pruebas 
resp = []
for i in range(1000):
    time.sleep(0.00001) #Debe haber un minimo desfasaje de tiempo 
    resp.append(random())


print("Lista de numeros aleatorios:\n",resp)
print("Media aritmetica:",sum(resp)/len(resp))
print("Maximo:",max(resp))
print("Minimo:",min(resp))
