#!/usr/bin/env python3

# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# Challenge #23: The database
# Challenge of Mouredev
# Link: https://github.com/mouredev/retos-programacion-2023

# Reto #23: La base de datos
#### Dificultad: Media | Publicación: 06/06/23 | Corrección: 12/06/23

## Enunciado

# Realiza una conexión desde el lenguaje que hayas seleccionado a la siguiente base de datos MySQL:
# - Host: mysql-5707.dinaserver.com
# - Port: 3306
# - User: mouredev_read
# - Password: mouredev_pass
# - Database: moure_test

# Una vez realices la conexión, lanza la siguiente consulta e imprime el resultado:
# - SELECT # FROM `challenges`
#
# Se pueden usar librerías para realizar la lógica de conexión a la base de datos.

#pip install mysql-connector-python

# -------------------- Extern Imports --------------------
import mysql.connector
import datetime

# -------------------- APP --------------------
class Credentials:

    def __init__(self) -> None:
        
        self.host = "mysql-5707.dinaserver.com"
        self.port = 3306
        self.user = "mouredev_read"
        self.password = "mouredev_pass"
        self.database = "moure_test"

class Info:

    def about():

        _about = """# Code By 14Wual
# Challenge #23: The database
# Challenge of Mouredev
# Link: https://github.com/mouredev/retos-programacion-2023\n"""

        print(_about)

    def return_str_current_datetime():
        current_datetime = datetime.datetime.now()
        return str(current_datetime.strftime("%Y-%m-%d %H:%M:%S"))

class Challeng:

    def __init__(self) -> None:

        Info.about()
        
        self.ddbb_credentials = Credentials()
        self.connection = self.create_connection()
        
        if self.connection:

            print(f"[✓] - {Info.return_str_current_datetime()} Established connection.")
            print(f"[Info] - {Info.return_str_current_datetime()} Running query.")

            try:
                cursor = self.connection.cursor()
                cursor.execute("SELECT * FROM challenges")
                
                output = cursor.fetchall()

                # output = [
                #   (*, 'E* ****** "**** ****"', '*****', datetime.date(****, **, **)), 
                #   (*, 'E* "******** ******"', '*****', datetime.date(****, **, *)), 
                #   (*, 'E* ******* ** *****', '*****', datetime.date(****, **, *)), 
                #   Rest of output...
                # ]

                print(f"[✓] - {Info.return_str_current_datetime()} Query executed successfully.")
                print(f"[Info] - {Info.return_str_current_datetime()} Closing connection.")
                
                try:cursor.close();self.connection.close()
                finally:print(f"[✓] - {Info.return_str_current_datetime()} Connection closed correctly.")

                print(f"[Info] - {Info.return_str_current_datetime()} Showing results.")
                Challeng.beautifull_print_output(output)

            except mysql.connector.Error as error:Exceptions(expecific="Error executing query", error=error)
        
        else:print("[x] The connection could not be completed.")

    def create_connection(self):

        print(f"[Info] - {Info.return_str_current_datetime()} Connecting to the database.")

        try:return mysql.connector.connect(host=self.ddbb_credentials.host,port=self.ddbb_credentials.port,user=self.ddbb_credentials.user,password=self.ddbb_credentials.password,database=self.ddbb_credentials.database)
        except mysql.connector.errors.InterfaceError as error:Exceptions(expecific="InterfaceError", error=error)
        except mysql.connector.Error as error:Exceptions(expecific="Other", error=error)
        return None
    
    def beautifull_print_output(output):

        print("\n----- Challenges -----")
        for row in output:
            print("ID:", row[0])
            print("Title:", row[1])
            print("Difficulty:", row[2])
            print("Date:", row[3])
            print("----------------------")

        # ----- Challenges -----
        # ID: *
        # Title: E* ****** "**** ****"
        # Difficulty: *****
        # Date: ****-**-**
        # ----------------------
        # Rest of output...
        # ----------------------

class Exceptions:
    def __init__(self, expecific, error) -> None:
        print(f"[x] - {Info.return_str_current_datetime()} Type of error: ", expecific, f"\n[x] - {Info.return_str_current_datetime()} Error: " ,error)
    
if __name__ == '__main__':Challeng()