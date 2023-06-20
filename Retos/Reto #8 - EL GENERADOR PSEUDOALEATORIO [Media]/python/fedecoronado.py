import time

def prandom(min:int, max:int):
    a = time.time()*10000 #multiplico *10000 para tomar los utlimos decimales de contador de tiempo y variar más el resultado
    rnd = a - int(a)
    '''si se llama 2 veces seguidas a la funcion da el mismo resultado, 
       si se agrega esta linea es muy lenta para se soluciona el problema'''
    time.sleep(0.51) 
    return int(rnd * (max - min + 1))+ min    
  

min =0
max = 100


for i in range(0,1000):
    a = prandom(min,max)
    print(i,a)
