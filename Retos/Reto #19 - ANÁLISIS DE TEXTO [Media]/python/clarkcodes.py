# Retos Semanales ‘23
# Reto #19: ANÁLISIS DE TEXTO
# MEDIA | Publicación: 11/05/23 | Resolución: 15/05/23
#
# Crea un programa que analice texto y obtenga:
# - Número total de palabras.
# - Longitud media de las palabras.
# - Número de oraciones del texto (cada vez que aparecen un punto).
# - Encuentre la palabra más larga.
#
# Todo esto utilizando un único bucle.

# Autor: Clark - @ClarkCodes
# Fecha de Resolución: 16/05/2023

# Imports
import traceback
import typer
from rich import print
from rich.table import Table
from rich import box
from rich.progress import Progress, SpinnerColumn, TextColumn
import tkinter as tk
from tkinter import filedialog
from enum import Enum
import re

# Constantes
MAX_OPTS_NUM = 2
OPT_NO_DISPONIBLE = "Opción no diponible. La configuración no se ha alterado."

# Atributos Globales
text_File_Path = "" 
text_To_Analize = "" # Entrada de texto del usuario que se requiere analizar
text_From_File = False
is_Text_Set = False

# Preparación para el cuadro de diálogo de abrir archivo con tkinter
root = tk.Tk()
root.withdraw()
file_Path = ""

# Enum
class OptionType( Enum ):
    SET_TEXT = 1
    ANALIZE_TEXT = 2

class TextType( Enum ):
    FROM_FILE = 1
    KEYBOARD_INPUT = 2

# Funciones
def main_menu():
    #print( "[bold green]* Menú Principal *[/bold green]\nElija una de las opciones disponibles." )
    options_table = Table( "[green]Opción", "[green]Descripción", title="[bold green]* Menú Principal *[/bold green]\nElija una de las opciones disponibles", title_justify="center", caption_justify="center" )
    options_table.add_row( "1. ", "Establecer Texto a Analizar" )
    options_table.add_row( "2. ", "Analizar Texto" )
    options_table.add_row( "q. ", "Salir" )
    print( options_table )

def set_text_from_file():
    global file_Path
    global text_To_Analize

    print( f"\n* Establecer texto desde archivo\nSeleccione un archivo de texto como fuente:" )

    with Progress( SpinnerColumn(), TextColumn( "[progress.description]{task.description}" ) ) as progress:
        progress.add_task( description="[light_sky_blue1]Preparando cuadro de diálogo... un momento por favor...", total=None )

    file_Path = filedialog.askopenfilename( title="Texto desde archivo", defaultextension=".txt" ) # Ruta del archivo de texto que se requiere analizar
    
    if( file_Path ):
        with open( file_Path, 'r' ) as file:
            text_To_Analize = file.read()
    else:
        text_To_Analize = ""

def set_text_from_keyboard_input():
    global text_To_Analize
    print( f"\n* Establecer texto desde teclado" )
    text_To_Analize = typer.prompt( "Texto a analizar" )

def set_text(): # Setting the Text to analyze
    global text_From_File
    global is_Text_Set
    text_state = ""
    text_source = ""

    if( not is_Text_Set ):
        text_state = "no "

    print( f"\n* Establecer texto a analizar" )
    print( f"Estado actual: Texto {text_state}establecido{text_source}.\n" )
    options_table = Table( "[green]Opción", "[green]Descripción", title="Elija una opción", title_justify="center", caption_justify="center" )
    options_table.add_row( "1. ", "Texto desde archivo." )
    options_table.add_row( "2. ", "Texto ingresado por teclado." )
    print( options_table )

    user_op = int( typer.prompt( "\nOpción elegida" ) )

    if( user_op == TextType.FROM_FILE.value or user_op == TextType.KEYBOARD_INPUT.value ):
        text_From_File = user_op == TextType.FROM_FILE.value

        if( user_op == TextType.FROM_FILE.value ): 
            set_text_from_file()
            text_source = "archivo"
        elif( user_op == TextType.KEYBOARD_INPUT.value ):
            set_text_from_keyboard_input()
            text_source = "teclado"
            
        if ( text_To_Analize ): # Se verifica que el texto halla sido establecido correctamente
            print( f"\n[green]✔ Listo, texto establecido desde {text_source}." )
            is_Text_Set = True
        else:
            print( f"\n[red]❌ El texto no se ha estableció, vuelva a establecerlo." )
            is_Text_Set = False
    else:
        print( f"[bright_black]{OPT_NO_DISPONIBLE}" )

def text_analizer():
    global text_To_Analize
    global is_Text_Set

    if( is_Text_Set ):
        words_count = 0
        average_words_len = 0
        sentences_count = 0
        longest_words = []

        words_len = []
        temp_word = ""

        words = text_To_Analize.replace( "\n", " " ).split( " " ) # Se divide todo el texto en una lista de palabras, sin embargo hay que refinarlo dado que cada palabra puede contener signos de puntuación y/o espacios

        for word in words: # Motor de análisis: Único Bucle permitido usar indicado en las instrucciones, el cual recorre la lista de palabras y donde se va analizando cada palabra y llevando cuentas
            if( len( word ) != 0 ):
                if( "." in word ): # Se van contando las oraciones en cada iteración
                    sentences_count += 1

                temp_word = re.sub( r"[^\w]", "", word ) # Se usa una expresión regular para filtrar solamente la palabra actual sin signos de puntuación ni otros caracteres
                words_count += 1 # Se van contando las palabras

                words_len.append( len( temp_word ) ) # Se va llevando el registro de las longitudes de las palabras en la lista correspondiente

            if( len( longest_words ) == 0 or len( longest_words[0] ) == len( temp_word ) ): # Palabra o Palabras más largas
                longest_words.append( temp_word )

            elif( len( temp_word ) > len( longest_words[0] ) ):
                longest_words.clear()
                longest_words.append( temp_word )
                
        # Operaciones posteriores al bucle - Se prepara el reporte final
        average_words_len = sum( words_len ) / len( words_len )

        longest_words_str = ""
        if( len( longest_words ) > 1 ): # Se prepara una cadena presentable y amigable con el usuario, que contengan las palabras más largas si hubiera más de una, sino se presenta la unica palabra que halla
            for i, w in enumerate( longest_words ):
                longest_words_str += f"{w}"
                if ( i < len( longest_words ) - 1 ):
                    longest_words_str += ", "
        else:
            longest_words_str = longest_words[0]        
        
        # Report
        report_table = Table( "[bold green]Parámetro", "[bold green]Valor", title="[bold yellow]** Reporte General **", title_justify="center", box=box.ROUNDED )
        report_table.add_row( "[green]Número total de palabras:[/green]", f"[yellow]{words_count}" )
        report_table.add_row( "[green]Longitud media de palabras:[/green]", f"[yellow]{average_words_len:.2f}" )
        report_table.add_row( "[green]Número de oraciones en el texto:[/green]", f"[yellow]{sentences_count}" )
        report_table.add_row( "[green]Palabra/s más larga/s:[/green]", f"[yellow]{longest_words_str}" )
        print( f"\n[green]✔ Listo, texto analizado.\n" )
        print( report_table )

    else:
        print( "\nNo se ha establecido un texto a analizar todavía, establezca el texto primero." )


def main():
    while True:
        print( "[bold green]\n*** Reto #19: ANÁLISIS DE TEXTO - By @ClarkCodes ***\n" )
        main_menu()

        userOp = typer.prompt( "\nOpción elegida" )
        
        if( userOp == 'q' or userOp == 'Q' ): # Condición de Salida
            print( "[green]\n✅ Esto ha sido todo por hoy.\n❤ Muchas gracias por ejecutar este Script, hasta la próxima...💻 Happy Coding!,👋🏼 bye :D\n😎 Clark." )
            break

        try:
            userNumericOption = int( userOp ) # Se convierte la opcion ingresada por el usuario de texto a entero
            
            if( userNumericOption >= 1 and userNumericOption <= MAX_OPTS_NUM ): # Se verifica si la opción ingresada es válida, estando dentro el rango de opciones disponibles
                
                if( userNumericOption == OptionType.SET_TEXT.value ): # Option #1
                    set_text()
                elif( userNumericOption == OptionType.ANALIZE_TEXT.value ): # Option #2
                    with Progress( SpinnerColumn(), TextColumn( "[progress.description]{task.description}" ) ) as progress:
                        progress.add_task( description="[light_sky_blue1]Analizando Texto... un momento por favor...", total=None )

                    text_analizer()
            else:
                print( "❌ Opción ingresada no disponible, ingrese solo una de las opciones disponibles en el menú, verifique nuevamente." )
            
        except ValueError as ve:
            print( "\n❌ Opción ingresada no disponible, ingrese solo una de las opciones disponibles en el menú, verifique nuevamente." )
            #print( f"{ve}\n{traceback.print_exc()}" )
        except Exception as ex:
            print( "\n❌ Oops... algo no ha salido bien, revise nuevamente por favor." )
            #print( f"{ex}\n{traceback.print_exc()}" )

    raise typer.Abort()
    

# Llamada a la Función Principal usando typer
if __name__ == "__main__":
    typer.run( main )
