import mysql.connector

print("Resultados de mysql")

conexion = mysql.connector.connect(host="mysql-5707.dinaserver.com", user="mouredev_read", passwd="mouredev_pass", db="moure_test")
cur = conexion.cursor()
cur.execute("SELECT * FROM challenges")

for i in cur.fetchall():
  print(i)

conexion.close()