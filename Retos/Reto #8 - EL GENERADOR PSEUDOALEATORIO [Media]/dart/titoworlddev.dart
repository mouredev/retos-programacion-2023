/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */

void main() {
  pseudoRandomNumbers();
}

pseudoRandomNumbers() {
  String randomNum = DateTime.now().millisecond.toString();
  if (int.parse(randomNum) % 100 == 0) {
    randomNum = randomNum.replaceFirst(RegExp(r'\d'), '1');
  } else if (randomNum[1] == '0') {
    randomNum = randomNum.substring(2);
  } else {
    randomNum = randomNum.substring(1);
  }
  print(randomNum);
}
