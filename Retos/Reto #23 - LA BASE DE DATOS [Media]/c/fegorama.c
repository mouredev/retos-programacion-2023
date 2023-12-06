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
 *
 * -------------------------------------------------------------------------------
 * Compilar con GCC y MariaDB Connector/C:
 * gcc .\reto23_mysql.c -o .\reto23_mysql.exe \
 * 			-I"C:\Program Files\MariaDB\MariaDB Connector C 64-bit\include" \
 * 			-L"C:\Program Files\MariaDB\MariaDB Connector C 64-bit\lib" \
 * 			-l libmariadb
 * -------------------------------------------------------------------------------
 */
#include "C:/Program Files/MariaDB/MariaDB Connector C 64-bit/include/mysql.h"
#include <stdio.h>
#include <stdlib.h>

#define CHALLENGES_FIELD_ID 0
#define CHALLENGES_FIELD_NAME 1
#define CHALLENGES_FIELD_DIFFICULTY 2
#define CHALLENGES_FIELD_DATE 3

int main()
{
	MYSQL *conn;
	MYSQL_RES *res;
	MYSQL_ROW row;

	/* Configuration */
	const char *host = "mysql-5707.dinaserver.com";
	const char *user = "mouredev_read";
	const char *password = "mouredev_pass";
	const char *database = "moure_test";
	const int port = 3306;

	/* Initialize connection */
	if ((conn = mysql_init(NULL)) == NULL)
	{
		fprintf(stderr, "Initializing error: %s", mysql_error(conn));
		exit(1);
	}

	/* Connect to database */
	if (!mysql_real_connect(conn, host, user, password,
							database, port, NULL, 0))
	{
		fprintf(stderr, "%s\n", mysql_error(conn));
		exit(1);
	}

	/* send SQL query */
	if (mysql_query(conn, "SELECT * FROM `challenges`"))
	{
		fprintf(stderr, "%s\n", mysql_error(conn));
		exit(1);
	}

	res = mysql_use_result(conn);

	/* output table name */
	printf("Result of query:\n");

	while ((row = mysql_fetch_row(res)) != NULL)
		printf("%s  %s, %s, %s\n", row[CHALLENGES_FIELD_ID],
			   row[CHALLENGES_FIELD_NAME],
			   row[CHALLENGES_FIELD_DIFFICULTY],
			   row[CHALLENGES_FIELD_DATE]);

	/* close connection */
	mysql_free_result(res);
	mysql_close(conn);

	return 0;
}