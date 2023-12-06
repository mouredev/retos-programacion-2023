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

import 'package:mysql1/mysql1.dart';

/**
 * Clase que representa una conexión a una base de datos MySQL
 *
 */
class MySQLConnector{
  String host;
  int port;
  String user;
  String password;
  String database;
  MySqlConnection? connection;



  MySQLConnector({required this.host, required this.port,required this.user, required this.password,required this.database});

  Future<void> connect() async{

    try{
      connection = await MySqlConnection.connect(ConnectionSettings(
          host: host,
          port: port,
          user: user,
          db: database,
          password: password));
    }catch(e){
      print(e);
    }

  }

  Future<void> disconnect() async{
    try{
      await connection!.close();
    }catch(e){
      print(e);
    }
  }
  /**
   * Funcion que realiza una consulta a la base de datos y devuelve una promesa con el resultado
   * @returns Promise<any> Promesa con el resultado de la consulta
   * @param query Consulta a realizar
   */
  Future<List<Map<String,dynamic>>> query(String query) async{
    List<Map<String,dynamic>> list = [];
    try{
      await connect();
      final results = await connection?.query(query);
      for(var row in results?.toList() ?? []){
        list.add(row.fields);
      }
      return list;
    }catch(e){
      print(e);
      return list;
    }
  }
}

void main() async{
  final connection = MySQLConnector(host: 'mysql-5707.dinaserver.com', port: 3306, user: 'mouredev_read', password: 'mouredev_pass', database: 'moure_test');
  await connection.query('SELECT * FROM `challenges`').then((value) {
    print(value);
  });
  connection.disconnect();
}