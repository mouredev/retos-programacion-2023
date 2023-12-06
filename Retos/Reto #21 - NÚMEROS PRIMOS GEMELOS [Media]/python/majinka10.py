import math

def is_prime(n:int):
  if n>1:
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i) == 0:
            return False
    return True
  else:
      return False

def primos_gemelos(rango:int):
    primos=[]
    gemelos=[]
    for i in range(1,rango):
       if is_prime(i):
          primos.append(i)
    for n,j in enumerate(primos):
       if n<len(primos)-1:
        if primos[n+1]-j==2:
            tupla=(j,primos[n+1])
            gemelos.append(tupla)
    return gemelos

print(primos_gemelos(100))
