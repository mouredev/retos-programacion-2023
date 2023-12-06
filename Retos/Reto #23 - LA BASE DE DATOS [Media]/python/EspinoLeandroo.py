import mysql.connector

def main():
    try:
        # Parámetros de conexión
        host = "mysql-5707.dinaserver.com"
        port = 3306
        user = "mouredev_read"
        password = "mouredev_pass"
        database = "moure_test"

        # Crear la conexión a la base de datos
        connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )

        if connection.is_connected():
            print("Conexión exitosa a la base de datos")

            # Crear un cursor para ejecutar consultas
            cursor = connection.cursor()

            # Consulta
            query = "SELECT * FROM `challenges`"

            # Ejecutar la consulta
            cursor.execute(query)

            # Obtener los resultados
            results = cursor.fetchall()

            # Imprimir los resultados
            for row in results:
                print(row)

            # Cerrar cursor y conexión
            cursor.close()
            connection.close()
            print("Conexión cerrada")
        else:
            print("No se pudo conectar a la base de datos")

    except mysql.connector.Error as error:
        print("Error al conectarse a la base de datos:", error)

if __name__ == "__main__":
    main()
