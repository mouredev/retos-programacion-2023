/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

void checkPrimeFiboEven(int number) {
  String isPrimeResult() {
    for (int i = 0; i < (number + 100); i++) {
      if (i != 1 && i != number) {
        if (number % i == 0) return '$number no es primo';
      }
    }
    return '$number es primo';
  }

  String isFibonacciResult() {
    List<int> fibonacci = [];
    for (int i = 0; i < (number + 18); i++) {
      if (i > 1) {
        fibonacci.add(fibonacci[i - 2] + fibonacci[i - 1]);
      } else {
        fibonacci.add(i);
      }
    }

    return fibonacci.contains(number) ? '' : 'no ';
  }

  String isOddResult() {
    return number.isOdd ? 'impar' : 'par';
  }

  String answer =
      '${isPrimeResult()}, ${isFibonacciResult()}es fibonacci y es ${isOddResult()}';
  print(answer);
}

void main() {
  checkPrimeFiboEven(2);
  checkPrimeFiboEven(7);
  checkPrimeFiboEven(12765);
  checkPrimeFiboEven(1597);
  checkPrimeFiboEven(216);
  checkPrimeFiboEven(610);
}
