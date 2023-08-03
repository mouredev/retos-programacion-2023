import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class algama12 {

    public static void main(String[] args) {

        String url = "jdbc:mysql://mysql-5707.dinaserver.com:3306/moure_test";
        String usuario = "mouredev_read";
        String contra = "mouredev_pass";

        Connection connection = null;
        Statement statement = null;
        ResultSet resultSet = null;

        try {
            connection = DriverManager.getConnection(url, usuario, contra);

            statement = connection.createStatement();

            resultSet = statement.executeQuery("SELECT * FROM challenges");

            while (resultSet.next()) {
                int id = resultSet.getInt("id");
                String challengeName = resultSet.getString("name");
                System.out.println("ID: " + id + ", Name: " + challengeName);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            // Cerrar los recursos
            try {
                if (resultSet != null) resultSet.close();
                if (statement != null) statement.close();
                if (connection != null) connection.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}
