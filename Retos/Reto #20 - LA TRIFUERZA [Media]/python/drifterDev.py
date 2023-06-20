def crear_piramide(n):
  piramide=[]
  fila_larga=(2*n)-1
  for i in range(1,n+1):
    longitud_fila=(2*i)-1
    fila=[]
    for j in range (int((fila_larga-longitud_fila)/2)):
      fila.append(" ")
    for k in range (longitud_fila):
      fila.append("*")
    for m in range (int((fila_larga-longitud_fila)/2)):
      fila.append(" ")
    piramide.append(fila)
  return piramide

def imprimir(array):
  for fila in array:
    print(" "*(len(fila))+" ".join(fila))
  for fila in array:
    print(" ".join(fila)+" "+" ".join(fila))

if __name__=="__main__":
    while(True):
      n=int(input("Ingresa un numero menor o igual a 2 para visualizar mejor la piramide: "))
      if n>=2:
        break
    imprimir(crear_piramide(n))
