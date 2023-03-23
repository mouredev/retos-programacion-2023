#  * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
#  * Ejemplos:
#  * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
#  * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"

num=int(input())

fibonacci=list(range(0,100))

x1=0
x2=1
x3=1


for i in range(0,100):
    fibonacci[i]=x1 + x2
    x3=x1 + x2
    x1 = x2
    x2 = x3

primo=False

if(num<1):
    primo=False

for i in range(2,int((num/2))+1):
    if (num%2==0):
        primo=False
    else:
        primo=True

par=False

if(num%2==0):
    par=True
else:
    par=False

if (primo==1 and par==1 and (num in fibonacci)==1):
    print("Este numero es primo, fibonacci y par")
elif (primo==0 and par==1 and (num in fibonacci)==1):
    print("Este numero no es primo, es fibonnaci y par")
elif (primo==1 and par==0 and (num in fibonacci)==1):
    print("Este numero es primo, fibonacci y es impar")
elif (primo==1 and par==1 and (num in fibonacci)==0):
    print("Este numero es primo ni fibonacci, es par")
elif (primo==0 and par==1 and (num in fibonacci)==0):
    print("Este numero no es primo ni fibonacci, es par")
elif (primo==0 and par==0 and (num in fibonacci)==1):
    print("Este numero no es primo, es fibonacci y es impar")
elif (primo==1 and par==0 and (num in fibonacci)==0):
    print("Este numero es primo, no es fibonacci y es impar")
elif (primo==0 and par==0 and (num in fibonacci)==0):
    print("Este numero no es primo, no es fibonacci y es impar")
    