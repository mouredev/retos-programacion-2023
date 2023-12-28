import mysql.connector
from colorama import Fore, Style

class MySQLConnector:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print(Fore.GREEN + "Conexión exitosa a la base de datos MySQL" + Style.RESET_ALL)
        except mysql.connector.Error as error:
            print(Fore.RED + "Error al conectar a la base de datos:", error + Style.RESET_ALL)

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            return results
        except mysql.connector.Error as error:
            print(Fore.RED + "Error al ejecutar la consulta:", error + Style.RESET_ALL)

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

# Ejemplo de uso
if __name__ == "__main__":
    host = 'mysql-5707.dinaserver.com'
    port = 3306
    user = 'mouredev_read'
    password = 'mouredev_pass'
    database = 'moure_test'

    connector = MySQLConnector(host, port, user, password, database)
    connector.connect()

    query = 'SELECT * FROM challenges'
    results = connector.execute_query(query)

    if results:
        for row in results:
            print(Fore.CYAN + str(row) + Style.RESET_ALL)

    connector.close()
