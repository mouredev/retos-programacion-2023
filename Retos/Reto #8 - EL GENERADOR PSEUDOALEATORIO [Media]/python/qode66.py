"""
/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */
"""

import math
from datetime import datetime

sigma2 = 6.0
sigma = math.sqrt(sigma2)
mu = 0

def funcionGauss(x,s,m):

    a = 1 #altura de la campana, valor formal a = 1/(sigma*math.sqrt(2*math.pi))
    b = m #posicion del centro
    c = s #anchura de la campana

    y = a * math.exp(-((x - b)**2)/(2 * c**2)) #funcion de Gauss

    return y

dt = datetime.now()
seed = ((2*sigma2) * (dt.microsecond/1000000)) - sigma2

numAlea = round(100*(funcionGauss(seed,sigma,mu)))

print(numAlea)
