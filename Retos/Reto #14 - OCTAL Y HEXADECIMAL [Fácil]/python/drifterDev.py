numero=int(input("Numero que desea convertir: "))
numero1=numero
numero2=numero
octa=""
hexa=""
n=numero
numeros=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
while(numero1>0):
    n=numero1%8
    numero1=numero1//8
    octa+=str(n)

while(numero2>0):
    m=numero2%16
    numero2=numero2//16
    hexa+=str(numeros[m])

print("El numero "+str(numero)+" en sistema octal es: "+str(octa[::-1]))
print("El numero "+str(numero)+" en sistema hexadecimal es: "+str(hexa[::-1]))
