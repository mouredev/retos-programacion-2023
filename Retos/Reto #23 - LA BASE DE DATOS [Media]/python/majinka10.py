import mysql.connector

config = {
  'user': 'mouredev_read',
  'password': 'mouredev_pass',
  'host': 'mysql-5707.dinaserver.com',
  'database': 'moure_test',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

query='SELECT * FROM challenges'
cursor.execute(query)
result = cursor.fetchall()

for row in result:
    print(row)

cursor.close()
cnx.close()