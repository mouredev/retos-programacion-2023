const mysql = require("mysql");

const ejecutarConsulta = async () => {
	const connection = mysql.createConnection({
		host: "mysql-5707.dinaserver.com",
		port: "3306",
		user: "mouredev_read",
		password: "mouredev_pass",
		database: "moure_test",
	});

	try {
		const connectAsync = () => {
			return new Promise((resolve, reject) => {
				connection.connect((err) => {
					if (err) {
						console.error(
							"Error al conectar a la base de datos:",
							err
						);
						reject(err);
					} else {
						resolve();
					}
				});
			});
		};
		await connectAsync();

		const queryAsync = () => {
			return new Promise((resolve, reject) => {
				connection.query(
					"SELECT * FROM customers",
					function (err, result, fields) {
						connection.end();

						if (err) {
							console.error(
								"Error al ejecutar la consulta:",
								err
							);
							reject(err);
						} else {
							console.log(result);
							resolve(result);
						}
					}
				);
			});
		};

		const resultado = await queryAsync();
		return resultado;
	} catch (error) {
		console.error("Error general:", error);
		throw error;
	}
};

ejecutarConsulta();
