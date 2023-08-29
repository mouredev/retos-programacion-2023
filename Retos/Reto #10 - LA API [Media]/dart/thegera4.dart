/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs: 
 * https://github.com/public-apis/public-apis
 */

import 'dart:convert';
import 'dart:io';
import 'package:http/http.dart' as http;

void main(){
  fetchData();
}

fetchData() async {
  var url = 'https://dog.ceo/api/breeds/list/all';
  var httpClient = new HttpClient();
  var request = await httpClient.getUrl(Uri.parse(url));
  var response = await request.close();
  var responseBody = await response.transform(utf8.decoder).join();
  var data = jsonDecode(responseBody);
  print(data);
}