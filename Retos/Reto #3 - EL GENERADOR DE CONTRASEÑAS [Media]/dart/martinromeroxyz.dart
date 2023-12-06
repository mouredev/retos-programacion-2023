/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

Map<String, Set<String>> sets = {
    'lower': {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'},
    'upper': {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'},
    'number': {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'},
    'symbol': {'!','"','#','\$','%','&','\\',',','(',')','*','+','-','.','/',':',';','<','=','>','?','@','[',']','^','_','`','{','|','}','~'},
    'empty': {}
  };

void main() {

  print(generatePassword(length: 12, containsCapitals: true, containsNumbers: false, containsSymbols: true));

}

String generatePassword({int length = 8, bool containsCapitals = true, bool containsNumbers = true, bool containsSymbols = true}) {
  if(length <= 8 || length >= 16) return 'length must be between 8 and 16 characters';

  Set<String> upper = containsCapitals ? sets['upper']! : sets['empty']!;
  Set<String> number = containsNumbers ? sets['number']! : sets['empty']!;
  Set<String> symbol = containsSymbols ? sets['symbol']! : sets['empty']!;

  List result = {...sets['lower']!, ...upper, ...number, ...symbol}.toList();

  result.shuffle();

  return result.sublist(0, length).join();
}
