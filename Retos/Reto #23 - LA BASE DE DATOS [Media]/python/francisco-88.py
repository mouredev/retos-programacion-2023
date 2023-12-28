import mysql.connector

conexion = mysql.connector.connect(user='mouredev_read',
                                   password='mouredev_pass',
                                   host='mysql-5707.dinaserver.com',
                                   database='moure_test')

cursor = conexion.cursor()

print('Conexión exitosa')

query = ("SELECT * FROM challenges")
cursor.execute(query)

for row in cursor:
    print(row)

cursor.close()
conexion.close()

print('Desafío terminado')