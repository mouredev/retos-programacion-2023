import pymysql

host = 'mysql-5707.dinaserver.com'
# Port: 3306
usuario = 'mouredev_read'
password =  'mouredev_pass'
db = 'moure_test'

conexion = pymysql.connect(
host=host,
user=usuario,
password=password,
db=db,
charset='utf8mb4',
cursorclass=pymysql.cursors.DictCursor)

cursor = conexion.cursor()

sql = "SELECT * FROM challenges"

cursor.execute(sql)
datos = cursor.fetchall()

cursor.close()
conexion.close()

for dato in datos:
    print (dato)
