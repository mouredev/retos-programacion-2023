/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs: 
 * https://github.com/public-apis/public-apis
 */

// Usare la api de fakerapi.it para crear personas aleatorias
// y mostrarlas en la terminal

// ignore_for_file: uri_does_not_exist
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  getAndPrintPersons();
}

const baseUrl = 'https://fakerapi.it/api/v1/persons';

void getAndPrintPersons() async {
  final res = await http.get(Uri.parse(baseUrl));
  final data = json.decode(res.body)['data'];
  int index = 1;
  data.forEach((person) {
    String firstName = person['firstname'];
    String lastName = person['lastname'];

    print('$index: $firstName $lastName');
    index++;
  });
}
