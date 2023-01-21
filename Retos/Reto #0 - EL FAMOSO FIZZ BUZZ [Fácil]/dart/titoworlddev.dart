/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz"
 * - Múltiplos de 5 por la palabra "buzz"
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz"
 */

void fizzbuzz() {
  for (int i = 1; i <= 100; i++) {
    (i % 5 == 0 && i % 3 == 0)
        ? print('fizzbuzz')
        : (i % 3 == 0)
            ? print('fizz')
            : (i % 5 == 0)
                ? print('buzz')
                : print(i);
  }
}

void main() {
  fizzbuzz();
}