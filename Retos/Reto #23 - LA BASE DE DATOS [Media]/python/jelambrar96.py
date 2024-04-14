#!/usr/bin/python3

"""
# Reto #23: La base de datos
/*
 * Realiza una conexión desde el lenguaje que hayas seleccionado a la siguiente base de datos MySQL:
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
 */
"""

__author__ = "Jorge Lambraño - jelambrar96"
__copyright__ = "Copyright 2024, retos-programacion-2023"
__credits__ = ["Brais Moure - mouredev"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Jorge Lambraño"
__email__ = "jelambrar@gmail.com"
__status__ = "Production"



import mysql.connector


MYSQL_HOST = "mysql-5707.dinaserver.com"
MYSQL_PORT = "3306"
MYSQL_USERNAME = "mouredev_read"
MYSQL_PASSWORD = "mouredev_pass"
MYSQL_DATABASE = "moure_test"


# Connect to MySQL database
def connect_to_database():
    connection = None
    try:
        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USERNAME,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE
        )
    except mysql.connector.Error as error:
        print("Error connecting to MySQL database:")
        print(error)
    return connection


def main():
    connection = connect_to_database()
    if connection is None:
        return

    cursor = connection.cursor()
    results = []

    try:
        consulta = f"SELECT * FROM challenges"
        cursor.execute(consulta)
        results = cursor.fetchall()
    except mysql.connector.Error as error:
        print(error)
    
    for item in results:
        print(item)

    cursor.close()
    connection.close()


if __name__ == '__main__':
    main()
