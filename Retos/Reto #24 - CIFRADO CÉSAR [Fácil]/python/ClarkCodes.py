"""
Retos Semanales ‘23
Reto #24: CIFRADO CÉSAR
FÁCIL | Publicación: 12/06/23 | Resolución: 19/06/23

 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
"""

# Autor: Clark - @ClarkCodes
# Fecha de Resolución: 15/06/2023

# Imports
import typer
from rich import print
from rich.table import Table
from rich import box
from enum import Enum

# Constantes
ENCODING_VALUE = 3
MIN_OPTION = 1
MAX_OPTION = 2
UPPER_LETTERS_RANGE = range( 65, 91 )
LOWER_LETTERS_RANGE = range( 97, 123 )

# Variables Globales
welcomePending = True

# Enums
class CypherType( Enum ):
    ENCRYPT = 1
    DECRYPT = 2

# Funciones - Métodos
def main_menu():
    global welcomePending

    if( welcomePending ):
        print( "[green]\nBienvenido al Script de [yellow]El Cifrado César[/yellow], ¡vamos cifrar o decifrar un mensaje![/green] 😀" )
        welcomePending = False
    else:
        print( "[green]\n¿Ciframos o deciframos otro?" )

    options_table = Table( "[green]Opción", "[green]Acción", title="[bold yellow]* Elije una Opción *", title_justify="center", box=box.ROUNDED )
    options_table.add_row( "1.", "Cifrar/Encriptar" )
    options_table.add_row( "2.", "Decifrar/Desencriptar" )
    options_table.add_row( "q.", "Salir" )

    print( "" )
    print( options_table )

def index_validator( letter_index : int ) -> int:
    is_letter_inside_boundaries = False
    # Aplicación Heurística Algorítmica con los indices ascii de letras mayúsculas y minúsculas
    if( letter_index < 97 - ENCODING_VALUE ): # Se determina si se trata de letras minúsculas o mayúsculas - Letras mayúsculas
        if( letter_index > 90 ): # Determinar si se rebasa por arriba, de ser así se hace que dé la vuelta, lo mismo se hace si se trata del caso contrapuesto
            return 64 + ( letter_index - 90 )
        
        elif( letter_index < 65 ): # O si se reabasa por debajo
            return 91 - ( 65 - letter_index )
        
        else: # O si está dentro del rango
            is_letter_inside_boundaries = True

    else: # Letras minúsculas
        if( letter_index > 122 ):
            return 96 + ( letter_index - 122 )
        
        elif( letter_index < 97 ):
            return 123 - ( 97 - letter_index )
        
        else: 
            is_letter_inside_boundaries = True
            
    if( is_letter_inside_boundaries ): # Si está dentro del rango, simplemente se devuelve el mismo indice
        return letter_index
    
def cypher( cypher_type : CypherType, msj : str ) -> str:
    encrypted_decrypted_msj = ""
    
    for letter in msj:
        letter_index = ord( letter ) # Se obtiene el indice ascii de la letra
        encrypted_decrypted_index = 0

        if( letter_index in UPPER_LETTERS_RANGE or letter_index in LOWER_LETTERS_RANGE ):
            encrypted_decrypted_index = index_validator( letter_index + ENCODING_VALUE ) if( cypher_type == CypherType.ENCRYPT ) else index_validator( letter_index - ENCODING_VALUE )
            encrypted_decrypted_msj += chr( encrypted_decrypted_index ) # Se obtiene la letra del indice ascii del caracter

        else:
            encrypted_decrypted_msj += letter

    return encrypted_decrypted_msj

def encrypt_decrypt( cypher_type : CypherType ):
    operation_type = "cifrar/encriptar" if cypher_type == CypherType.ENCRYPT else "descifrar/desencriptar"
    past_word = "cifrado/encriptado" if cypher_type == CypherType.ENCRYPT else "descifrado/desencriptado"
    
    print( f"\nIngrese un mensaje para {operation_type}:" )
    msj = input( "Mensaje: " )

    if( len( msj ) > 0 ):
        print( f"\nSu mensaje {past_word} con Cifrado César es el siguiente:\n" )
        
        if( cypher_type == CypherType.ENCRYPT ):
            print( cypher( CypherType.ENCRYPT, msj ) )
        else:
            print( cypher( CypherType.DECRYPT, msj ) )
    else:
        print( print( "\n❌ El mensaje no puede estar vacío, verifique nuevamente." ) )

def main():
    print( "[bold green]\n*** Reto #24: CIFRADO CÉSAR - By @ClarkCodes ***" )

    while True:
        main_menu()

        print( "[bold green]Opción elegida", end = "" )
        user_answer = typer.prompt( "", default = str( 1 ) )
        
        if( user_answer == 'q' or user_answer == 'Q' ): # Condición de Salida
            print( "[green]\n✅ Esto ha sido todo por hoy.\n❤ Muchas gracias por ejecutar este Script, hasta la próxima...💻 Happy Coding!,👋🏼 bye :D\n😎 Clark." )
            break

        try:
            user_option = int( user_answer ) # Se convierte la opcion ingresada por el usuario de texto a entero

            if( user_option >= MIN_OPTION and user_option <= MAX_OPTION ):
                if( user_option == CypherType.ENCRYPT.value ): # Option #1
                    encrypt_decrypt( CypherType.ENCRYPT )

                elif( user_option == CypherType.DECRYPT.value ): # Option #2
                    encrypt_decrypt( CypherType.DECRYPT )
            else:
                print( "\n❌ Opción ingresada no disponible, ingrese solo una de las opciones disponibles en el menú, verifique nuevamente." )

        except ValueError as ve:
            print( "\n❌ Opción ingresada no disponible, solo se admiten números enteros positivos mayores o iguales a 2, o la letra 'q' si deseas salir, verifique nuevamente." )
            print( ve )
        except Exception as ex:
            print( "\n❌ Oops... algo no ha salido bien, revise nuevamente por favor." )
            print( ex )

# Llamada a la Función Principal usando typer
if __name__ == "__main__":
    typer.run( main )
