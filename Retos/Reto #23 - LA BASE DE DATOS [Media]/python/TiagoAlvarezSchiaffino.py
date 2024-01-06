import mysql.connector

def connect_to_database():
    """
    Establish a connection to the MySQL database.

    Returns:
        mysql.connector.connection_cext.CMySQLConnection: The database connection object.
    """
    try:
        host = "mysql-5707.dinaserver.com"
        port = 3306
        user = "mouredev_read"
        password = "mouredev_pass"
        database = "moure_test"

        connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )

        if connection.is_connected():
            print("Connection to the database successful")
            return connection
        else:
            print("Unable to connect to the database")
            return None

    except mysql.connector.Error as error:
        print("Error connecting to the database:", error)
        return None

def execute_query(connection, query):
    """
    Execute a SQL query on the connected database and print the results.

    Args:
        connection (mysql.connector.connection_cext.CMySQLConnection): The database connection object.
        query (str): The SQL query to execute.
    """
    try:
        cursor = connection.cursor(dictionary=True)  # Using a dictionary cursor for easier result handling

        cursor.execute(query)

        results = cursor.fetchall()

        for row in results:
            print(row)

        cursor.close()
    except mysql.connector.Error as error:
        print("Error executing query:", error)

def main():
    # Connect to the database
    connection = connect_to_database()

    if connection:
        try:
            # Define the SQL query
            query = "SELECT * FROM `challenges`"

            # Execute the query and print the results
            execute_query(connection, query)

        finally:
            # Close the database connection
            connection.close()
            print("Connection closed")

if __name__ == "__main__":
    main()
