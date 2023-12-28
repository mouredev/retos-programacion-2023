# Retos Semanales ‘23
# Reto #12: VIERNES 13
# FÁCIL | Publicación: 20/03/23 | Resolución: 27/03/23
#
# Crea una función que sea capaz de detectar si existe un viernes 13
# en el mes y el año indicados.
# - La función recibirá el mes y el año y retornará verdadero o falso.
#

# Autor: Clark - @ClarkCodes
# Fecha de Resolución: 31/07/2023

# Imports
from datetime import datetime
import typer
from rich import print
from enum import Enum

# Atributos Globales
welcome_pending = True

# Constantes
MIN_MONTH = 1
MAX_MONTH = 12
MIN_YEAR = 1900

# Enums
class ValidatorType( Enum ):
    MONTH = 0
    YEAR = 1

class DayOfWeek( Enum ):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

class MonthOfYear( Enum ):
    Enero = 1
    Febrero = 2
    Marzo = 3
    Abril = 4
    Mayo = 5
    Junio = 6
    Julio = 7
    Agosto = 8
    Septiembre = 9
    Octubre = 10
    Noviembre = 11
    Diciembre = 12

# Funciones - Métodos
def main_menu():
    global welcome_pending

    if( welcome_pending ):
        print( "\n[green]Bienvenido al Script de[/green] [yellow]Viernes 13[/yellow], [green]verifiquemos si existe un viernes 13 en el mes y año que quieras.[/green] 😀\n" )
        welcome_pending = False
    else:
        print( "\n[green]¿Verificamos en otro mes y año?\n" )

    print( "[green]A continuación debes ingresar el mes y año a verificar, ambos deben ser números enteros positivos, deben tener el formato 'mm' y 'yyyy' respectivamente, o ingresa 'q' si deseas salir." )

def exit_verifier( user_answer : str ) -> bool: # Verificador de Salida y terminación del Programa
    if( user_answer.lower() == 'q' ): # Condición de Salida
        return True

def is_month_year_valid( number : int, type : ValidatorType ): # Validador
    if( ( type == ValidatorType.MONTH and number >= MIN_MONTH and number <= MAX_MONTH ) or ( type == ValidatorType.YEAR and number >= MIN_YEAR ) ):
        return True
    return False

def friday_13_verifier( month : int, year : int ) -> bool: # Verificador
    fecha = datetime.strptime( f"13/{month}/{year}", "%d/%m/%Y" )

    if( fecha.weekday() == DayOfWeek.FRIDAY._value_ ):
        return True
    return False

def main():
    exit_msj = f"[green]\n✅ Esto ha sido todo por hoy.\n❤ Muchas gracias por ejecutar este Script, hasta la próxima...💻 Happy Coding!,👋🏼 bye :D\n😎 Clark."
    month = 0
    year = 0
    
    print( "[bold green]\n*** Reto #12: VIERNES 13 - By @ClarkCodes ***" )
    
    while True:
        main_menu()

        try: # Ingreso de Información
            print( "\n[bold green]Número del mes[/bold green]", end = "" )
            user_answer = typer.prompt( "", default="01" )

            if exit_verifier( user_answer ): # Condición de Salida
                print( exit_msj )
                break

            month = int( user_answer ) # Conversión del mes a entero
            
            print( "\n[bold green]Número del año[/bold green]", end = "" )
            user_answer = typer.prompt( "", default="1900" )
            
            if exit_verifier( user_answer ): # Condición de Salida
                print( exit_msj )
                break

            year = int( user_answer )
            
            # Validadción y Verificación de la Fecha
            if( is_month_year_valid( month, ValidatorType.MONTH ) and is_month_year_valid( year, ValidatorType.YEAR ) ):
                print( f"\n[green]Resultado: ", end = "" )
                
                if friday_13_verifier( month, year ): # Verificador
                    month_item = list( MonthOfYear )[month - 1]
                    print( f"[yellow]✅ El mes ingresado SI tiene un Viernes 13 en el año indicado." )
                    print( f"[green]Es el[/green] [yellow]Viernes, 13 de {month_item.name} del {year}[/yellow]" )
                else:
                    print( f"[red]❌ El mes ingresado NO tiene un Viernes 13 en el año indicado." )

            else:
                print( "\n❌ Solo se admiten números enteros positivos, mayor o igual a 1 y menor o igual a 12 para el mes y mayor o igual a 1900 para el año, o la letra 'q' si deseas salir, verifique nuevamente." )

        except ValueError as ve:
            print( "\n❌ Valor ingresado no permitido, solo se admiten números enteros positivos, mayor o igual a 1 y menor o igual a 12 para el mes y mayor o igual a 1900 para el año, o la letra 'q' si deseas salir, verifique nuevamente." )

        except Exception as ex:
            print( "\n❌ Oops... algo no ha salido bien, revise nuevamente por favor." )

# Llamada a la Función Principal usando typer
if __name__ == "__main__":
    typer.run( main )
