// Importamos la librería MySQL y la interfaz Connection
const mysql = require("mysql2")

// Se crea un objeto con la interfaz Connection que se conectará a la BD.
const conexion = mysql.createConnection({
    host: "mysql-5707.dinaserver.com",
    port: 3306,
    user: "mouredev_read",
    password: "mouredev_pass",
    database: "moure_test"
})

conexion.execute("SELECT * FROM challenges", (error, resultado) => {
    if (error) {
        console.log("Error al ejecutar la consulta de SQL");
    }

    console.log(resultado);
});
