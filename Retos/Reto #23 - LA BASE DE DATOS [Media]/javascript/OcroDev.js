import mysql from 'mysql'

const connection = mysql.createConnection({
  host: 'mysql-5707.dinaserver.com',
  user:'mouredev_read',
  password: 'mouredev_pass',
  database: 'moure_test'
})

connection.connect()
connection.query('SELECT * FROM challenges', (err, row) => {
  if (err) throw err
  console.log(row)
})
connection.end()


/*
 * Realiza una conexión desde el lenguaje que hayas seleccionado a la siguiente
 * base de datos MySQL:
 ? - Host: mysql-5707.dinaserver.com
 ? - Port: 3306
 ? - User: mouredev_read
 ? - Password: mouredev_pass
 ? - Database: moure_test
 * 
 * Una vez realices la conexión, lanza la siguiente consulta e imprime el resultado:
 * - SELECT * FROM `challenges`
 *
 * Se pueden usar librerías para realizar la lógica de conexión a la base de datos.
 */