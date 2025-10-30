"""
Realiza una conexión desde el lenguaje que hayas seleccionado a la siguiente
base de datos MySQL:
- Host: mysql-5707.dinaserver.com
- Port: 3306
- User: mouredev_read
- Password: mouredev_pass
- Database: moure_test

Una vez realices la conexión, lanza la siguiente consulta e imprime el resultado:
- SELECT * FROM `challenges`

Se pueden usar librerías para realizar la lógica de conexión a la base de datos.
"""

import mysql.connector
from mysql.connector import Error

def main():
    """
    Función principal que gestiona la conexión a la base de datos MySQL,
    ejecuta una consulta SELECT sobre la tabla `challenges`
    y muestra los resultados en consola.
    """
    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host='mysql-5707.dinaserver.com',
            port=3306,
            user='mouredev_read',
            password='mouredev_pass',
            database='moure_test'
        )

        if connection.is_connected():
            print("Conexión establecida correctamente.\n")
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM challenges")
            results = cursor.fetchall()

            print("Resultados de la consulta:\n")
            for row in results:
                print(row)

    except Error as e:
        print(f"Error al conectar o ejecutar la consulta en la base de datos: {e}")
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            print("\nConexión a la base de datos cerrada correctamente.")


if __name__ == "__main__":
    main()
