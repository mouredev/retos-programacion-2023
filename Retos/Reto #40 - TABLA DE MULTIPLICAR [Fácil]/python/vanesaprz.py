"""
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
"""

#Solicito un número al usuario y me aseguro que el input recibido es un int.  
while True:
    try:
        num = int(input ("Indica número para realizar tabla de multiplicar: ")) #guarda la variable del usuario
        break
    except ValueError:
        print("Input no válido, indica un número entero: ") 

#Calcula el resultado y le da el formato deseado
for i in range (1,11):
    resultado = i * num 
    print(f"{num} x {i} = {resultado}")

