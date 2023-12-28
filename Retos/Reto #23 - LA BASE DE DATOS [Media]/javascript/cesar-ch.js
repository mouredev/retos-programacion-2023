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

import { createConnection } from 'mysql'

let connection = createConnection({
    host: 'mysql-5707.dinaserver.com',
    port: 3306,
    user: 'mouredev_read',
    password: 'mouredev_pass',
    database: 'moure_test'
})

connection.connect()

connection.query('SELECT * FROM `challenges`', (err, rows, fields) => {
    if (err) throw err;
    let result = JSON.parse(JSON.stringify(rows))

    console.log('-----------------------------------------------------------------------------------------')
    console.log('   ID    |          NAME          |           DIFFICULT         |             DATE       ')
    result.map(e => {
        console.log('-------------------------------------------------------------------------------------')
        console.log(`   ${e.id}     | ${e.name}  |       ${e.difficulty}       | ${e.date}`)
        console.log('-------------------------------------------------------------------------------------')
    })
})


connection.end();