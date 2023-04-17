/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */

void main() {
  print("HOLA");
  print(getParams('https://retosdeprogramacion.com?year=2023&challenge=0'));
}


List<List<String?>> getParams(String url) {

  final regexParams = RegExp(r"([?&])([^=]+)=([^&]+)");
  final params = regexParams.allMatches(url).map((match)=> [match.group(2),match.group(3)]).toList();
  return params;





}


