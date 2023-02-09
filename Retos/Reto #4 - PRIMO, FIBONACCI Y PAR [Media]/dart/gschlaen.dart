void main() {
  checkNumber(2);
  checkNumber(7);
}

void checkNumber(int num) {
  String isPrime = "es";
  String isFibonacci = "no es fibonacci";
  String isEven = "es impar";

  int i = 2;
  if (num == 1) {
    isPrime = "no es";
  }
  while (i < num) {
    if (num % i == 0) {
      isPrime = "no es";
    }
    i++;
  }

  int a = 0;
  int b = 1;
  var sum = 1;
  while (sum <= num) {
    if (sum == num) {
      isFibonacci = "fibonacci";
    }
    a = b;
    b = sum;
    sum = a + b;
  }

  if (num % 2 == 0) {
    isEven = "es par";
  }

  print("$num $isPrime primo, $isFibonacci y $isEven");
}
