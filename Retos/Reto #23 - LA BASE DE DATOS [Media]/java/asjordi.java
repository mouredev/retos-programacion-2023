import java.sql.*;
import java.util.Date;
import java.util.Properties;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Database {

    public static void main(String[] args) {

        String url = "jdbc:mysql://mysql-5707.dinaserver.com:3306/moure_test";
        Properties props = databaseProperties();

        try (Connection c =  DriverManager.getConnection(url, props);
            Statement stmt = c.createStatement();
             ResultSet rs = stmt.executeQuery("SELECT * FROM challenges")) {
                while (rs.next()){
                    int id = rs.getInt("id");
                    String name = rs.getString("name");
                    String difficulty = rs.getString("difficulty");
                    Date date = rs.getDate("date");
                    System.out.println("id: " + id + " name: " + name + " difficulty: " + difficulty + " date: " + date +"\n");
                }
        } catch (SQLException e) {
            Logger.getLogger(Database.class.getName()).log(Level.SEVERE, null, e);
        }

    }

    private static Properties databaseProperties(){
        Properties p = new Properties();
        p.setProperty("user", "mouredev_read");
        p.setProperty("password", "mouredev_pass");
        return p;
    }

}
