import 'dart:math';

void main() {
  const letters = [
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z'
  ];

  int excelColumn(String column) {
    int result = 0;

    // Si la columna es unica devuelve la letra en la posicion indicada
    if (column.split('').length == 1 &&
        letters.contains(column.toUpperCase())) {
      return letters.indexOf(column.toUpperCase()) + 1;
    }

    // Si son varias letras divide el string para obtener los caracteres
    List arrayResult = column.split('');

    // Itera el arreglo para obtener la suma de las posiciones
    for (int i = 0; i < arrayResult.length; i++) {
      // Obtiene el indice de la letra dentro del arreglo de letras
      int indx = letters.indexOf(arrayResult[i]);

      // Obtiene el exponente de acuerdo a la posicion del elemento dentro del arreglo
      // Formula: (26 ^ (array.length - [indice + 1 ]);
      num indexExp = pow(26, arrayResult.length - (i + 1));

      //Acumula el resultado del indice de la letra por el exponente correspondiente
      //en la variable result
      result += (indx + 1) * indexExp.toInt();
    }

    // Devuelve el resultado de la suma de las letras de acuerdo a su posicion para
    // dar el valor de la columna
    return result;
  }

  print(excelColumn('A'));
  print(excelColumn('Z'));
  print(excelColumn('AA'));
  print(excelColumn('CA'));
}
