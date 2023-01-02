void main() {
  for (var i = 1; i <= 100; i++) {
    var result = "$i. ";

    if (i % 3 == 0) {
      result += "fizz";
    }
    if (i % 5 == 0) {
      result += "buzz";
    }

    print("$result\n");
  }
}