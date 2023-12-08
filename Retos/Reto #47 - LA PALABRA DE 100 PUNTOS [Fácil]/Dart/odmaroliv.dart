/*
  Autor: Daniel Olivares
  Fecha de creación: 08 de diciembre de 2023
 * - Crea un programa que calcule los puntos de una palabra.
 * - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
 *   español de 27 letras, la A vale 1 y la Z 27.
 * - El programa muestra el valor de los puntos de cada palabra introducida.
 * - El programa finaliza si logras introducir una palabra de 100 puntos.
 * - Puedes usar la terminal para interactuar con el usuario y solicitarle
 *   cada palabra.
 * [NOTA] No agrege la letra anie jeje
 */

import 'dart:io';

String? input;
int suma = 0;
bool isEnd = false;
var mapaAbecedario = <String, int>{};
void main(List<String> arguments) {
  creaMapLetras();

  while (isEnd == false) {
    print('\n');
    print('Introduce una palabra:');
    print('_______________________________');
    print('\n');
    if (obtieneFrase() == true) {
      calcularPorcentaje();
      decideGanador();
      print('\n');
    }
  }
}

bool obtieneFrase() {
  try {
    input = stdin.readLineSync()?.toUpperCase().trim();
    if (input == null || input!.isEmpty) {
      print("Tienes que escribir algo");
      return false;
    }
    print('\n');
    return true;

    //input = 'YYYY';
  } catch (e) {
    print('Algo salio mal');
    return false;
  }
}

void calcularPorcentaje() {
  if (input != null || input!.isNotEmpty) {
    var txtSplite = input!.split("");

    for (var i = 0; i < input!.length; i++) {
      if (mapaAbecedario.containsKey(txtSplite[i])) {
        var mapValue = mapaAbecedario[txtSplite[i]] ?? 0;
        suma = suma + mapValue;
      }
    }
    print('**El valor de la frase es: $suma**');
    print('\n--- --- --- --- --- --- --- ---');
  }
}

void decideGanador() {
  if (suma == 100) {
    print('Felicidades, has ganado!!');
    print('Fin del juego');
    isEnd = true;
  } else if (suma > 100) {
    print('Te has pasado!');
    print('--- --- --- --- --- --- --- ---\n');
    print('[Quires salir? S/N]');
    reiniciaJuego();
    isEnd = stdin.readLineSync()?.toUpperCase() == 'S' ? true : false;
  } else {
    print('Te ha faltado!');
    print('--- --- --- --- --- --- --- ---\n');
    print('[Quires salir? S/N]');
    reiniciaJuego();
    isEnd = stdin.readLineSync()?.toUpperCase() == 'S' ? true : false;
  }
}

void creaMapLetras() {
  var letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
  var valorLetra = 1;

  for (var letra in letras) {
    mapaAbecedario[letra] = valorLetra++;
  }
}

void reiniciaJuego() {
  suma = 0;
}
