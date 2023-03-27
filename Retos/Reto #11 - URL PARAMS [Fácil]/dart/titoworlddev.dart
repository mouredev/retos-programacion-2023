/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */

void main() {
  print(getParams("https://retosdeprogramacion.com?year=2023&challenge=0"));
}

List getParams(String url) {
  final uri = Uri.parse(url);
  final params = uri.queryParameters;
  return params.values.toList();
}
