symbols=['═', '║', '╗', '╔', '╝', '╚']

def dibujaMatriz(m):
  for i in range(len(m)):
    for j in range(len(m[i])):
      print(m[i][j], end="")
    print()

def espiral(lado:int):
  matriz=[]
  for _ in range(lado):
    a = [0]*lado
    matriz.append(a)

  if lado%2==0:
    n=lado//2
    m=n-1
    for i in range(n):
      matriz[n][m]=symbols[5]
      matriz[m][n]=symbols[2]
      matriz[n][n]=symbols[4]
      matriz[i][i]=symbols[0]
      n+=1
      m-=1
    n=lado//2
    m=n-1
    veces2=2
    veces1=1
    for j in range(n-1):
      l=m
      for k in range(veces2):
        matriz[n+1][l]=symbols[0]
        matriz[m-1][l]=symbols[0]
        matriz[l][n+1]=symbols[1]
        l+=1
      veces2+=2
      r=m+1
      for b in range(veces1):
        matriz[r][m-1]=symbols[1]
        a=b
        r+=1
      veces1+=2
      n+=1
      m-=1
      matriz[j+1][j]=symbols[3]
      
  else:
    n=(lado-1)//2
    m=n
    for i in range(n+1):
      matriz[m][n]=symbols[2]
      n+=1
      m-=1
    n=(lado-1)//2
    m=n-1
    veces2=2
    veces1=1
    for k in range(n):
      matriz[k+1][k]=symbols[3]
      matriz[k][k]=symbols[0]
      matriz[n+1][n+1]=symbols[4]
      matriz[n+1][m]=symbols[5]
      r=m+1
      o=m+1
      for g in range(veces1):
        matriz[m][r]=symbols[0]
        matriz[n+1][r]=symbols[0]
        matriz[o][n+1]=symbols[1]
        r+=1
        o+=1
      veces1+=2
      n+=1
      m-=1
    n=(lado-1)//2
    m=n-1
    veces2=2
    for b in range(n-1):
      r=m+1
      for v in range(veces2):
        matriz[r][m-1]=symbols[1]
        r+=1
      veces2+=2
      n+=1
      m-=1

  dibujaMatriz(matriz)


espiral(0)
espiral(1)
espiral(2)
espiral(3)
espiral(4)
espiral(20)
espiral(50)
