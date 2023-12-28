/*
 * El día 128 del año celebramos en la comunidad el "Hola Mundo day"
 * Vamos a hacer "web scraping" sobre su sitio web: https://holamundo.day
 *
 * Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
 * del día 8. Mostrando hora e información de cada uno.
 * Ejemplo: "16:00 | Bienvenida"
 *
 * Se permite utilizar librerías que nos faciliten esta tarea.
 *
 */

// Se ignoran los errores porque solo se puede ejecutar en un proyecto de Dart
// ignore_for_file: undefined_function, uri_does_not_exist, undefined_class
import 'package:http/http.dart' as http;
import 'package:html/parser.dart';
import 'package:html/dom.dart';

Future fetchUrl(String url) async {
  final response = await http.get(Uri.parse(url));
  return parse(response.body);
}

void main() async {
  String url = 'https://holamundo.day';
  final document = await fetchUrl(url);
  final h1List = document.querySelectorAll('h1');

  Element? h1Schedules;
  h1List.forEach((el) {
    if (el.innerHtml.contains('Agenda 8 de mayo')) h1Schedules = el;
  });

  Element? sibling = h1Schedules!.nextElementSibling;
  do {
    print(sibling!.text);
    sibling = sibling.nextElementSibling;
  } while (sibling!.text.contains(':'));
}
