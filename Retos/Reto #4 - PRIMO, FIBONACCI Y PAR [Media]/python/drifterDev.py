def fibonacci(y):
  lista=[0,1]
  while lista[-1]<y:
    lista.append(lista[-1]+lista[-2])
  if y in lista:
    return " es fibonacci"
  else:
    return " no es fibonacci"
def primo(x):
  lista2=[]
  for i in range(1, x):
    if x%i==0:
      lista2.append(i)
  if x in lista2:
    return " es primo"
  else:
    return " no es primo"
def par(z):
  if z%2==0:
    return " es par"
  else:
    return " es impar"
numero=int(input("Ingresa el numero a analizar: "))
print(str(numero)+primo(numero)+","+fibonacci(numero)+" y"+par(numero))


