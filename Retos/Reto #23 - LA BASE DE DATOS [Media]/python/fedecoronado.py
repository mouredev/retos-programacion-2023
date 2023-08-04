# Reto #23: La base de datos
#
# Realiza una conexión desde el lenguaje que hayas seleccionado a la siguiente base de datos MySQL:
# - Host: mysql-5707.dinaserver.com
# - Port: 3306
# - User: mouredev_read
# - Password: mouredev_pass
# - Database: moure_test
#
# Una vez realices la conexión, lanza la siguiente consulta e imprime el resultado:
# - SELECT # FROM `challenges`
#
# Se pueden usar librerías para realizar la lógica de conexión a la base de datos.
#

import mysql.connector
from mysql.connector import errorcode

from rich.table import Table
from rich import box
from rich import print

from datetime import date

class DbConnection:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def __enter__(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conexión exitosa a la base de datos")
            return self.connection
        except mysql.connector.Error as error:
            print("Error al conectarse a la base de datos:", error)
            return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()
            print("Desconexión exitosa de la base de datos")



def execute_query(connection, query):
    if not connection:
        print("No se ha establecido una conexión a la base de datos")
        return

    try:
        cursor = connection.cursor()
        cursor.execute( query ) # Se ejecuta la query
        rows = cursor.fetchall() # Se obtienen los registros
        cursor.close() # Se cierra la conexión
        connection.close()
        # Se prepara la tabla para mostrar los datos
        data_table = Table( 
                        "[blue]ID", "[blue]Nombre", "[red]Dificultad", "[blue]Fecha", 
                        title="[orange]** Datos Obtenidos: Challenges **", 
                        title_justify="center", 
                        box=box.ROUNDED
                        )
        # se llena la tabla con los datos del cursor
        for row in rows:
            data_table.add_row( 
                            str( row[0] ), 
                            row[1], 
                            row[2], 
                            row[3].strftime( "%d/%m/%Y" )
                        )
        return data_table
    except mysql.connector.Error as error:
        print("Error al ejecutar la consulta:", error)



if __name__ == "__main__":
    # Parámetros de conexión
    host = "mysql-5707.dinaserver.com"
    port = 3306
    user = "mouredev_read"
    password = "mouredev_pass"
    database = "moure_test"

    # Conectarse a la base de datos utilizando with para que se cierre sola
    with DbConnection(host, port, user, password, database) as connection:
        if connection:
            query = "SELECT * FROM `challenges`" # Ejecutar la consulta
            print(execute_query(connection, query))