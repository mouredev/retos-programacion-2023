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
import java.sql.DriverManager
import java.sql.Connection

/**
 * Clase que representa una conexión a una base de datos MySQL
 *
 */
class MySQLConnection(val host: String, val port: Int, val user: String, val password: String, val database: String){
   private var connection:Connection? = null
   init{
       try {
           connection = DriverManager.getConnection("jdbc:mysql://$host:$port/$database", user, password)
       }
         catch (e:Exception){
              println(e.message)
         }

   }
   fun close(){
        connection?.close()
   }
    /**
     * Funcion que realiza una consulta a la base de datos y devuelve una promesa con el resultado
     * @returns Promise<any> Promesa con el resultado de la consulta
     * @param query Consulta a realizar
     */
   fun query(query:String) : List<Map<String,Any?>>{
       val result : MutableList<Map<String,Any?>> =  mutableListOf()
       try {
           val statement = connection?.createStatement().use {
               val resultSet = it?.executeQuery(query)
               val metaData = resultSet?.metaData

               while (resultSet?.next() == true) {
                   val row: MutableMap<String, Any?> = mutableMapOf()
                   for (i in 1..metaData?.columnCount!!) {
                       row[metaData.getColumnName(i)] = resultSet.getObject(i)
                   }
                   result.add(row)
               }


           }
           return result
       }
         catch (e:Exception){
              println(e.message)
              return result
         }

   }
}



fun main() {
   val connection = MySQLConnection("mysql-5707.dinaserver.com",3306,"mouredev_read","mouredev_pass","moure_test")
   val results = connection.query("SELECT * FROM challenges")
    results.forEach { row ->
        row.forEach { (columnName, value) ->
            println("$columnName: $value")
        }
    }
   connection.close()
}
