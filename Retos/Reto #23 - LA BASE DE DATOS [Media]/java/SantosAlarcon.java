import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;

public class App {
    public static void main(String[] args) throws Exception {
        // Creamos el objeto Connection y lo ponemos a NULL.
        Connection conexion = null;

        // Se crea una conexión a la BD usando DriverManager.
        conexion = DriverManager.getConnection("jdbc:mysql://mysql-5707.dinaserver.com:3306/moure_test", "mouredev_read", "mouredev_pass");

        // Se prepara primero la consulta y luego se ejecuta.
        ResultSet rs = conexion.prepareStatement("SELECT * FROM challenges").executeQuery();

        // Se va iterando con cada uno de las filas y se imprime la información de cada columna.
        while(rs.next()) {
            System.out.printf("ID: %d\nNombre: %s\nDificultad: %s\n\nFecha: %s\n",rs.getInt("id"), rs.getString("name"), rs.getString("difficulty"), rs.getString("date"));
        }

        // Se cierre la conexión a la BD.
        conexion.close();
    }
}

