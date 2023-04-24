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

const Map<String, String> leetAlphabet = {
  'A': '4',
  'B': 'I3',
  'C': '[',
  'D': ')',
  'E': '3',
  'F': '|=',
  'G': '&',
  'H': '#',
  'I': '1',
  'J': ',_|',
  'K': '>|',
  'L': '1',
  'M': '/\\/\\',
  'N': '^/',
  'O': '0',
  'P': '|*',
  'Q': '(_,)',
  'R': 'I2',
  'S': '5',
  'T': '7',
  'U': '(_)',
  'V': '\\/',
  'W': '\\/\\/',
  'X': '><',
  'Y': 'j',
  'Z': '2',
};

// Solucion 1
String solution(String text) => text
    .toUpperCase()
    .split('')
    .map((el) => (leetAlphabet.keys.contains(el)) ? leetAlphabet[el]! : el)
    .join('');

// Solucion 2
String solution2(String text) => text
    .toUpperCase()
    .replaceAllMapped(RegExp(r'(\w)'), (m) => '${leetAlphabet[m[1]]}');

void main() {
  print(solution(text) + '\n');
  print(solution2(text));
  // Output:
  // #014 [0/\/\0 35745 /\/\0(_)I23)3\/?
  // 35|*3I20 (_,)(_)3 73 &(_)573 /\/\1 501(_)[10^/.
  // ¡/\/\(_)[#45 &I24[145 |*0I2 70)0 10 (_,)(_)3 #4[35 |*0I2 14 [0/\/\(_)^/1)4)!
}