# Retos Semanales ‘23
# Reto #27: CUENTA ATRÁS
# MEDIA | Publicación: 03/07/23 | Resolución: 10/07/23
#
# Crea una función que reciba dos parámetros para crear una cuenta atrás.
# - El primero, representa el número en el que comienza la cuenta.
# - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
# - Sólo se aceptan números enteros positivos.
# - El programa finaliza al llegar a cero.
# - Debes imprimir cada número de la cuenta atrás.

# Autor: Clark - @ClarkCodes
# Fecha de Resolución: 02/08/2023

# Imports
from datetime import datetime
import typer
from rich import print
import time

# Funciones - Métodos
def validate_positiveness( n : int ):
    if n > 0:
        return True
    return False

def timer( start : int, time_span : int ):
    print( f"\n[bold yellow]** Temporizador de Cuenta Atrás **\n" )

    for step in range( start, -1, -1 ):
        print( f"[green]Cuenta restante: {step}" )
        
        if( step > 0 ):
            time.sleep( time_span )

def main():
    exit_msj = f"[green]\n✅ Esto ha sido todo por hoy.\n❤ Muchas gracias por ejecutar este Script, hasta la próxima...💻 Happy Coding!,👋🏼 bye :D\n😎 Clark."
    value_error = "\n❌ Valor ingresado no permitido, solo se admiten números enteros positivos, verifique nuevamente."
    start = 0
    time_span = 0
    
    print( "[bold green]\n*** Reto #27: CUENTA ATRÁS - By @ClarkCodes ***" )
    print( "\n[green]Bienvenido al Script de[/green] [yellow]Cuenta Atrás[/yellow], [green]¡hagamos un Temporizador!.[/green] 😀\n" )
    
    print( "[green]Este es un temporizador un tanto particular, desciende desde un número entero positivo hasta llegar a 0, con una cantidad de segundos indicados que transcurren entre cada vez que desciende una unidad.\n" )

    while True:
        try: # Ingreso de Información
            print( "[bold green]Número de partida[/bold green]", end = "" )
            user_answer = typer.prompt( "" )
            start = int( user_answer ) # Conversión del mes a entero
            
            print( "\n[bold green]Lapso entre unidades[/bold green]", end = "" )
            user_answer = typer.prompt( "" )
            time_span = int( user_answer )
            
            # Validadción y Verificación de la Fecha
            if( validate_positiveness( start ) and validate_positiveness( time_span ) ):
                timer( start, time_span )
                time.sleep( 1 )
                print( f"\n[bold yellow]¡Tic Toc!. El Tiempo ha terminado y la cuenta ha concluído." )
                time.sleep( 2 )
                print( exit_msj )
                break
            else:
                print( value_error )

        except ValueError as ve:
            print( value_error )

        except Exception as ex:
            print( "\n❌ Oops... algo no ha salido bien, revise nuevamente por favor." )

# Llamada a la Función Principal usando typer
if __name__ == "__main__":
    typer.run( main )
