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


/**
 * Clase que representa una conexión a una base de datos MySQL
 *
 */
class MysqlConnection {
    host: string;
    port: number;
    user: string;
    password: string;
    database: string;
    connection: mysql.Connection;

    /**
     * Constructor de la clase
     * @param host
     * @param port
     * @param user
     * @param password
     * @param database
     */
    constructor(host: string, port: number, user: string, password: string, database: string) {
        this.host = host;
        this.port = port;
        this.user = user;
        this.password = password;
        this.database = database;
        this.connection = mysql.createConnection({
            host: this.host,
            port: this.port,
            user: this.user,
            password: this.password,
            database: this.database
        });

    }

    /**
     * Funcion que cierra la conexión a la base de datos
     */
    close(): void {
        this.connection?.end();
    }

    /**
     * Funcion que realiza una consulta a la base de datos y devuelve una promesa con el resultado
     * @returns Promise<any> Promesa con el resultado de la consulta
     * @param query Consulta a realizar
     */
    query(query: string): Promise<any> {
        return new Promise((resolve, reject) => {
            this.connection.query(query, (error, results, fields) => {
                if (error) reject(error);
                resolve(results);
            });

        })
    }


}

const connection = new MysqlConnection('mysql-5707.dinaserver.com', 3306, 'mouredev_read', 'mouredev_pass', 'moure_test');
connection.query('SELECT * FROM `challenges`').then((results) => {
    console.log(results);
    connection.close();
}).catch((error) => {
    console.log(error);
})


