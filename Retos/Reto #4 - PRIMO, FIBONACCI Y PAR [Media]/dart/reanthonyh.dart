import 'dart:math';

void main() {
  print(evaluateNumber(2));
  print(evaluateNumber(7));
  print(evaluateNumber(11));
  print(evaluateNumber(13));
  print(evaluateNumber(34));
}

extension IntExtention on int {
  bool get isPrime {
    if (this <= 1) {
      return false;
    }
    for (var i = 2; i < sqrt(this); i++) {
      if (this % i == 0) {
        return false;
      }
    }
    return true;
  }

  bool get isFibonacci {
    if (this == 0 || this == 1 || this == 2) {
      return true;
    }

    final fibonacciNumbers = [0, 1];
    for (var i = 2; i < this; i++) {
      final fiboNumber = fibonacciNumbers[i - 2] + fibonacciNumbers[i - 1];
      if (fiboNumber == this) {
        return true;
      }
      fibonacciNumbers.insert(i, fiboNumber);
    }
    return false;
  }

  bool get isEven {
    return this % 2 == 0;
  }
}

String evaluateNumber(int number) {
  if (!number.isNegative) {
    String isPrime = number.isPrime ? 'es primo' : 'no es primo';
    String isFibonacci = number.isFibonacci ? 'fibonacci ' : 'no es fibonacci';
    String isEven = number.isEven ? 'par' : 'impar';

    return "$number $isPrime, $isFibonacci y es $isEven";
  }
  return "$number es negativo";
}
