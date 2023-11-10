import java.sql.*;

public class cesarjv {
    public static void main(String[] args) {
        try(Connection conn=getInstance();
            Statement stmt=conn.createStatement();
            ResultSet rs=stmt.executeQuery("SELECT * FROM challenges")){

            while(rs.next()){
                System.out.print(rs.getInt(1));
                System.out.print(" | ");
                System.out.print(rs.getString(2));
                System.out.print(" | ");
                System.out.print(rs.getString(3));
                System.out.print(" | ");
                System.out.println(rs.getString(4));
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private static Connection getInstance() throws SQLException {
        final String url="jdbc:mysql://mysql-5707.dinaserver.com:3306/moure_test?serverTimezone=America/Caracas";
        final String username="mouredev_read";
        final String password="mouredev_pass";
        Connection connection = null;
        connection = DriverManager.getConnection(url, username, password);
        return connection;
    }
}
