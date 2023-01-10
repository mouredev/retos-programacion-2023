/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

Map<String, String> leetAlphabet = {
    'A': '4',
    'B': 'I3',
    'C': '[]',
    'D': ')',
    'E': '3',
    'F': '|=',
    'G': '&',
    'H': '#',
    'I': '1',
    'J': ',_|',
    'K': '>|',
    'L': '1',
    'M': r'/\/\',
    'N': '^/',
    'O': '0',
    'P': '|*',
    'Q': '(_,)',
    'R': 'I2',
    'S': '5',
    'T': '7',
    'U': '(_)',
    'V': r'\/',
    'W': r'\/\/',
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
  
  String result = convertToHackerCode("Hello World!");
  
  print(result);
  
  result = convertToHackerCode("mouredev");
  
  print(result);
 
}

String convertToHackerCode(String text){
    
    String convertedText = '';
    
    for (int i = 0; i < text.length; i++) {
      if (leetAlphabet.containsKey(text[i].toUpperCase())){
        convertedText = '$convertedText${leetAlphabet[text[i].toUpperCase()]}';
      }
      else{
        convertedText = '$convertedText${text[i]}';
      }
    }
    return convertedText;
}