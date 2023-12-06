import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class EspinoLeandroo {
    public static void main(String[] args) {
        String jdbcUrl = "jdbc:mysql://mysql-5707.dinaserver.com:3306/moure_test";
        String user = "mouredev_read";
        String password = "mouredev_pass";

        try {
            // Establecer la conexión a la base de datos
            Connection connection = DriverManager.getConnection(jdbcUrl, user, password);
            System.out.println("Conexión exitosa a la base de datos");

            // Crear una sentencia SQL
            String query = "SELECT * FROM challenges";
            Statement statement = connection.createStatement();

            // Ejecutar la consulta
            ResultSet resultSet = statement.executeQuery(query);

            // Imprimir los resultados
            while (resultSet.next()) {
                int id = resultSet.getInt("id");
                String description = resultSet.getString("description");
                System.out.println("ID: " + id + ", Descripción: " + description);
            }

            // Cerrar la conexión
            resultSet.close();
            statement.close();
            connection.close();
            System.out.println("Conexión cerrada");
        } catch (Exception e) {
            System.out.println("Error al conectarse a la base de datos: " + e.getMessage());
        }
    }
}

