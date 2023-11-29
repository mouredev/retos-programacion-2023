# Reto #21: Números primos gemelos
#### Dificultad: Media | Publicación: 22/05/23 | Corrección: 29/05/23 | Mi solución: 24/11/2023

## Enunciado
#  Crea un programa que encuentre y muestre todos los pares de números primos
#  gemelos en un rango concreto.
#  El programa recibirá el rango máximo como número entero positivo. 
#  - Un par de números primos se considera gemelo si la diferencia entre
#    ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
#  - Ejemplo: Rango 14
#     (3, 5), (5, 7), (11, 13)

#creacion de funcion que revisa si es primo o no
def is_prime(number: int)->bool:
    #definamos caso base
    if number < 2:
        return False
    
    #revisamos si es un numero primo
    for index in range(2, number):
        if number%index ==0:
            return False
    return True

#mostramos los primos gemelos
def find_prime_twins(range_number: int):
    if range_number >2:
        print(f"Valores gemelos primos para <{range_number}>")
        for index in range(2, range_number):
            #revisa si el valor no excede el rango y valida si cada elemento es primo
            if index +2 <=range_number and is_prime(index) and is_prime(index+2):
                print(f"({index}, {index+2})")
    else:
        print(f"No hay numeros primos gemelos para <{range_number}>")

if __name__ == "__main__":
    
    find_prime_twins(42)
    find_prime_twins(2)
    find_prime_twins(-100)
    find_prime_twins(int(input("Ingresa un valor para evaluar la existencia de # primos gemelos: ")))
    