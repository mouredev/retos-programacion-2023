"""
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
import mysql.connector

#Realizar la conexión con los argumentos dados.
connect = mysql.connector.connect(
	user="mouredev_read",
    password="mouredev_pass", 
    host="mysql-5707.dinaserver.com",
    database='moure_test', port=3306)
    
query = "SELECT * FROM challenges"
cursor = connect.cursor()
cursor.execute(query)
result = cursor.fetchall()

#Recorrer el cursor para mostrar los resultados de la query
for item in result:
    print(item)

#Recuerda cerrar al salir para que no se escapen los bits.
cursor.close()
connect.close()
