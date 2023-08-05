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
using MySql.Data.MySqlClient;


namespace Reto23
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Connection();
            Console.ReadKey();

        }
        public static void Connection()
        {
            string connectionString = "server=mysql-5707.dinaserver.com;user=mouredev_read;database=moure_test;password=mouredev_pass;";
            using (MySqlConnection connection = new MySqlConnection(connectionString))
            {
                connection.Open();

                string query = "SELECT * FROM challenges;"; 

                using (MySqlCommand command = new MySqlCommand(query, connection))
                {
                    using (MySqlDataReader reader = command.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            string column0Value = reader.GetString(0);                                                                      
                            string column1Value = reader.GetString(1);
                            string column2Value = reader.GetString(2);
                            string column3Value = reader.GetString(3);

                            Console.WriteLine($"Column1: {column0Value}, Column2: {column1Value}, Column2: {column2Value}, Column2: {column3Value}");
                        }
                    }
                }
            }
        }
    }
}
