import pymysql;

conexion = pymysql.connect(
host = 'mysql-5707.dinaserver.com',
user = 'mouredev_read',
password =  'mouredev_pass',
db = 'moure_test',
charset='utf8mb4',
cursorclass=pymysql.cursors.DictCursor)

cursor = conexion.cursor()

sql = "SELECT * FROM challenges"

cursor.execute(sql)
rows = cursor.fetchall()

cursor.close()
conexion.close()

for row in rows:
    print (row)
