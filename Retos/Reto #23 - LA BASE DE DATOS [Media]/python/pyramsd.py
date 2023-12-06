# install mysql-connector-python (pip install mysql-connector-python)
import mysql.connector

user = "mouredev_read"
password = "mouredev_pass"
host = "mysql-5707.dinaserver.com"
port = "3306"
database = "moure_test"

conexion = None

try: 
    conexion = mysql.connector.connect(user=user, password=password,
                                    host=host, database=database,
                                    port=port)

    
    consulta = "SELECT * FROM challenges"
    
    cursor = conexion.cursor() # realiza consultas
    cursor.execute(consulta) # ejecuta la consulta

    resultados = cursor.fetchall() # leer y descartar resultado para cerrar conexion

    for i in resultados:
        print(i)

except:
    print("Error al conectar a la base de datos")

finally:
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()

    print("Conexion cerrada")
    
