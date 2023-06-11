"""
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
import mysql.connector

HOST = "mysql-5707.dinaserver.com"
PORT = 3306
USER = "mouredev_read"
PASSWORD = "mouredev_pass"
DATABASE = "moure_test"


database = mysql.connector.connect(
    host=HOST,
    port=PORT,
    user=USER,
    password=PASSWORD,
    database=DATABASE
)

cursor = database.cursor()

cursor.execute("SELECT * FROM challenges")

results = cursor.fetchall()

[print(result) for result in results]