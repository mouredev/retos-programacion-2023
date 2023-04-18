/*
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 * 
 * Ejemplo: 4
 *         _
 *       _|       
 *     _|
 *   _|
 * _|
 * 
 */

void main() {
  print(drawLadder(4));
}

drawLadder(int stairsNum) {
  const upStair = '_|';
  const downStair = '|_';
  const finalStair = '_';
  String ladder = '';

  for (int i = 0; i <= stairsNum; i++) {
    if (stairsNum.isNegative) {
      final spaces = ' ' * (2 * i);
      if (i == 0) {
        ladder += '$finalStair\n';
      } else {
        ladder += '$spaces$downStair\n';
      }
    } else {
      final spaces = ' ' * ((2 * stairsNum) - (i * 2));
      if (i == 0) {
        ladder += '$spaces$finalStair\n';
      } else {
        ladder += '$spaces$upStair\n';
      }
    }
  }

  return ladder;
}
