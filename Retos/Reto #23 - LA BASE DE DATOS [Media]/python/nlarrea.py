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

host = "mysql-5707.dinaserver.com"
user = "mouredev_read"
password = "mouredev_pass"
database = "moure_test"

try:
    conn = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM challenges")
    rows = cursor.fetchall()

    for row in rows:
        challenge_id, name, difficulty, date = row
        print(f"{challenge_id}: {name} ({difficulty}) - {date}")

except mysql.connector.Error as err:
    print("Error while connecting to Database", err)
    
finally:
    cursor.close()
    conn.close()