"""
Reto #23 de conexión a MySQL de MoureDev
By Santos Alarcón Asensio.
"""

# Se importa la librería MySQL Connector
import mysql.connector

# Se crea el objeto 'conector'
connector = mysql.connector.connect(
    host="mysql-5707.dinaserver.com",
    port=3306,
    user="mouredev_read",
    password="mouredev_pass",
    database="moure_test"
)

# Crearemos un 'cursor'
cursor = connector.cursor()

# Con este 'cursor' haremos la consulta SQL
cursor.execute("SELECT * FROM challenges")

# Obtenemos TODOS los resultados de la consulta del cursor
resultados = cursor.fetchall()

# Se cierra el cursor y la conexión a la BD.
cursor.close()
connector.close()

print(resultados)
