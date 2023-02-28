import time
#importamos time para sacar el tiempo en que se ejecuta

def rand(seed):
    random_seed = (7**5) * seed % (-1 + 2**31) #hacemos la formula de rand
    print(random_seed % 101) # la semilla le sacamos modulo para que de un numero entre 0 y 100

seed = int(time.time()) 
rand(seed)
