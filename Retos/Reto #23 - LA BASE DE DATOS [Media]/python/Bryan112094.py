import mysql.connector

def consult_sql(c):
    sql = "SELECT * FROM `challenges`"
    c.execute(sql)
    rows = c.fetchall()
    for row in rows:
        print(row)

def main():
    try:
        conexion = mysql.connector.connect(
            host = 'mysql-5707.dinaserver.com',
            user = 'mouredev_read',
            password = 'mouredev_pass',
            database = 'moure_test',
            port=3306
        )
        c = conexion.cursor(dictionary=True)
        consult_sql(c)
    except mysql.connector.Error as error:
        print('No se pudo conectar la base de datos: ' + error)


if __name__ == '__main__':
    main()