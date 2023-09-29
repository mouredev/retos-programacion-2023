"""
Retos Semanales ‘23
Reto #25: EL CÓDIGO KONAMI
MEDIA | Publicación: 19/06/23 | Resolución: 26/06/23

 * Crea un programa que detecte cuando el famoso "Código Konami" se ha introducido
 * correctamente desde el teclado. 
 * Si sucede esto, debe notificarse mostrando un mensaje en la terminal.
"""

# Autor: Clark - @ClarkCodes
# Fecha de Resolución: 25/07/2023

# Imports
import typer
from rich import print
import random
from pynput.keyboard import Key, KeyCode, Listener

# Constantes
PHRASES = [ "Ok... interesante... cuéntame más.", "Muy bien, suena cool... ¿qué más?", "Bien, bien... qué curioso... sigue contandome :)", "Cool!, te sigo leyendo...", "Me gusta leerte :) ... continua por favor..." ]
KONAMI_CODE = ( Key.up, Key.up, Key.down, Key.down, Key.left, Key.right, Key.left, Key.right, KeyCode.from_char( "b" ), KeyCode.from_char( "a" ) )
KONAMI_CODE_LETTERING = f"""[bold yellow]
██╗  ██╗ ██████╗ ███╗   ██╗ █████╗ ███╗   ███╗██╗     ██████╗ ██████╗ ██████╗ ███████╗
██║ ██╔╝██╔═══██╗████╗  ██║██╔══██╗████╗ ████║██║    ██╔════╝██╔═══██╗██╔══██╗██╔════╝
█████╔╝ ██║   ██║██╔██╗ ██║███████║██╔████╔██║██║    ██║     ██║   ██║██║  ██║█████╗  
██╔═██╗ ██║   ██║██║╚██╗██║██╔══██║██║╚██╔╝██║██║    ██║     ██║   ██║██║  ██║██╔══╝  
██║  ██╗╚██████╔╝██║ ╚████║██║  ██║██║ ╚═╝ ██║██║    ╚██████╗╚██████╔╝██████╔╝███████╗
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
"""

# Variables Globales
welcomePending = True
consecutiveCodeKeysPressed = 0
_exit = False

# Funciones
def main_menu():
    global welcomePending

    if( welcomePending ):
        print( "[green]\nBienvenido al Script de [yellow]El Código Konami[/yellow], esto es algo similar a un diario, un espacion donde me puedes contar acerca de ti, de tu día, y de todo lo que quieras, o presiona la tecla ESCAPE para salir.[/green] 😀" )
        welcomePending = False
    else:
        print( f"[dodger_blue2]\n{random.choice( PHRASES )}" ) # Frases mostradas aleatoriamente

def key_listener( key ):
    global _exit
    global consecutiveCodeKeysPressed

    if( key == KONAMI_CODE[consecutiveCodeKeysPressed] ): # Solo si se empieza a introducir el código Konami en orden se va sumando 1 al contador
        consecutiveCodeKeysPressed += 1
    else: # Si no se completa el código Konami en orden se reestablece el valor del contador a 0
        if( consecutiveCodeKeysPressed > 0 ):
            consecutiveCodeKeysPressed = 0

    if( consecutiveCodeKeysPressed == len( KONAMI_CODE ) ): # Si el contador es igual a la longitud del Código Konami, significa que se ha introducido toda la secuencia en orden y se muestra el mensaje correspondiente
        print( f"\n\n[yellow]Ha ingresado el Código Konami!, se ha desbloqueado una funcionalidad secreta :)" )
        print( KONAMI_CODE_LETTERING )
        consecutiveCodeKeysPressed = 0

    if key == Key.esc: # Si el usuario presiona la tecla ESCAPE en el siguiente enter cuando salga del input se termina el programa
        print( f"\n\n[yellow]Has presionado la tecla ESCAPE, el programa terminará cuando presiones ENTER.\n" )
        _exit = True
        return False

def main():
    global _exit
    print( "[bold green]\n*** Reto #25: EL CÓDIGO KONAMI - By @ClarkCodes ***" )

    listener = Listener( on_release = key_listener ) # Listener, importantisimo, funcionalidad core, se le pasa la función callback que tiene la lógica
    listener.start() # Se lo ejecuta en otro hilo para no bloquear el input del usuario y que se vea el texto que se introduce, se lo hace una sola vez y esta escuchando en todo momento.

    while True:
        main_menu()

        print( "\n[bold green]Respuesta: ", end = "" )

        try:
            user_answer = input( "" )

            if( _exit ): # Condición de Salida
                print( "[green]\n✅ Esto ha sido todo por hoy.\n❤ Muchas gracias por ejecutar este Script, hasta la próxima...💻 Happy Coding!,👋🏼 bye :D\n😎 Clark." )
                break

        except ValueError as ve:
            print( "\n❌ Opción ingresada no disponible, solo se admiten números enteros positivos mayores o iguales a 2, o la letra 'q' si deseas salir, verifique nuevamente." )
            print( ve )
        except Exception as ex:
            print( "\n❌ Oops... algo no ha salido bien, revise nuevamente por favor." )
            print( ex )

# Llamada a la Función Principal usando typer
if __name__ == "__main__":
    typer.run( main )
