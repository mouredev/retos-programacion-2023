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

import mysql from 'mysql';

const host = 'mysql-5707.dinaserver.com';
const user = 'mouredev_read';
const password = 'mouredev_pass';
const database = 'moure_test';

const conn = mysql.createConnection({
    host,
    user,
    password,
    database
});

conn.connect();

conn.query('SELECT * FROM challenges', function (error, results) {
    if (error) throw error;

    results.forEach(result => {
        let day = result.date.getDate() >= 10 ? result.date.getDate() : '0'+result.date.getDate();
        let month = (result.date.getMonth() + 1) >= 10 ? (result.date.getMonth() + 1) : '0'+String(result.date.getMonth() + 1);
        let year = result.date.getFullYear();
        let formatDate = `${day}-${month}-${year}`;
        
        console.log(`${result.id}. ${result.name} (${result.difficulty}) - ${formatDate}`);
    });
});

conn.end();