"""
 Retos Semanales ‘23
 Reto #21: NÚMEROS PRIMOS GEMELOS
 MEDIA | Publicación: 22/05/23 | Resolución: 29/05/23

 * Crea un programa que encuentre y muestre todos los pares de números primos
 * gemelos en un rango concreto.
 * El programa recibirá el rango máximo como número entero positivo.
 * 
 * - Un par de números primos se considera gemelo si la diferencia entre
 *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
 *
 * - Ejemplo: Rango 14
 *   (3, 5), (5, 7), (11, 13)
 *
"""

# Autor: Clark - @ClarkCodes
# Fecha de Resolución: 25/05/2023

# Imports
import typer
from rich import print
from enum import Enum

# Funciones - Métodos
def isPrime( n : int ) -> bool: # Devuelve True si un número es primo, False por lo contrario
    for i in range( 2, n ):
        if( ( n % i ) == 0 ):
            return False
    return True

def prime_twins_engine( max_range : int ):
    prime_twins = []
    left_prime = 0
    right_prime = 0

    for n in range( 1, max_range + 1 ): # Prime Twins Engine
        if( isPrime( n ) ):
            if( left_prime == 0 ): # En la primera iteración simplemente se asigna el primer valor primo a left_prime, se necesitan dos primos para realizar la resta y verificar si son gemelos
                left_prime = n

            else: # En las siguientes iteraciones en que se hallen números primos se asignará su valor a right_prime y se realizará la resta, si la diferencia es exactamente 2, se agregará left_prime y right_prime como una tupla par de valores a la lista prime_twins, ahí se iran recolectando los primos gemelos que se encuentren
                right_prime = n

                if( ( right_prime - left_prime ) == 2 ):
                    prime_twins.append( tuple( ( left_prime, right_prime ) ) )

                left_prime = right_prime # Al final de la iteración nos aseguramos que left_prime tenga ahora el valor de right_prime para que la próxima vez que se halle un primo y se asigne su valor a right_prime se pueda realizar la resta correctamente ahora entre el último primo que se tenia con el siguiente
    
    print(f"\n[green]Los Números Primos Gemelos en el rango entre 1 y {max_range} son los siguientes:\n" )
    
    for index, prime_twin_pair in enumerate( prime_twins ):
        print( f"[green]{prime_twin_pair[0]} y {prime_twin_pair[1]}", end="" )
        
        if( index < len( prime_twins ) - 1 ):
            print( ", ", end="" )
    
    print( " " )

def main():
    welcome_pending = True

    while True:
        if( welcome_pending ):
            print( "[bold green]\n*** Reto #21: NÚMEROS PRIMOS GEMELOS - By @ClarkCodes ***" )
            welcome_pending = False

        else:
            print( "[green]\n¿Qué tal, está cool no?, ¿quieres ingresar otro rango?" )

        print( "[green]\nIngrese el rango máximo para calcular los Números Primos Gemelos, debe ser un número entero positivo, o ingresa 'q' si deseas salir." )
        print( "[bold green]\nRango máximo: ", end = "" )
        user_answer = input( "" )
        
        if( user_answer == 'q' or user_answer == 'Q' ): # Condición de Salida
            print( "[green]\n✅ Esto ha sido todo por hoy.\n❤ Muchas gracias por ejecutar este Script, hasta la próxima...💻 Happy Coding!,👋🏼 bye :D\n😎 Clark." )
            break

        try:
            max_range = int( user_answer ) # Se convierte la opcion ingresada por el usuario de texto a entero
            
            if( max_range >= 1 ):
                prime_twins_engine( max_range )

            else:
                print( "\n❌ Solo se admiten números enteros positivos mayores o iguales a 1, o la letra 'q' si deseas salir, verifique nuevamente." )

        except ValueError as ve:
            print( "\n❌ Opción ingresada no disponible, solo se admiten números enteros positivos mayores o iguales a 2, o la letra 'q' si deseas salir, verifique nuevamente." )
        except Exception as ex:
            print( "\n❌ Oops... algo no ha salido bien, revise nuevamente por favor." )

# Llamada a la Función Principal usando typer
if __name__ == "__main__":
    typer.run( main )
