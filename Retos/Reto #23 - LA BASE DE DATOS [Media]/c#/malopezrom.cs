/*
 * Realiza una conexión desde el lenguaje que hayas seleccionado a la siguiente base de datos MySQL:
 * - Host: mysql-5707.dinaserver.com
 * - Port: 3306
 * - User: mouredev_read
 * - Password: mouredev_pass
 * - Database: moure_test
 *
 * Una vez realices la conexión, lanza la siguiente consulta e imprime el resultado:
 * - SELECT * FROM `challenges`
 *
 * Se pueden usar librerías para realizar la lógica de conexión a la base de datos.
 */

using System;
using System.Text.RegularExpressions;
using System.Collections.Generic;
using MySql.Data.MySqlClient;


namespace retosProgramacion2023
{

    /**
     * Clase que representa una conexión a una base de datos MySQL
     *
     */
    public class MySQLConnection
    {
        private string connectionString;
        private MySqlConnection connection;
        /**
        * Constructor de la clase
        * @param host
        * @param port
        * @param user
        * @param password
        * @param database
        */

        public MySQLConnection(string host,int port, string user, string password, string database)
        {
            connectionString = $"server={host};user={user};database={database};port={port};password={password};";
            this.connection = new MySqlConnection(connectionString);
        }

        public bool Connect()
        {
            try
            {
                connection.Open();
                return true;
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
                return false;
            }


        }
        public void Close()
        {
            connection.Close();
        }
        /**
        * Funcion que realiza una consulta a la base de datos y devuelve una promesa con el resultado
        * @returns Promise<any> Promesa con el resultado de la consulta
        * @param query Consulta a realizar
        */
        public List<Dictionary<string,object>> Query(string query)
        {
            List<Dictionary<string,object>> result = new List<Dictionary<string,object>>();
            try
            {
                MySqlCommand command = new MySqlCommand(query, connection);
                MySqlDataReader reader = command.ExecuteReader();
                while (reader.Read())
                {
                    Dictionary<string, object> row = new Dictionary<string, object>();
                    for (int i = 0; i < reader.FieldCount; i++)
                    {
                        row.Add(reader.GetName(i), reader.GetValue(i));
                    }
                    result.Add(row);
                }
                reader.Close();
                return result;
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
                return result;
            }

        }

    }

    class Program
    {
        static void Main(string[] args)
        {

                MySQLConnection connection = new MySQLConnection("mysql-5707.dinaserver.com", 3306, "mouredev_read", "mouredev_pass", "moure_test");
                if(connection.Connect())
                {
                    List<Dictionary<string, object>> result = connection.Query("SELECT * FROM `challenges`");
                    foreach (Dictionary<string, object> row in result)
                    {
                        foreach (KeyValuePair<string, object> column in row)
                        {
                            Console.WriteLine($"{column.Key} : {column.Value}");
                        }
                        Console.WriteLine("--------------------------------------------------");
                    }
                    connection.Close();
                }
        }

    }
}