import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;

public class Qv1ko {

    public static void main(String[] args) {

        Connection con = null;
        java.sql.Statement stmt = null;
        ResultSet rs = null;

        try {
            Class.forName("com.mysql.jdbc.Driver");
            con = DriverManager.getConnection("jdbc:mysql://mysql-5707.dinaserver.com:3306/moure_test", "mouredev_read", "mouredev_pass");
            stmt = con.createStatement();
            rs = stmt.executeQuery("SELECT * FROM `challenges`");
            while (rs.next()) {
                System.out.println(rs.getString("id") + ". " + rs.getString("name") + " (" + rs.getString("difficulty") + ") - " + rs.getString("date"));
            }
            con.close();
        } catch (Exception exc) {
            exc.printStackTrace();
        } finally {
            try {
                if(rs != null) {
                    rs.close();
                }
                if(stmt != null) {
                    stmt.close();
                }
                if(con != null) {
                    con.close();
                }
            } catch (SQLException exc) {
                exc.printStackTrace();
            }
        }
        
    }

}
