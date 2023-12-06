/*
Para que funcione se debe tener instalado Node.js y el siguiente recurso:
   "mysql": "^2.15.0",
*/
const mysql = require("mysql");

function startConnection() {
  return mysql.createConnection({
    host: "mysql-5707.dinaserver.com",
    user: "mouredev_read",
    password: "mouredev_pass",
    database: "moure_test",
    port: 3306,
  });
}

function getInformation() {
  try {
    const connection = startConnection();

    let sql = "SELECT * FROM challenges";

    connection.query(sql, (err, row) => {
      if (err) {
        console.log(err);
        return;
      } else {
        console.table(row);
        return;
      }
    });

    connection.end();
  } catch (error) {
    console.log(error);
  }
}

getInformation();
