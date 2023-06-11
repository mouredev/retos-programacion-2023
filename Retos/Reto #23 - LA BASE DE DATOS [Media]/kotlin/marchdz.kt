import java.sql.*
import java.time.format.DateTimeFormatter;

fun main() {
    val url = "jdbc:mysql://mysql-5707.dinaserver.com:3306/moure_test"
    val user = "mouredev_read"
    val password = "mouredev_pass"
    var connection: Connection? = null
    var statement: Statement? = null
    var resultSet: ResultSet? = null
    val dateFormatter = DateTimeFormatter.ofPattern("dd-MM-yyyy")

    try {
        connection = DriverManager.getConnection(url, user, password)
        statement = connection.createStatement()
        resultSet = statement.executeQuery("SELECT * FROM challenges")
        while (resultSet.next()) {
            println(
                "${resultSet.getInt("id")} " +
                "${resultSet.getString("name")} " +
                "${resultSet.getString("difficulty")} " +
                resultSet.getDate("date")?.toLocalDate()?.format(dateFormatter)
            )
        }
    } catch (e: SQLException) {
        println(e.message)
    } finally {
        resultSet?.close()
        statement?.close()
        connection?.close()
    }
}