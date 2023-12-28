/*
 * Crea un programa que encuentre y muestre todos los pares de números primos
 * gemelos en un rango concreto.
 * El programa recibirá el rango máximo como número entero positivo.
 * 
 * - Un par de números primos se considera gemelo si la diferencia entre
 *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
 *
 * - Ejemplo: Rango 14
 *   (3, 5), (5, 7), (11, 13)
 */

void main() {
  print(primeCouples(14));
  print(primeCouples(129));
}

String primeCouples(int range) {
  int prePrime = 2;
  String couple = '';
  List primeList = [];

  bool isPrime(int numero) {
    if (numero <= 1) {
      return false;
    }
    for (int i = 2; i < numero; i++) {
      if (numero % i == 0) {
        return false;
      }
    }
    return true;
  }

  for (int i = 2; i < range; i++) {
    if (isPrime(i)) {
      if (i == prePrime + 2) {
        couple = '($prePrime, $i)';
        primeList.add(couple);
      }
      prePrime = i;
    }
  }

  return 'Rango $range\n ${primeList.join(', ')}';
}
