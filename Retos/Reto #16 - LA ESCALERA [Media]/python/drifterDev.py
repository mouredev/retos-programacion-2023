n=int(input("Ingresa el numero de escalones: "))

if n>0:
    imprimir=[]
    escalon="_|"
    for i in range(n):
        anadir1="  "*i
        anadir2="  "*(n-i-1)
        imprimir.append(anadir2+escalon+anadir1)
    print(str("  "*n)+"_")
    for j in imprimir:
        print(j)
elif n<0:
    imprimir=[]
    escalon="|_"
    for i in range(-n):
        anadir1=" "*((i*2)+1)
        anadir2="  "*(-n-i-1)
        imprimir.append(anadir1+escalon+anadir2)
    print("_")
    for j in imprimir:
        print(j)
else:
    print("__")
