void main() {
  for (int i = 0; i < 100; i++) {
    random();
  }
}

random() {
  final number1 = DateTime.now().microsecondsSinceEpoch;
  final number2 = DateTime.now().millisecondsSinceEpoch;
  String str = (number1 * number2).toString();
  str = str.substring(str.length - 2, str.length);
  print(int.parse(str) + 1);
}
