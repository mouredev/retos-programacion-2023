'''
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
'''
import mysql.connector

connection = mysql.connector.connect(user='mouredev_read', 
                                   password='mouredev_pass',
                                   host='mysql-5707.dinaserver.com',
                                   database='moure_test',
                                   port='3306')

cursor = connection.cursor()

query = "SELECT * FROM `challenges`"
cursor.execute(query)

result = cursor.fetchall()

connection.close()

for row in result:
    print(row)
