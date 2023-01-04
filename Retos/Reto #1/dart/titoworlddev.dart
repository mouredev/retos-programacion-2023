/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

 String text = '''Hola como estas MoureDev? 
Espero que te guste mi solucion. 
¡Muchas gracias por todo lo que haces por la comunidad!''';

String solution(String text) {
  return text.split('').map((el) {
    const Map<String, String> leetAlphabet = {
      'A': '4',
      'E': '3',
      'G': '6',
      'I': '1',
      'O': '0',
      'S': '5',
      'T': '7',
    };

    return (leetAlphabet.keys.contains(el.toUpperCase()))
        ? leetAlphabet[el.toUpperCase()]!
        : el;
  }).join('');
}

void main() {
  print(solution(text));
  // Output:
  // H0l4 c0m0 35745 M0ur3D3v?
  // 35p3r0 qu3 73 6u573 m1 50luc10n. 
  // ¡Much45 6r4c145 p0r 70d0 l0 qu3 h4c35 p0r l4 c0mun1d4d!
}