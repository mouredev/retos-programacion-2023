# /*
# * Realiza una conexión desde el lenguaje que hayas seleccionado a la siguiente base de datos MySQL:
#  * - Host: mysql-5707.dinaserver.com
#  * - Port: 3306
#  * - User: mouredev_read
#  * - Password: mouredev_pass
#  * - Database: moure_test
#  *
#  * Una vez realices la conexión, lanza la siguiente consulta e imprime el resultado:
#  * - SELECT * FROM `challenges`
#  *
#  * Se pueden usar librerías para realizar la lógica de conexión a la base de datos.
#  */

from mysql.connector import connect



class MySQLConnector:
    def __init__(self, host, port, user, password, database):
        self.__host = host
        self.__port = port
        self.__user = user
        self.__password = password
        self.__database = database

    def __connect(self):
        return connect(
            host=self.__host,
            port=self.__port,
            user=self.__user,
            password=self.__password,
            database=self.__database
        )

    def execute_query(self, query):
        connection = self.__connect()
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        connection.close()
        return result



if __name__ == '__main__':
    mysql = MySQLConnector(
        host='mysql-5707.dinaserver.com',
        port=3306,
        user='mouredev_read',
        password='mouredev_pass',
        database='moure_test'
    )
    result = mysql.execute_query('SELECT * FROM `challenges`')
    for row in result:
        print(row)