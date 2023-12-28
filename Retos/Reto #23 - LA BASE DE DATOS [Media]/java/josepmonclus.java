import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

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

public class josepmonclus {

    private static final String MYSQL_URL = "jdbc:mysql://mysql-5707.dinaserver.com:3306/moure_test";
    private static final String MYSQL_USER = "mouredev_read";
    private static final String MYSQL_PASS = "mouredev_pass";
    
    public static void main(String[] args) {
        josepmonclus josepmonclus = new josepmonclus();

        List<Challenge> challenges = josepmonclus.getChallenges();

        for(Challenge c : challenges) {
            System.out.println(c.toString());
        }
    }

    private List<Challenge> getChallenges() {
        List<Challenge> challenges = new ArrayList<>();

        try {
            Class.forName("com.mysql.jdbc.Driver");
            Connection con = DriverManager.getConnection(
                MYSQL_URL,
                MYSQL_USER,
                MYSQL_PASS);

            Statement stmt = con.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM `challenges`");

            while (rs.next()) {
                Challenge challenge = new Challenge(
                    rs.getInt("id"), 
                    rs.getString("name"), 
                    rs.getString("difficulty"), 
                    new Date(rs.getDate("date").getTime()));
                challenges.add(challenge);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        return challenges;
    }
  
    public class Challenge {
        int id;
        String name;
        String difficulty;
        Date date;

        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");

        public Challenge(int id, String name, String difficulty, Date date) {
            this.id = id;
            this.name = name;
            this.difficulty = difficulty;
            this.date = date;
        }

        // Getters & setters...

        @Override
        public String toString() {
            return id + " | " + name + " | " + difficulty + " | " + sdf.format(date);
        }        
    }
}
