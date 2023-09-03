#Crea un generador de números pseudoaleatorios entre 0 y 100.
#Se utilizara un generador linael congruecial GLC ==> Xn+1 = (a * Xn + c) % m
#Donde:
#    Xn es el número pseudoaleatorio actual.
#    Xn+1 es el siguiente número pseudoaleatorio en la secuencia.
#   'a' es el multiplicador.
#   'c' es el incremento.
#   'm' es el módulo.
#
import math
import time

#***Parámetros***
A=1664525
X=int(time.time()) # generar una semilla aleatoria
C=1013904223
M=2**(2+2*math.log(5,2)) # modulo para generar numeros entre 0 y 100

for _ in range(100):
    GLC=(A*X+C)%M
    X=GLC
    print(round(GLC))
