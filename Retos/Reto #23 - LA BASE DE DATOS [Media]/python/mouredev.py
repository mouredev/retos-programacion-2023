import mysql.connector

config = {
    "host": "mysql-5707.dinaserver.com",
    "port": "3306",
    "database": "moure_test",
    "user": "mouredev_read",
    "password": "mouredev_pass" 
}

connection = mysql.connector.connect(**config)
cursor = connection.cursor()

query = "SELECT * FROM challenges"
cursor.execute(query)
result = cursor.fetchall()

for row in result:
    print(row)

cursor.close()
connection.close()