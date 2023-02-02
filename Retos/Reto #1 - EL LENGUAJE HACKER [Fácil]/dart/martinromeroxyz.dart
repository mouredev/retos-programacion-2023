/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

final Map<String, String> leet = {
  'A': '4',
  'Á': '4',
  'B': 'I3',
  'C': '[',
  'D': ')',
  'E': '3',
  'É': '3',
  'F': '|=',
  'G': '&',
  'H': '#',
  'I': '1',
  'Í': '1',
  'J': ',_|',
  'K': '>|',
  'L': '1',
  'M': '/\\/\\',
  'N': '^/',
  'O': '0',
  'Ó': '0',
  'P': '|*',
  'Q': '(_,)',
  'R': 'I2',
  'S': '5',
  'T': '7',
  'U': '(_)',
  'Ú': '(_)',
  'V': '\\/',
  'W': '\\/\\/',
  'X': '><',
  'Y': 'j',
  'Z': '2',
  '1': 'L', 
  '2': 'R',	
  '3': 'E',	
  '4': 'A',	
  '5': 'S',	
  '6': 'b',	
  '7': 'T',	
  '8': 'B',	
  '9': 'g',	
  '0': 'o'
};

void main() {
  print(translateToLeet('alta cohesión, bajo acoplamiento'));
}

String translateToLeet(String text) {
  String result = '';
  
  text.split('').forEach((ch) => result += leet[ch.toUpperCase()] ?? ch);
  
  return result;
}
