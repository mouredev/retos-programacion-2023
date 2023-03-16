#!/usr/bin/python3

# /*
#  * Crea un generador de números pseudoaleatorios entre 0 y 100.
#  * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
#  *
#  * Es más complicado de lo que parece...
#  */

import time, os

def limpiarPantalla(): # Función para limpiar la pantalla
    if os.name == 'posix': # Sí se ejecuta en sistemas unix utiliza "clear"
        os.system('clear')
    else: # En otros casos, usará "cls"
        os.system('cls')

def generarSemilla(): # Función que genera una semilla basada en el tiempo
    semilla = time.time_ns() # Se obtiene un entero a traves del tiempo actual en nano-segundos
    return semilla # Devuelve el entero

def generarEnteroPseudoAleatorio(): # Función que genera un número pseudo-aleatorio
    semilla = generarSemilla() # Obtiene una semilla 
    número = semilla % 101 # Obtiene el residuo de dividir la semilla entre 101, lo cual siempre es un número entre 0 y 100
    return número # Devuelve un número pseudo-aleatorio

# def generarEnteroPseudoAleatorio2(): # Función que genera un número pseudo-aleatorio
#     semilla = str(generarSemilla()) # Obtiene una semilla en formato string
#     semilla = semilla[13:] # Elimina los 13 primeros dígitos
#     número = int(semilla) % 101 # Vuelve a convertir la semilla en un entero, obtiene el residuo de dividir la semilla entre 101, lo cual siempre es un número entre 0 y 100
#     return número # Devuelve un número pseudo-aleatorio

def comprobarAleatoriedad(función, ciclos): # Función que muestra la distribución de números para comprobar la aleatoriedad de una función
    númerosGenerados = [] # Lista que almacenará los números generados
    for i in range(ciclos): # Iniciando el ciclo
        númerosGenerados.append(función()) # Añadiendo la respuesta de la función a la lista

    for i in range(101): # # Ciclo para enseñar la cantidad de veces que se ha generado cada número
        porcentaje = númerosGenerados.count(i) * 100 / ciclos # Obteniendo el porcentaje de veces que apareció el número
        print(f"Número {i} aparece {númerosGenerados.count(i)} veces, ocupando el {porcentaje}% del total") # Mostrando resultado

def main(): # Función principal
    limpiarPantalla() # Limpia la pantalla
    print(f'Número generado: {generarEnteroPseudoAleatorio()}') # Enseñando un número pseudo-aleatorio

    input("[!] Presione 'Enter' para comprobar aleatoriedad de la función: ")
    limpiarPantalla()
    comprobarAleatoriedad(generarEnteroPseudoAleatorio, ciclos=100) # Toma como argumentos la función y las veces que se llamará la función

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nCerrando programa')