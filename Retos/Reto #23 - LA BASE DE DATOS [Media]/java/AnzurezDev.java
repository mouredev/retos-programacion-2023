import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class AnzurezDev {
    private static String URL   = "JDBC:mysql://mysql-5707.dinaserver.com:3306/moure_test?serverTimezone=UTC";
    private static String USER  = "mouredev_read";
    private static String PASS  = "mouredev_pass";
    private static String JDBC  = "com.mysql.cj.jdbc.Driver";
    private static String QUERY = "SELECT * FROM challenges";

    public static void main(String[] args) {
        Connection connection   = null;
        Statement statement     = null;
        ResultSet resultSet     = null;

        try {
            connection   = DriverManager.getConnection( URL, USER, PASS );
            Class.forName( JDBC );
            statement     = connection.createStatement();
            resultSet     = statement.executeQuery( QUERY );

            while ( resultSet.next() ) {
                System.out.println( resultSet.getInt(1) + "\t" + resultSet.getString(2) + "\t" + resultSet.getString(3) + "\t" + resultSet.getString(4) );
            }
        } catch ( Exception e ) {
            e.printStackTrace();
        } finally {
            try {
                if ( resultSet != null )
                    resultSet.close();
                if ( statement != null )
                    statement.close();
                if ( connection != null )
                    connection.close();
            } catch ( SQLException e ) {
                e.printStackTrace();
            }
        }
    }
}