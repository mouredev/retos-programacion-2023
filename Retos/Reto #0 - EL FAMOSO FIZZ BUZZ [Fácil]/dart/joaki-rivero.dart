void main() {
  _fizzbuzz();
}

void _fizzbuzz() {
  for (var i = 1; i <= 100; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
      print("fizzbuzz\n");
    }
    else if (i % 3 == 0) {
      print("fizz\n");
    }
    else if (i % 5 == 0) {
      print("buzz\n");
    } else {
      print("$i\n");
    }
  }
}