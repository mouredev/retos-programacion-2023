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

const connection = mysql.createConnection({
  host: 'mysql-5707.dinaserver.com',
  port: '3306',
  user: 'mouredev_read',
  password: 'mouredev_pass',
  database: 'moure_test',
});

connection.connect();

connection.query('SELECT * FROM challenges', (error, rows) => {
  if (error) throw error;
  rows.map((x) => {
    console.log(x.id, x.name, x.difficulty, x.date.toDateString());
  });
});

connection.end();
