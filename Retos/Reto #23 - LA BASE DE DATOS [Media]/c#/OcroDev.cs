// See https://aka.ms/new-console-template for more information
/*
 * Realiza una conexión desde el lenguaje que hayas seleccionado a la siguiente
 * base de datos MySQL:
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

using MySql.Data.MySqlClient;

namespace OcroDev;

public class Program
{
    static void Main(string[] args)
    {
        string connectionString = @"
            server=mysql-5707.dinaserver.com;
            port=3306;
            user=mouredev_read;
            password=mouredev_pass;
            database=moure_test;
        ";

        MySqlConnection connection = new(connectionString);
        try
        {
            connection.Open();

            string query = "SELECT * FROM challenges";

            MySqlCommand command = new MySqlCommand(query, connection);
            MySqlDataReader reader = command.ExecuteReader();
            Console.WriteLine("[");
            while (reader.Read())
            {  
                string id = reader.GetString("id");
                string name = reader.GetString("name");
                string difficulty = reader.GetString("difficulty");
                string date = reader.GetString("date");
                Console.WriteLine(" RowDataPacket{");
                Console.WriteLine($"  id:{id},");
                Console.WriteLine($"  name:{name},");
                Console.WriteLine($"  difficulty:{difficulty},");
                Console.WriteLine($"  date:{date}");
                Console.WriteLine(" }");
            }
            Console.WriteLine("]");

            reader.Close();

            connection.Close();
        }

        catch(Exception ex) 
        {
            Console.WriteLine(ex.ToString());
        }
    }
};
