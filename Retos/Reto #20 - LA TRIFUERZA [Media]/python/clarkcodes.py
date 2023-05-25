# Retos Semanales ‘23
# Reto #20: LA TRIFUERZA
# MEDIA | Publicación: 15/05/23 | Resolución: 22/05/23
#
# ¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 
#
# Crea un programa que dibuje una Trifuerza de "Zelda" formada por asteriscos.
# - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
# - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
#
# Ejemplo: Trifuerza 2
# 
#    *
#   ***
#  *   *
# *** ***
#

# Autor: Clark - @ClarkCodes
# Fecha de Resolución: 18/05/2023

# Imports
import typer
from rich import print
from enum import Enum

# Constantes
SPACE = " "
ASTERISK = "[yellow]*"

# Atributos Globales
welcome_pending = True

# Enums
class TrianglesFloor( Enum ):
    TOP = 1
    BOT = 2

class CharType( Enum ):
    SPACE = 1
    ASTERISK = 2

# Funciones - Métodos
def main_menu():
    global welcome_pending

    if( welcome_pending ):
        print( "[green]Bienvenido al Script de[/green] [yellow]La Trifuerza[/yellow], [green]ya que ha salido el nuevo Zelda, en horabuena, ¡vamos a dibujar una![/green] 😀\n" )
        welcome_pending = False
    else:
        print( "[green]¿Dibujamos otra?\n" )

    print( "[green]A continuación debes ingresar un número entero positivo, como mínimo 2, o ingresa 'q' si deseas salir." )
    print( "[green]¿De cuantas filas quieres que sea cada triángulo?\n" )

def char_writer( char_cant: int, char_type : CharType ):
    char = SPACE if char_type == CharType.SPACE else ASTERISK
    for ch in range( 0, char_cant ):
        print( char, end = "" )

def triangles_drawer( rows_cant : int, triangle_base_len : int, triangle_floor : TrianglesFloor ):
    asterisk_cant = 1 # Asterisks start with 1 and it grows with an increment of 2

    if( triangle_floor == TrianglesFloor.TOP ):
        spaces_count = triangle_base_len # Initial spaces quantity, it decrements with a step of 1
        
        for row_num in range( 0, rows_cant ): # Loop for the rows, in every row there are spaces and asterisks
            char_writer( spaces_count, CharType.SPACE )
            spaces_count -= 1

            char_writer( asterisk_cant, CharType.ASTERISK )
            asterisk_cant += 2

            print( " " ) # Necessary new lane because spaces and asterisks are drawn secuentially on the same line.

    elif( triangle_floor == TrianglesFloor.BOT ):
        spaces_count = rows_cant - 1 # Initial spaces quantity for second floor, it decrements with a step of 1
        middle_spaces_count = triangle_base_len # Spaces in the middle to draw the second triangle of the second floor

        for row_num in range( 0, rows_cant ): # Loop for the rows, in every row there are spaces and asterixs
            # Initial Spaces
            char_writer( spaces_count, CharType.SPACE )
            spaces_count -= 1

            # First Triangle Asterisks
            char_writer( asterisk_cant, CharType.ASTERISK )

            # Middle Spaces or Asterisk
            if( middle_spaces_count > 1 ):
                char_writer( middle_spaces_count, CharType.SPACE )
            else:
                char_writer( middle_spaces_count, CharType.ASTERISK )

            middle_spaces_count -= 2

            # Second Triangle Asterisks
            char_writer( asterisk_cant, CharType.ASTERISK )

            asterisk_cant += 2 # Asterisk increment, just now because the second triangle must be drawn exactly the same as the first one, so the asterisks work for the first and the second one in every iteration and the increment happens after both have been drawn
            print( " " )

def triforce_drawer( rows_cant : int ):
    triangle_base_len = ( 2 * rows_cant ) - 1 # Fórmula 2n - 1
    print( f"[yellow]-*-[/yellow] [green]Contemplad[/green] [yellow]¡LA TRIFUERZA![/yellow] [green]con[/green] [yellow]{rows_cant}[/yellow] [green]filas por Triángulo[/green] [yellow]-*-[/yellow]\n" )
    triangles_drawer( rows_cant, triangle_base_len, TrianglesFloor.TOP )
    triangles_drawer( rows_cant, triangle_base_len, TrianglesFloor.BOT )

def main():
    while True:
        print( "[bold green]\n*** Reto #20: LA TRIFUERZA - By @ClarkCodes ***\n" )
        main_menu()

        print( "[bold green]Número de filas por triángulo[/bold green]", end = "" )
        userAnswer = typer.prompt( "", default="2" )
        
        if( userAnswer == 'q' or userAnswer == 'Q' ): # Condición de Salida
            print( "[green]\n✅ Esto ha sido todo por hoy.\n❤ Muchas gracias por ejecutar este Script, hasta la próxima...💻 Happy Coding!,👋🏼 bye :D\n😎 Clark." )
            break

        try:
            rows_cant = int( userAnswer ) # Se convierte la opcion ingresada por el usuario de texto a entero
            
            if( rows_cant >= 2 ):
                print( " " )
                triforce_drawer( rows_cant )

            else:
                print( "\n❌ Solo se admiten números enteros positivos mayores o iguales a 2, o la letra 'q' si deseas salir, verifique nuevamente." )

        except ValueError as ve:
            print( "\n❌ Opción ingresada no disponible, solo se admiten números enteros positivos mayores o iguales a 2, o la letra 'q' si deseas salir, verifique nuevamente." )
            #print( f"{ve}\n{traceback.print_exc()}" )
        except Exception as ex:
            print( "\n❌ Oops... algo no ha salido bien, revise nuevamente por favor." )
            #print( f"{ex}\n{traceback.print_exc()}" )

    raise typer.Abort()

# Llamada a la Función Principal usando typer
if __name__ == "__main__":
    typer.run( main )

#
# *** Razonamiento y análisis previo para dibujar los triángulos ***
#
# + Observación:
#
# Número de Filas: 2 - Triángulo Individual
#  *
# ***
#
# Número de Filas: 3 - Triángulo Individual
#   *
#  ***
# *****
# 
# Número de Filas: 4 - Trifuerza completa
#        *
#       ***
#      *****
#     *******
#    *       *
#   ***     ***
#  *****   *****
# ***************
#
#  
# + Explicación:
#
# Para la base de los triángulos se usa la fórmula indicada: 2n - 1, cuyo resultado se usará 
# para la cantidad de unidades(asteriscos) de la base de cada triángulo.
# La Trifuerza se va a dividir en dos pisos, el primero con el triángulo superior y el segundo
# con los dos triángulos inferiores.
#
# Se obervan los siguientes patrones:
# 
# - Se empieza con un asterisco como la punta del triángulo, de allí hay un incremento homogenio  
# de 2 unidades hasta llegar a la cantidad de unidades de la base, la cual fué calculada por la 
# formula anteriormente mencionada. 
# Al realizar el incremento de 2 en 2, esto coincide con el número de filas que debe haber cuando 
# se llega al número de unidades que la base debe tener.
#
# - El número de espacios inicial en el primer piso que se debe dejar para dibujar el triángulo superior,
# empezando por supuesto por el asterisco de la punta, es igual al número de unidades de la base, es decir 
# al resultado calculado por la fórmula mencionada anteriormente, esto se da por la propiedad de triángulos 
# semejantes descrita en geometría.
#
# - En el segundo piso hay dos intervalos de espacios, el primero desde borde de la pantalla hasta el primer 
# asterisco en una cierta linea del triángulo de la izquiera y el segundo desde el ultimo asteristo dibujado 
# en esa linea del triangulo de la izquierda dibujado en esa linea hasta el primer asterisco del triangulo de 
# la derecha que corresponde en esa linea.
#
# - El número de espacios inicial del segundo piso(donde estan los dos triángulos inferiores) que se debe 
# dejar para dibujar el primer asterisco de la punta del triángulo de la izquierda y que así se forme una 
# simetría con las demás filas, es igual al número de filas ingresado menos uno, es decir: n - 1. 
# Estos espacios tanto en el primer, como en el segundo piso van disminuyendo de 1 en 1 en cada fila posterior, 
# por lo tanto, si el número de filas ingresado fué 5, entonces la cantidad inicial de espacios para 
# dibujar el asterisco de la punta en el primer piso es 9, en la siguiente fila es 8, en la siguiente es 7, 
# luego 6 y luego 5, en el segundo piso en cambio es 4, luego 3, en la siguiente 2, luego 1 y hasta al final 
# llegar a 0, es decir en la fila base del segundo piso no deben haber espacios para dibujar la base del 
# triangulo. De esta manera se coincide con el número de filas requerido.
# 
# - Para dibujar los dos triangulos inferiores, se debe tener en cuenta las proporciones y los espacios 
# necesarios a dibujarse en cada fila, teniendo en consideración que entre las dos bases se debe añadir
# un asterisco extra en medio delas bases de estos, dado que de otra manera se estaría dejando un espacio 
# vacío en medio de los dos triángulos inferiores y en mi opinión se vería raro, parecería como que algo 
# ahí no coincidiría.
