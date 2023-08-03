## la escalera

def escaleraup(n,b):
    i=0
    while i <= n:
        if i==0:
            escalon="  _"
            print(" "*n + escalon)
        else:
            b=b-1
            escalon=" _| "
            print(" "*b + escalon)
        i=i+1


def escaleradown(n,b):
    i=0

    while i >= n:
        if i==0:
         
         escalon="_"
         print(" "*b+escalon)
        else:
            b=b+1
            escalon="|_ "   
            print(" "*b+escalon)
        i=i-1

#####################################################

n=int(input("ingrese numero de escalones \n"))
b=n

if n>0:
    escaleraup(n,b)


elif n==0:
    print("__")


else:
    b=1
    escaleradown(n,b)


