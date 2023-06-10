using System;
using MySql.Data.MySqlClient;

namespace Reto23;

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


class Program
{
    static void Main()
    {
        string connectionString = 
            "Server=mysql-5707.dinaserver.com; Database=moure_test;Uid=mouredev_read;Pwd=mouredev_pass";

        GetDataFromServer(connectionString);
        Console.ReadKey();
        
    }

    private static void GetDataFromServer(string connectionString)
    {
        string queryString = "SELECT * FROM challenges";

        using (MySqlConnection connection = new MySqlConnection(connectionString))
        {
            try
            {
                MySqlCommand command = new MySqlCommand(queryString, connection);
                connection.Open();
                Console.WriteLine("conected");

                MySqlDataReader reader = command.ExecuteReader();

                while (reader.Read())
                {
                    for (int i = 0; i < reader.FieldCount; i++) Console.Write(reader.GetString(i) + " | ");
                    
                    Console.WriteLine();
                }

                connection.Close();
            }

            catch(MySqlException e)
            {
                Console.WriteLine($"Error code: {e.Code}-{e.Message}");
            }
        }
    }
}