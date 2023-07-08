"""
Retos Semanales ‘23
Reto #22: LA ESPIRAL
MEDIA | Publicación: 29/05/23 | Resolución: 06/06/23

 * Crea una función que dibuje una espiral como la del ejemplo.
 * - Únicamente se indica de forma dinámica el tamaño del lado.
 * - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
 *
 * Ejemplo espiral de lado 5 (5 filas y 5 columnas):
 * ════╗
 * ╔══╗║
 * ║╔╗║║
 * ║╚═╝║
 * ╚═══╝
 *
"""

# Autor: Clark - @ClarkCodes
# Fecha de Resolución: 04/06/2023

# Imports
import math
import typer
from rich import print
from enum import Enum

# Constantes
HORIZONTAL_WAY = "═"
VERTICAL_WAY = "║"
UPPER_RIGHT_CORNER = "╗"
UPPER_LEFT_CORNER = "╔"
LOWER_RIGHT_CORNER = "╝"
LOWER_LEFT_CORNER = "╚"
EVEN_CORE = "╚╝"
ODD_CORE = "╔╗"
MIN_SIDE_LEN = 3

# Variables Globales
welcomePending = True

# Enums
class PartType( Enum ):
    TOP = 1
    BOT = 2

# Funciones - Métodos
def main_menu():
    global welcomePending

    if( welcomePending ):
        print( "[green]\nBienvenido al Script de [yellow]La Espiral[/yellow], ¡vamos a dibujar una![/green] 😀" )
        welcomePending = False
    else:
        print( "[green]\n¿Dibujas otra?" )

    print( "[green]\nA continuación debes ingresar un número entero positivo, como mínimo 2, o ingresa 'q' si deseas salir." )
    print( "[green]¿De cuantas unidades quieres que sea el lado mayor?\n" )

def is_even( number : int ):
    if( number % 2 == 0 ):
        return True
    return False

def print_line( line : str ):
    print( f"[yellow]{line}" )

def core_row_drawer( side_len : int, is_sl_even : bool ):
    core = ""
    vert_cant = side_len - 2 # total vertical chars quantity around the core, it must be distributed
    left_cant = 0 # cantidad de lineas verticales que deben dibujarse a la izquierda del core
    right_cant = 0 # cantidad de lineas verticales que deben dibujarse a la derecha del core

    if( is_sl_even ): # En función de si side_len es par o no, se define el tipo de core que se necesita usar y cuantas lineas verticales debendibujarse a la izquierda y a la derecha
        core = EVEN_CORE
        left_cant = int( vert_cant / 2 )
        right_cant = left_cant
    else:
        core = ODD_CORE
        left_cant = math.floor( vert_cant / 2 )
        right_cant = vert_cant - left_cant

    print_line( f"{VERTICAL_WAY * left_cant}{core}{VERTICAL_WAY * right_cant}" )

def parts_drawer( side_len : int, horizontal_cant : int, part_type : PartType ):
    vert_cant = side_len - ( horizontal_cant + 2 ) # total vertical chars quantity around corners
    left_cant = math.floor( vert_cant / 2 ) # cantidad de lineas verticales que deben dibujarse a la izquierda de la ezquina izquierda
    right_cant = vert_cant - left_cant # cantidad de lineas verticales que deben dibujarse a la derecha de la ezquina derecha
    left_corner = ""
    right_corner = ""

    if( part_type == PartType.TOP ): # Se define que tipo de esquinas se necesitan usar dependiendo del tipo de parte
        left_corner = UPPER_LEFT_CORNER
        right_corner = UPPER_RIGHT_CORNER
    elif( part_type == PartType.BOT ):
        left_corner = LOWER_LEFT_CORNER
        right_corner = LOWER_RIGHT_CORNER
    
    print_line( f"{VERTICAL_WAY * left_cant}{left_corner}{HORIZONTAL_WAY * horizontal_cant}{right_corner}{VERTICAL_WAY * right_cant}" )

def spiral_drawer( side_len : int ):
    print( f"[yellow]-*-[/yellow] [green]Contemplad[/green] [yellow]¡LA ESPIRAL![/yellow] [green]con[/green] [yellow]{side_len}[/yellow] [green]unidades de filas y columnas[/green] [yellow]-*-[/yellow]\n" )
    
    is_sl_even = is_even( side_len )
    core_row_index = int( side_len / 2 if is_sl_even else math.floor( side_len / 2 ) ) + 1
    horizontal_cant = side_len - 1

    for row in range( 1, side_len + 1 ): # Rango entre 1 y side_len incluídos ambos extremos
        if( row == 1 ):
            print_line( f"{HORIZONTAL_WAY * ( side_len - 1 )}{UPPER_RIGHT_CORNER}" )

        else:
            if( row < core_row_index ): # Parte Superior antes del core
                horizontal_cant -= 2
                parts_drawer( side_len, horizontal_cant, PartType.TOP )

            elif( row == core_row_index ):
                core_row_drawer( side_len, is_sl_even )

            elif( row > core_row_index ): # Parte Inferior despues del core
                if( horizontal_cant == 1 and is_sl_even ):
                    horizontal_cant += 1
                elif( horizontal_cant == 2 and not is_sl_even ):
                    horizontal_cant = 1

                parts_drawer( side_len, horizontal_cant, PartType.BOT )
                horizontal_cant += 2

def main():
    print( "[bold green]\n*** Reto #22: LA ESPIRAL - By @ClarkCodes ***" )

    while True:
        main_menu()

        print( "[bold green]Número de unidades[/bold green]", end = "" )
        userAnswer = typer.prompt( "", default = str( MIN_SIDE_LEN ) )
        
        if( userAnswer == 'q' or userAnswer == 'Q' ): # Condición de Salida
            print( "[green]\n✅ Esto ha sido todo por hoy.\n❤ Muchas gracias por ejecutar este Script, hasta la próxima...💻 Happy Coding!,👋🏼 bye :D\n😎 Clark." )
            break

        try:
            side_len = int( userAnswer ) # Se convierte la opcion ingresada por el usuario de texto a entero
            
            if( side_len >= MIN_SIDE_LEN ):
                print( " " )
                spiral_drawer( side_len )

            else:
                print( "\n❌ Solo se admiten números enteros positivos mayores o iguales a 2, o la letra 'q' si deseas salir, verifique nuevamente." )

        except ValueError as ve:
            print( "\n❌ Opción ingresada no disponible, solo se admiten números enteros positivos mayores o iguales a 2, o la letra 'q' si deseas salir, verifique nuevamente." )
            print( ve.with_traceback() )
        except Exception as ex:
            print( "\n❌ Oops... algo no ha salido bien, revise nuevamente por favor." )
            print( ex )

# Llamada a la Función Principal usando typer
if __name__ == "__main__":
    typer.run( main )

'''
Análisis, Planificación y Explicación

 * Ejemplo espiral de lado 3 (3 filas y 3 columnas):
  ══╗
  ╔╗║
  ╚═╝
 
 * Ejemplo espiral de lado 4 (4 filas y 4 columnas):
  ═══╗
  ╔═╗║
  ║╚╝║
  ╚══╝

 * Ejemplo espiral de lado 5 (5 filas y 5 columnas):
  ════╗
  ╔══╗║
  ║╔╗║║
  ║╚═╝║
  ╚═══╝

* Ejemplo espiral de lado 6 (6 filas y 6 columnas):
  ═════╗
  ╔═══╗║
  ║╔═╗║║
  ║║╚╝║║
  ║╚══╝║
  ╚════╝     

* Ejemplo espiral de lado 7 (7 filas y 7 columnas):
  ══════╗
  ╔════╗║
  ║╔══╗║║
  ║║╔╗║║║
  ║║╚═╝║║
  ║╚═══╝║
  ╚═════╝

* Ejemplo espiral de lado 10 (10 filas y 10 columnas):

*** Se observan los siguientes patrones:

- Una espiral solo puede ser de mínimo 3 unidades ingresadas por el usuario, con un número menor 
no se formaría una figura de espiral.

- El core o núcleo de la espiral, el cual está en el centro de esta, siempre va dibujado de una 
forma determinada dependiendo si el número de unidades requeridas por el usuario es par o es impar, 
este core consta siempre de dos caracteres de esquinas, si n es par se dibuja así: ╚╝ y si n es impar, 
se dibuja así ╔╗, por lo tanto, se lo puede almacenar en una constante para poder usarlo llegado el momento.

- Cuando se dibuje la linea del centro de la espiral donde va el core, para determinar cual es la fila 
donde este debe ir, coincide con que el core siempre está dibujado, dependiendo de si n es par o impar; 
si n es par, está dibujado en la fila cuyo orden corresponde a ( n / 2 ) + 1, pero si es impar en cambio está dibujado 
en la fila cuyo orden corresponde a math.floor( n / 2 ) + 1, es decir a n / 2 pero redondeado hacia el entero 
inferior más próximo + 1.

- Los caracteres que rodean al núcleo son siempre lineas verticales, es decir el caracter '║', la cantidad 
de estos caracteres que hay que dibujar al rededor del núcleo se dividen en dos partes, la cantidad de 
estos caracteres a la izquierda del núcleo y a la derecha de este, dado que n es la longitud de caracteres 
en la fila, y el núcleo ocupa 2 caracteres, entonces lo restante son para las lineas verticales, es decir 
la cantidad de lineas verticales que rodean al núcleo es n - 2, si n es par esta resta siempre va a ser par, y 
por lo contrario si n es impar esta resta también siempre va a ser impar.
Si n es par, estas lineas verticales se distribuyen equitativamente e irian la misma cantidad en ambos lados, 
es decir, a la izquierda y a la derecha irian la cantidad de caracteres ( n - 2 ) / 2
si por otro lado, n es impar, dado que hay que dividir n - 2 para 2, entendiendo que n - 2 es impar, esto significa 
que el resultado de esta división va a ser inexacto y va a dar como resultado un número decimal, un float, 
entonces para distribuírlo al rededor del núcleo, tratando de buscar la mitad pero sin decimales, esto 
resulta en una distribución inequitativa, entonces a la izquierda coincide que  siempre va la cantidad menor 
y a la derecha la cantidad mayor que más se acerque a la mitad, sin usar decimales y que sumando estas dos cantidades 
den como resultado n - 2, entonces coincide que a la izquierda irian math.floor( ( n - 2 ) / 2 ) caracteres, esto es,
tomando el resultado decimal de ( n - 2 ) / 2 y aplicandole el método math.floor() para obtener el entero inferior 
más próximo, es decir, redondeandolo hacia abajo, y para determinar la cantidad de caracteres que van a la derecha
se resta ( n - 2 ) - la cantidad de caracteres en la izquierda, es decir: ( n - 2 ) - math.floor( ( n - 2 ) / 2 ).
Los resultados de las operaciones que vamos realizando los podemos asignar a variables si se va a necesitar ese valor 
posteriormente para no tener que realizar el calculo cada vez que se lo use, unicamente por motivos explicativos 
y para evitar mayores enredos, los hemos puesto aquí de esta manera.

- Se puede dividir la espiral en tres partes, parte superior, linea del core y parte inferior, excluyendo la 
primera linea la cual no sigue el patrón de las demás dado que no tiene esquina superior izquierda.
Se considera parte superior a las lineas que estan después de la primera linea y antes de la linea del core.
Se considera parte inferior a todas las lineas que estan después del core, teniendo en cuenta que el total de 
número de lineas incluyendo la primera debe ser igual a n, a n en el código se la llamará side_len, que 
significa side length, o sea, longitud del lado, que quiere decir longitud de caracteres de ancho y lado 
requerido por el usuario para la espiral.

- Para dibujar las lineas de la parte superior, la cantidad de lineas horizontales entre las esquinas empieza en 
n - 3 y va decrementandose en 2 en cada linea posterior. La cantidad de lineas verticales al rededor es igual a 
n - ( cantidad de lineas horizontales + 2, por los caracteres las esquinas ), las cuales se distribuyen de forma 
similar a la linea del core.
Coincide que a la cantidad de totales de lineas verticales que deben dibujarse las asignaremos a la variable vert_cant, 
entonces a la izquierda deben dibujarse math.floor( vert_cant / 2 ) caracteres, se redondea también hacia abajo 
vert_cant / 2, y a la derecha deben dibujarse vert_cant - los caracteres verticales de la izquierda.

Se observa que si n es par, la cantidad de lineas horizontales entre las esquinas de la parte superior terminan 
siempre en 1, mientras que si n es impar, terminan siempre en 2.

- Para dibujar las lineas de la parte inferior es el mismo proceso que para dibujar la parte superior, pero se 
dibujar las esquinas correspondientes a la parte inferior y también se observa que la cantidad de lineas 
horizontales entre las esquinas, dependiendo de si n es par, empiezan en 2, y si n es impar empiezan en 1, y 
van incrementandose en 2 en cada linea posterior hasta terminar la espiral.
'''
