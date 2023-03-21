void main() {
  print(isHeterogram("hola"));
  print(isHeterogram("olla"));
  print(isIsogram("hola"));
  print(isIsogram("olla"));
  print(isPangram("Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú"));
}

Map<String, int> countLetters(String text) {
  final letters = text.toLowerCase().replaceAll(RegExp('[^A-ZÑa-zñ]'), '');
  Map<String, int> counts = {};
  for (int i = 0; i < letters.length; i++) {
    counts.update(
      letters[i],
      (value) => value + 1,
      ifAbsent: () => counts[letters[i]] = 1,
    );
  }
  return counts;
}

String isHeterogram(String text) {
  final counts = countLetters(text);
  bool heterogram = counts.values.every((element) => element == 1);
  return heterogram ? "$text es heterograma" : "$text no es heterograma";
}

String isIsogram(String text) {
  final counts = countLetters(text);
  int count = counts.values.first;
  bool isogram = counts.values.every((element) => element == count);
  return isogram ? "$text es isograma" : "$text no es isograma";
}

String isPangram(String text) {
  final counts = countLetters(text);
  bool pangram = counts.length == 27;
  return pangram ? "$text es pangrama" : "$text no es pangrama";
}
