import mysql.connector

config = {
    "host": "mysql-5707.dinaserver.com",
    "port": "3306",
    "database": "moure_test",
    "user": "mouredev_read",
    "password": "mouredev_pass" 
}

try:
    with mysql.connector.connect(**config) as connection:
        with connection.cursor() as cursor:
            query = "SELECT * FROM challenges"
            cursor.execute(query)
            
            result = cursor.fetchall()
            
            for row in result:
                print(row)

except mysql.connector.Error as error:
    print(f"Error en la conexión o consulta: {error}")
