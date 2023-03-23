import datetime

x = datetime.datetime.now()
microsegundos = int(x.strftime("%f"))
print("El número \"aleatorio\" entre 0 y 100 es: ", microsegundos%101)