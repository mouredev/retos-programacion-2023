import datetime

class numero:
    def __init__(self,numero,rango_inferior, rango_superior):
        self.numeros=numero
        self.rango_inferior=rango_inferior
        self.rango_superior=rango_superior

def generador_numeros_pseudoaleatorios():
    seed = datetime.datetime.now().microsecond
    numeros=[]
    probabilidad=1/len(range(0,101))
    acumulado=probabilidad
    rango_inferior=0
    rango_superior=acumulado-0.001
    for number in range(0,101):
        numeros.append(numero(number,rango_inferior,rango_superior))
        acumulado+=probabilidad
        rango_inferior=rango_superior
        rango_superior=acumulado-0.001

    for j in numeros:
        if seed in range(int(j.rango_inferior*1000000),int(j.rango_superior*1000000)):
            print(j.numeros)
    
generador_numeros_pseudoaleatorios()
    
