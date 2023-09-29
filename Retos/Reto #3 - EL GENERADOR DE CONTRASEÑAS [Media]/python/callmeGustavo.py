import random 

## Numeros
numeros = []
for i in range(48,58):
    numeros.append(chr(i))
#print(numeros)

## Mayusculas
mayusculas = []
for i in range(65,91):
    mayusculas.append(chr(i))
#print(mayusculas)

## Minuscula
minusculas = []
for i in range(97,123):
    minusculas.append(chr(i))
#print(minusculas)

## Signos
signos = []
for i in range(33,48):
    signos.append(chr(i))
for ii in range(58,65):
    signos.append(chr(ii))
for iii in range(91,97):
    signos.append(chr(iii))
#print(signos)

longitud = int(input("Ingrese longitud del password: "))

if longitud < 8 or longitud > 16:
    raise ValueError('Longitud inválida')

password = ""
for i in range(longitud):
    password += numeros[random.randint(0,len(numeros)-1)]
    #breakpoint() 
    password += mayusculas[random.randint(0,len(mayusculas)-1)] 
    password += minusculas[random.randint(0,len(minusculas)-1)] 
    password += signos[random.randint(0, len(signos)-1)]

print(password[:longitud])
# for i in longitud:
#     password +=  chr(longitud)
# # elif type(longitud) != int:
# #     raise ValueError("No es un int")




