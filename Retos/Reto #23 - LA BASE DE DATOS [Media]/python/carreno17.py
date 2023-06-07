import datetime
import mysql.connector

"""

# Reto #23: La base de datos
#### Dificultad: Media | Publicación: 06/06/23 | Corrección: 12/06/23

## Enunciado

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


def  connect_database(host: str, user: str, password: str, database: str, port: str, query: str):

    try:
        db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
        )
        query_database(db, query)
    except: 
        print('Error connecting to database, please try again')
    

def query_database(db, query: str) -> dict:
    
    cursor = db.cursor()
    cursor.execute(query)

    results = cursor.fetchall()
    
    for row in results:
        print(row)    

    cursor.close()
    db.close()

if __name__ == "__main__":
    connect_database("mysql-5707.dinaserver.com", 
                     "mouredev_read", 
                     "mouredev_pass", 
                     "moure_test", 
                     "3306",
                     "SELECT * FROM challenges" )