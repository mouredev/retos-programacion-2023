"""
Retos Semanales ‘23
Reto #23: LA BASE DE DATOS
MEDIA | Publicación: 06/06/23 | Resolución: 12/06/23

 * Realiza una conexión desde el lenguaje que hayas seleccionado a la siguiente
 * base de datos MySQL:
 * - Host: mysql-5707.dinaserver.com
 * - Port: 3306
 * - User: mouredev_read
 * - Password: mouredev_pass
 * - Database: moure_test
 * 
 * Una vez realices la conexión, lanza la siguiente consulta e imprime el resultado:
 * - SELECT * FROM `challenges`
 *
 * Se pueden usar librerías para realizar la lógica de conexión a la base de datos.
"""

# Autor: Clark - @ClarkCodes
# Fecha de Resolución: 07/06/2023

# NOTA: Para ejecutar este Script debes tener instalado MySQL Connector/Python 8.0.33, 
# el cual lo puedes descargar de la página oficial dev.mysql.com

# Imports
import mysql.connector
from mysql.connector import errorcode
import typer
from rich import print
from rich.table import Table
from rich import box
from rich.progress import Progress, SpinnerColumn, TextColumn
from datetime import date

# Constantes
CONFIG = { 
    "user" : "mouredev_read", 
    "password" : "mouredev_pass", 
    "host" : "mysql-5707.dinaserver.com", 
    "port" : 3306,
    "database" : "moure_test", 
    "raise_on_warnings" : True 
    }

def data_retriever():
    query = "SELECT * FROM `challenges`"

    try:
        db_connection = mysql.connector.connect( **CONFIG )

        with Progress( SpinnerColumn(), TextColumn( "[progress.description]{task.description}" ) ) as progress:
            progress.add_task( description="[light_sky_blue1]Recuperando datos del servidor...", total=None )

        cursor = db_connection.cursor()
        cursor.execute( query ) # Se ejecuta la query

        rows = cursor.fetchall() # Se obtienen los registros

        cursor.close() # Se cierra la conexión
        db_connection.close()
        
        # Se prepara la tabla para mostrar los datos
        data_table = Table( "[green]ID", "[green]Nombre", "[green]Dificultad", "[green]Fecha", title="[bold yellow]** Datos Obtenidos: Challenges **", title_justify="center", box=box.ROUNDED )

        for row in rows:
            data_table.add_row( str( row[0] ), row[1], row[2], row[3].strftime( "%d/%m/%Y" ) )

        print( "" )
        return data_table

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print( "Nombre de usuario o contraseña incorrectos, verifique nuevamente." )

        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print( "La Base de Datos no existe." )

        else:
            print(err)

    else:
        cursor.close()
        db_connection.close()
    
def main():
    print( "[bold green]\n*** Reto #23: LA BASE DE DATOS - By @ClarkCodes ***" )

    print( "[green]\n¡Bienvenidos!, a continuación nos conectaremos a la Base de Datos Remota y mostraremos los datos en una tabla." )

    while True:
        print( "[bold green]\nPresiona cualquier tecla para empezar, o presiona 'q' para salir: [/bold green]", end = "" )
        userAnswer = input( "" )
        
        if( userAnswer == 'q' or userAnswer == 'Q' ): # Condición de Salida
            print( "[green]\n✅ Esto ha sido todo por hoy.\n❤ Muchas gracias por ejecutar este Script, hasta la próxima...💻 Happy Coding!,👋🏼 bye :D\n😎 Clark." )
            break

        try:
            print( "" )
            with Progress( SpinnerColumn(), TextColumn( "[progress.description]{task.description}" ) ) as progress:
                progress.add_task( description="[light_sky_blue1]Estableciendo conexión con el servidor... un momento por favor...", total=None )
            
            print( "" )
            print( data_retriever() ) # Se llama a la función para obtener los datos y se los muestra por pantalla

        except Exception as ex:
            print( "\n❌ Oops... algo no ha salido bien, revise nuevamente por favor." )
            print( ex )

# Llamada a la Función Principal usando typer
if __name__ == "__main__":
    typer.run( main )
