import java.sql.DriverManager

fun main() {

    /*
    *
    * Reto #23 06/06/2023 LA BASE DE DATOS
    *
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

    // Para usar los drivers de mysql en kotlin usar la siguiente entrada
    // el fichero gradle para descargar las librerías necesarias
    // implementation("mysql:mysql-connector-java:8.0.26")

    val url = "jdbc:mysql://mysql-5707.dinaserver.com:3306/moure_test"
    val usuario = "mouredev_read"
    val contraseña = "mouredev_pass"

    val conexion = DriverManager.getConnection(url, usuario, contraseña)

    val consulta = "SELECT id, name, difficulty, date FROM challenges"
    val declaracion = conexion.createStatement()
    val resultado = declaracion.executeQuery(consulta)

    while (resultado.next()) {
        val id = resultado.getString("id")
        val name = resultado.getString("name")
        val difficulty = resultado.getString("difficulty")
        val date = resultado.getString("date")

        println("#$id - $date | $difficulty | $name")

    }

    resultado.close()
    declaracion.close()

}
