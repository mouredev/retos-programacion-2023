import math

def es_primo(x):
  square=int(math.sqrt(x))+1
  if x==2:
    return True
  for i in range (2, square+1):
      if x%i==0:
        return False
  return True

def buscar_primos(n):
  primos=[]
  for i in range (2, n+1):
      if es_primo(i):
         primos.append(i)
  return primos

def buscar_parejas(primos):
  parejas=[]
  for i in range (len(primos)-1):
    resta=primos[i+1]-primos[i]
    if resta==2:
      parejas.append((primos[i], primos[i+1]))
  return parejas

if __name__=="__main__":
    while(True):
      n=int(input("Ingresa el número que determina el rango de busqueda: "))
      if n>=1:
        break
    parejas=buscar_parejas(buscar_primos(n))
    for pareja in parejas:
      if pareja==parejas[-1]:
        print(pareja, end="")
      else:
       print(pareja, end=", ")
