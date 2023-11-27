# Reto No.40 -Tabla de multiplicar
# Dificultad: Fácil | Publicación: 09/10/23 | Corrección: 16/10/23
#-----------------------------------------------------------------
#Enunciado
# Crea un programa que sea capaz de solicitarte un número y se
# encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
#- Debe visualizarse qué operación se realiza y su resultado.
#  Ej: 1 x 1 = 1
#      1 x 2 = 2
#      1 x 3 = 3
#      ... 
#-----------------------------------------------------------------

print ("Pushodev")
print ("https://github.com/PushoDev")

numero = int(input("Ingresa un número: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

print ("Muchas Gracias por participar")
print ("Su número ingresado fué: ", numero)