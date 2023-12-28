import time

#Formula xn+1 = (a * xn + c) % m

def numero_pseudoaleatorio():
    a = 34567891
    c = 12345
    m = 101
    semilla = int(round(time.time() * 1000))

    numero_pseudorand = (semilla * a + c) % m
    
    print(numero_pseudorand)

numero_pseudoaleatorio()
