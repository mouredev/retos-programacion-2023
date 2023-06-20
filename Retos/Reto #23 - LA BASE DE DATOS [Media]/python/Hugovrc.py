import mysql.connector

config = {
    'user': 'mouredev_read',
    'password': 'mouredev_pass',
    'host': 'mysql-5707.dinaserver.com',
    'database': 'moure_test',
    'port': '3306'
}

con = mysql.connector.connect(**config)
cursor = con.cursor()

query = ("SELECT * FROM challenges")

cursor.execute(query)

for datos in cursor:
    print(datos)

cursor.close()
con.close()