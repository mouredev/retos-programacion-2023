import mysql.connector

connection = mysql.connector.connect(
    host    = "mysql-5707.dinaserver.com",
    user    = "mouredev_read",
    password= "mouredev_pass",
    database= "moure_test",
    port    = 3306
)

cursor = connection.cursor()
cursor.execute( "SELECT * FROM `challenges`" )

results = cursor.fetchall()

for row in results:
    ( identifier, title, difficulty, date ) = row
    print( f'{identifier} \t {title} \t {difficulty} \t {date}' )