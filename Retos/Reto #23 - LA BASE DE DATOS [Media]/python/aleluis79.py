"""
Realiza una conexión desde el lenguaje que hayas seleccionado a la siguiente base de datos MySQL:
- Host: mysql-5707.dinaserver.com
- Port: 3306
- User: mouredev_read
- Password: mouredev_pass
- Database: moure_test

Una vez realices la conexión, lanza la siguiente consulta e imprime el resultado:
- SELECT * FROM `challenges`
Se pueden usar librerías para realizar la lógica de conexión a la base de datos.
"""

# pip install mysql-connector-python
import mysql.connector

def imprime_resultado(table: str, titles: tuple, sizes: tuple) -> None:

    conexion = mysql.connector.connect(
        host="mysql-5707.dinaserver.com",
        user="mouredev_read",
        password="mouredev_pass",
        database="moure_test"
    )

    stitles = str(titles).replace('\'', '')
    stitles = stitles[1:len(stitles)-1]

    cursor = conexion.cursor()

    consulta = f"SELECT {stitles} FROM {table}"
    cursor.execute(consulta)

    resultados = cursor.fetchall()

    for i in range(len(titles)):
        print(titles[i].capitalize().ljust(sizes[i]), end=" ")
    print()
    print("="*(sum(sizes)+len(titles)-1))

    for fila in resultados:
        for i in range(len(fila)):
            print(str(fila[i]).ljust(sizes[i]), end=" ")
        print()

    cursor.close()
    conexion.close()


imprime_resultado("challenges", ("id", "name", "difficulty", "date"), (11, 100, 10, 10))