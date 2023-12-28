import 'dart:math' as math;

void main() {
  final triplesFound = searchForPythagoreanTriples(10);
  print(triplesFound);
}

List<int> generateNumbers(int limit) {
  return List.generate(limit, (int index) => (index + 1));
}

List<List<int>> searchForPythagoreanTriples(int limit) {
  final List<List<int>> pythagoreanTriples = [];

  if (limit <= 0) return pythagoreanTriples;

  final List<int> numbers = generateNumbers(limit);

  for (int i = 0; i < numbers.length; i++) {
    for (int j = i + 1; j < numbers.length; j++) {
      final int a = numbers[i];
      final int b = numbers[j];
      final num cSquare = math.pow(a, 2) + math.pow(b, 2);

      final num c = math.sqrt(cSquare);

      if (c is int) {
        pythagoreanTriples.add([a, b, c.toInt()]);
      }
    }
  }

  return pythagoreanTriples;
}
