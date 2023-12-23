"""/*
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
 */"""

import mysql.connector

configuracion = {
    'user': 'mouredev_read',
    'password': 'mouredev_pass',
    'host': 'mysql-5707.dinaserver.com',
    'database': 'moure_test',
    'port': '3306'
}
query = ("SELECT * FROM challenges")

def connect_server(configuracion):
    return mysql.connector.connect(**configuracion)

def main():
    conexion = connect_server(configuracion)
    cursor = conexion.cursor()
    cursor.execute(query)
    print(cursor)
    for data in cursor:
        print(data)
    cursor.close()
    conexion.close()

if __name__ == "__main__":
    main()