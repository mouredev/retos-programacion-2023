package reto_23;

import java.sql.*;


/*
 *
 * @author jesus
 * 
 * 
 * 
 * 
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
public class jesusWay {
    
    

    public static void main(String[] args) {
        
        
        String url = "jdbc:mysql://mysql-5707.dinaserver.com:3306/moure_test";
        String usuario = "mouredev_read";
        String clave = "mouredev_pass";
        try {
            Connection conexion = DriverManager.getConnection(url, usuario, clave);
            PreparedStatement ps = null;
            String query = "SELECT * FROM challenges";
            try {
                ps = conexion.prepareStatement(query);
                ResultSet rs = ps.executeQuery();
                System.out.printf("%3s  %30s  %-10s  %10s\n", "ID", "              NAME              "
                        , "DIFFICULTY", "   DATE   ");
                System.out.printf("%3s  %30s  %-10s  %10s\n", "**", "********************************"
                        , "**********", "**********");
                //System.out.print(rs);
                while (rs.next()) {
                    int id = rs.getInt(1);
                    String name = rs.getString(2);
                    String difficulty = rs.getString(3);
                    String date = rs.getString(4);
                    Model m = new Model(id, name, difficulty, date);
                    System.out.printf("%3d  %-32s  %-10s  %-15s\n", id, name, difficulty, date);
                }
                conexion.close();
            } catch (SQLException ex1) {
                System.out.println("ERROR SELECT: " + ex1);

            }

        } catch (SQLException ex) {
            System.out.println("ERROR CONNECTION: " + ex);

        }

    }
    
}

 class Model {
    
       private int id;
        private String name;
        private String difficulty;
        private String date;
        
        public Model(int id, String name , String difficulty, String date){
            this.id =id;
            this.name= name;
            this.difficulty=difficulty;
            this.date=date;
            
        }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDifficulty() {
        return difficulty;
    }

    public void setDifficulty(String difficulty) {
        this.difficulty = difficulty;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

 }
    
