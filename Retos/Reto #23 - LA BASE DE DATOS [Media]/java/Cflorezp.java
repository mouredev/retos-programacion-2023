package reto23baseDatos;

import java.sql.*;

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
public class Cflorezp {

    public static void main(String[] args) {
        String url = "jdbc:mysql://mysql-5707.dinaserver.com:3306/moure_test";
        String usuario = "mouredev_read";
        String contraseña = "mouredev_pass";


        try {
            Class.forName("com.mysql.cj.jdbc.Driver");

            Connection conexion = DriverManager.getConnection(url, usuario, contraseña);

            Statement statement = conexion.createStatement();

            String consulta = "SELECT * FROM challenges";
            ResultSet resultado = statement.executeQuery(consulta);

            ResultSetMetaData metaData = resultado.getMetaData();
            int columnCount = metaData.getColumnCount();

            System.out.println("\n-------------------------------------");
            System.out.println("DATOS TABLA 'CHALLENGES'");
            System.out.println("-------------------------------------");
            while (resultado.next()) {
                for (int i = 1; i <= columnCount; i++) {
                    String columnName = metaData.getColumnName(i);
                    String value = resultado.getString(i);
                    System.out.println(columnName + ": " + value);
                }
                System.out.println("-------------------------------------");
            }

            resultado.close();
            statement.close();
            conexion.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}








