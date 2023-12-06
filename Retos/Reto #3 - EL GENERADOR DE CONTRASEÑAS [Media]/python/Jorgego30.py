# * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
#  * Podrás configurar generar contraseñas con los siguientes parámetros:
#  * - Longitud: Entre 8 y 16.
#  * - Con o sin letras mayúsculas.
#  * - Con o sin números.
#  * - Con o sin símbolos.
#  * (Pudiendo combinar todos estos parámetros entre ellos)

import random

a="abcdefghijklmnopqrstuvwxyz"
A="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n="1234567890"
e="!\"$\\%&/()=?¿*^¨_:;,.-`+'@|"

l=0
a_=""
A_=""
n_=""
e_=""

f=1

print("Introduce el numero de caracteres de la contrasenha: ") 
l=int(input())

c=[]

while (f==1):
    if l<8 or l>16:
        print("\nLa longitud de la contrasenha debe estar comprendida entre 8 y 16 caracteres")
        print("")
        print("\nIntroduce de nuevo el numero de caracteres: ")
        l=int(input())
    else :
        f=0
        break
    


print("\nQuieres que la contrasenha tenga letras en minuscula? (y/n) ") 
a_=input()
print("\nQuieres que la contrasenha tenga letras en mayuscula? (y/n) ")  
A_=input()
print("\nQuieres que la contrasenha tenga numeros? (y/n) ")  
n_=input()
print("\nQuieres que la contrasenha tenga caracteres especiales? (y/n) ")  
e_=input()
print("")

t=""

if (a_=="y" and A_=="y" and n_=="y" and e_=="y"):
    t+=a
    t+=A
    t+=n
    t+=e
elif(a_=="y" and A_=="y" and n_=="y"):
    t+=a
    t+=A
    t+=n
elif(a_=="y" and A_=="y" and e_=="y"):
    t+=a
    t+=A
    t+=e
elif(a_=="y" and n_=="y" and e_=="y"):
    t+=a
    t+=n
    t+=e
elif(A_=="y" and n_=="y" and e_=="y"):
    t+=A
    t+=n
    t+=e
elif(a_=="y" and A_=="y"):
    t+=a
    t+=A
elif(a_=="y" and n_=="y"):
    t+=a
    t+=n
elif(a_=="y" and e_=="y"):
    t+=a
    t+=e
elif(A_=="y" and n_=="y"):
    t+=A
    t+=n
elif(A_=="y" and e_=="y"):
    t+=A
    t+=e
elif(n_=="y" and e_=="y"):
    t+=n
    t+=e
elif(a_=="y"):
    t+=a
elif(A_=="y"):
    t+=A
elif(n_=="y"):
    t+=n
elif(e_=="y"):
    t+=e

for i in range(0,l):
        numero_aleatorio=random.randint(0,len(t)-1)
        c.append(t[numero_aleatorio])

password=''.join(c)

print(password)