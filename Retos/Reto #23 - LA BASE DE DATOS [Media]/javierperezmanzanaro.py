"""/*
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
 */
    """

import mysql.connector as mysql


def conexion():
    try:
        HOST = 'mysql-5707.dinaserver.com'
        port = 3306
        USER = 'mouredev_read'
        PASSWORD = 'mouredev_pass'
        DATABASE = 'moure_test'
        db_connection = mysql.connect(  host=HOST,
                                        database=DATABASE,
                                        user=USER,
                                        password=PASSWORD)
        # print("Conexón realizada:", db_connection.get_server_info())
    except:
        print('Error durante la conexión')
    return db_connection



if __name__ == '__main__':
    db_connection = conexion()
    cursor=db_connection.cursor()
    query = ('SELECT * FROM `challenges`')
    cursor.execute(query)
    print(cursor)

    resultado = cursor.fetchall()

    for x in resultado:
        print(x)

    db_connection.close()