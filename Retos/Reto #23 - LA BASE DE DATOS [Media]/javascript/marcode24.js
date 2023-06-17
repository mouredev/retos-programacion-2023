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
  user: 'mouredev_read',
  password: 'mouredev_pass',
  database: 'moure_test',
});

connection.connect();

connection.query('SELECT * FROM challenges', (error, results) => {
  if (error) throw error;
  console.table(results);
  // ┌─────────┬────┬───────────────────────────────┬────────────┬──────────────────────────┐
  // │ (index) │ id │             name              │ difficulty │           date           │
  // ├─────────┼────┼───────────────────────────────┼────────────┼──────────────────────────┤
  // │    0    │ 1  │    'EL FAMOSO "FIZZ BUZZ"'    │  'Fácil'   │ 2022-12-26T06:00:00.000Z │
  // │    1    │ 2  │    'EL "LENGUAJE HACKER"'     │  'Fácil'   │ 2023-01-02T06:00:00.000Z │
  // │    2    │ 3  │     'EL PARTIDO DE TENIS'     │  'Media'   │ 2023-01-09T06:00:00.000Z │
  // │    3    │ 4  │ 'EL GENERADOR DE CONTRASEÑAS' │  'Media'   │ 2023-01-16T06:00:00.000Z │
  // │    4    │ 5  │   'PRIMO, FIBONACCI Y PAR'    │  'Media'   │ 2023-01-23T06:00:00.000Z │
  // └─────────┴────┴───────────────────────────────┴────────────┴──────────────────────────┘
});

connection.end();

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
