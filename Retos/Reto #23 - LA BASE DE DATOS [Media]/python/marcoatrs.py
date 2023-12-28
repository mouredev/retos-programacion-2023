from mysql import connector

conn = connector.connect(
    host="mysql-5707.dinaserver.com",
    user="mouredev_read",
    password="mouredev_pass",
    port=3306,
    database="moure_test",
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM challenges")
res = cursor.fetchall()

for row in res:
    print(row)
