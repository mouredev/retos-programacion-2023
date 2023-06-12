import mysql.connector

# Establecer la conexión
cnx = mysql.connector.connect(
    host='mysql-5707.dinaserver.com',
    port=3306,
    user='mouredev_read',
    password='mouredev_pass',
    database='moure_test'
)

# Crear un cursor para ejecutar consultas
cursor = cnx.cursor()

# Ejecutar la consulta
query = "SELECT * FROM challenges"
cursor.execute(query)

# Obtener los resultados
results = cursor.fetchall()

# Imprimir los resultados
for row in results:
    print(row)

# Cerrar el cursor y la conexión
cursor.close()
cnx.close()
