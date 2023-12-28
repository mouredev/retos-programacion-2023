void main() {
  for (int i = 1; i <= 100; i++) {
    if (i % 3 == 0) {
      print(i % 5 == 0 ? "fizzbuzz" : "fizz");
    } else if (i % 5 == 0) {
      print('buzz');
    } else {
      print(i);
    }
  }
}
