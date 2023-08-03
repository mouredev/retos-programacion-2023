"""
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
"""

import mysql.connector


def connection_with_mysql(config, query):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        cursor.execute(query)
        result = cursor.fetchall()

        return result if result else None
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    finally:
        if connection is not None:
            connection.close()
        if cursor is not None:
            cursor.close()


print("Connection with MySQL")

query = "SELECT * FROM challenges"
config = {
    "host": "mysql-5707.dinaserver.com",
    "port": "3306",
    "database": "moure_test",
    "user": "mouredev_read",
    "password": "mouredev_pass" 
}
for i in connection_with_mysql(config, query):
    print(i)