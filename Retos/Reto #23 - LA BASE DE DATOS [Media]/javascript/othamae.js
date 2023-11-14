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

const mysql = require('mysql');


const connection  = mysql.createConnection({
    user: 'mouredev_read',
    host: 'mysql-5707.dinaserver.com',
    database: 'moure_test',
    password: 'mouredev_pass',
    port: 3306,
  })
  
connection.connect((error)=>{
    if (error){
        console.log('Unable to connect to the database: ',error)
    } else{
        console.log('Connection has been established.')
    }    
  }) 
  
connection.query('SELECT * FROM `challenges`', function (error, results) {
    if (error){
        console.log('Error to query: ',error)
    }
    else{
        console.log('Query results: ',results)
    }
})

connection.end((error)=>{
    if (error){
        console.log('Error to end: ',error)
    } else{
        console.log('Connection has been closed.')
    }
})

