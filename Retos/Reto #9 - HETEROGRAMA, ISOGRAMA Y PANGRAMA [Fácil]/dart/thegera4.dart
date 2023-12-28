/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */

void main() {
  String texto = 'El veloz murciélago hindú comía feliz cardillo y kiwi.';
  print('Heterograma: ${esHeterograma(texto)}');
  print('Isograma: ${esIsograma(texto)}');
  print('Pangrama: ${esPangrama(texto)}');
}

bool esHeterograma(String texto) {
  texto = texto.toLowerCase();
  for (int i = 0; i < texto.length; i++) {
    if (texto[i] == ' ') continue;
    for (int j = i + 1; j < texto.length; j++) {
      if (texto[i] == texto[j]) return false;
    }
  }
  return true;
}

bool esIsograma(String texto) {
  texto = texto.toLowerCase();
  for (int i = 0; i < texto.length; i++) {
    if (texto[i] == ' ') continue;
    for (int j = i + 1; j < texto.length; j++) {
      if (texto[i] == texto[j]) return false;
    }
  }
  return true;
}

bool esPangrama(String texto) {
  texto = texto.toLowerCase();
  for (int i = 97; i <= 122; i++) {
    if (!texto.contains(String.fromCharCode(i))) return false;
  }
  return true;
}