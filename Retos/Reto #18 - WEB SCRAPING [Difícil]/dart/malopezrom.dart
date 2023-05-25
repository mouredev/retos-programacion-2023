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



import 'package:http/http.dart' as http;
import 'package:html/parser.dart' as parser;


/**
 * Función principal
 */
void main() async {
  printDay8();
}


/**
 * Función que imprime la agenda del día 8 de mayo
 */
void printDay8() async {
  var url = Uri.parse('https://holamundo.day');
  var response = await http.get(url);
  var document = parser.parse(response.body);
  var h1Elements = document.getElementsByTagName("h1");
  print("h1Elements: $h1Elements");
  var results = document.querySelectorAll('h1');


  for (var result in results) {
    if (result.text.contains('Agenda 8 de mayo')) {
      print(result.text);


      while (result.nextElementSibling!.text.contains(':')) {
        print(result.nextElementSibling!.text);
        result = result.nextElementSibling!;
      }


    }
  }
}

