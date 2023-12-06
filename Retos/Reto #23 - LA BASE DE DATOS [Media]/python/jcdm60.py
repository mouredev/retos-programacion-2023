# Reto #23: La base de datos
#### Dificultad: Media | Publicación: 06/06/23 | Corrección: 12/06/23

## Enunciado

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


def connect_to_database(host, port, user, password, database):
    try:
        connection = mysql.connector.connect(
            host=host, port=port, user=user, password=password, database=database
        )
        print("Conexión exitosa a la base de datos")
        return connection
    except mysql.connector.Error as error:
        print("Error al conectarse a la base de datos:", error)
        return None


def execute_query(connection, query):
    if not connection:
        print("No se ha establecido una conexión a la base de datos")
        return

    try:
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()

        for row in results:
            print(row)

        cursor.close()
    except mysql.connector.Error as error:
        print("Error al ejecutar la consulta:", error)


def disconnect_from_database(connection):
    if connection:
        connection.close()
        print("Desconexión exitosa de la base de datos")


if __name__ == "__main__":
    # Parámetros de conexión
    host = "mysql-5707.dinaserver.com"
    port = 3306
    user = "mouredev_read"
    password = "mouredev_pass"
    database = "moure_test"

    # Conectarse a la base de datos
    connection = connect_to_database(host, port, user, password, database)

    # Ejecutar la consulta
    query = "SELECT * FROM `challenges`"
    execute_query(connection, query)

    # Desconectarse de la base de datos
    disconnect_from_database(connection)
